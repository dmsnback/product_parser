def get_title(product):
    """Получение названия товара"""
    title = [product.get("name", "")]

    for label in product.get("filter_labels"):
        if label.get("filter") in ["obem", "cvet"] and label.get("title"):
            title.append(label["title"])
    return ", ".join(title)


def get_brand(product):
    """Получение названия бренда товара"""
    brand = ""

    for block in product.get("description_blocks", []):
        if block.get("code") == "brend":
            values = block.get("values", [])
            if values:
                brand = values[0].get("name")
    return brand


def get_price_data(product):
    """Получениее цены товара и расчёт процента скидки"""
    current = product.get("prev_price")
    original = product.get("price")

    if not current:
        current = product.get("price")
    discount_percentage = 0
    if current is not None and original is not None:
        discount_percentage = (
            (float(current) - float(original)) / float(current) * 100
        )
    return {
        "current": float(current),
        "original": float(original),
        "sale_tag": f"Скидка {int(discount_percentage)}%",
    }


def get_stock(product):
    """Получение информации о наличии товара и количестве"""
    in_stock = product.get("available", False)
    count = product.get("quantity_total", 0)
    return {"in_stock": in_stock, "count": count}


def get_assets(product):
    """Получение информации о изображениях товара"""
    main_image = product.get("image_url", "")
    set_images = []
    view360 = []
    video = []
    return {
        "main_image": main_image,
        "set_images": set_images,
        "view360": view360,
        "video": video,
    }


def get_metadata(product):
    """Получение описания и других характеристик товара"""
    rpc = product.get("vendor_code")
    description = ""
    proizvoditel = ""
    country = product.get("country_name")
    color = ""
    krepost = ""
    volume = ""

    for block in product.get("text_blocks"):
        if block.get("title") == "Описание":
            description = (
                block.get("content").replace("<br>", " ").replace("\n", " ")
            )

    for block in product.get("description_blocks", []):
        code = block.get("code")
        if code == "proizvoditel":
            values = block.get("values", [])
            if values:
                proizvoditel = values[0].get("name")
        elif code == "cvet":
            values = block.get("values", [])
            if values:
                color = values[0].get("name")
        elif code == "krepost":
            krepost = f"min-{block.get('min')}%, max-{block.get('max')}%"

        elif code == "obem":
            volume = f"min-{block.get('min')}л., max-{block.get('max')}л."

    return {
        "__description": description,
        "Артикул": str(rpc),
        "Страна производитель": country,
        "Производитель": proizvoditel,
        "Цвет": color,
        "Объём": volume,
        "Крепость": krepost,
    }
