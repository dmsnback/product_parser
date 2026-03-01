import time

import scrapy

from product_parser.items import ProductParserItem
from product_parser.utils import (
    get_assets,
    get_brand,
    get_metadata,
    get_price_data,
    get_stock,
    get_title,
)

START_URLS = [
    "https://alkoteka.com/catalog/vino",
    "https://alkoteka.com/catalog/shampanskoe-i-igristoe",
    "https://alkoteka.com/catalog/krepkiy-alkogol",
]


class AlkotekaCatalogSpider(scrapy.Spider):
    name = "alkoteka_catalog"
    allowed_domains = ["alkoteka.com"]

    city_uuid = "4a70f9e0-46ae-11e7-83ff-00155d026416"
    page = 1
    per_page = 20
    max_counts_products = 100

    def start_requests(self):
        for url in START_URLS:
            category_slug = url.rstrip("/").split("/")[-1]
            api_url = f"https://alkoteka.com/web-api/v1/product?city_uuid={self.city_uuid}&page={self.page}&per_page={self.per_page}&root_category_slug={category_slug}"

            yield scrapy.Request(
                url=api_url,
                method="GET",
                headers={"Accept": "application/json"},
                meta={"slug": category_slug, "page": self.page, "count": 0},
                callback=self.parse_api,
            )

    def parse_api(self, response):
        slug_category = response.meta["slug"]
        page = response.meta["page"]
        count = response.meta["count"]

        data = response.json()
        products = data.get("results", [])
        for product in products:
            if count >= self.max_counts_products:
                return
            count += 1
            product_url = product.get("product_url")
            slug_product = product_url.rstrip("/").split("/")[-1]
            product_url_api = f"https://alkoteka.com/web-api/v1/product/{slug_product}?city_uuid={self.city_uuid}"

            marketing_tags = [
                label.get("title") for label in product.get("action_labels")
            ]

            yield scrapy.Request(
                url=product_url_api,
                method="GET",
                headers={"Accept": "application/json"},
                meta={
                    "product_url": product_url,
                    "marketing_tags": marketing_tags,
                },
                callback=self.parse,
            )

        if products and count < self.max_counts_products:
            page += 1
            api_url = f"https://alkoteka.com/web-api/v1/product?city_uuid={self.city_uuid}&page={page}&per_page={self.per_page}&root_category_slug={slug_category}"

            yield scrapy.Request(
                url=api_url,
                method="GET",
                headers={"Accept": "application/json"},
                meta={"slug": slug_category, "page": page, "count": count},
                callback=self.parse_api,
            )

    def parse(self, response):
        product_url = response.meta["product_url"]
        marketing_tags = response.meta["marketing_tags"]

        data = response.json()
        product = data.get("results", [])

        item = ProductParserItem(
            timestamp=int(time.time()),
            RPC=str(product.get("vendor_code")),
            url=product_url,
            title=get_title(product),
            marketing_tags=marketing_tags,
            brand=get_brand(product),
            section=product.get("category", {}).get("name"),
            price_data=get_price_data(product),
            stock=get_stock(product),
            assets=get_assets(product),
            metadata=get_metadata(product),
            variants=1,
        )

        yield item
