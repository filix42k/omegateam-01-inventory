import json

def load_items():
    with open("items.json", "r", encoding="utf-8") as f:
        return json.load(f)


def update_quantity(items, code, change):
    for item in items:
        if item["code"] == code:
            new_qty = item["quantity"] + change
            if new_qty < 0:
                print("จำนวนคงเหลือไม่พอ")
                return items
            item["quantity"] = new_qty
            return items
    print("ไม่พบสินค้ารหัสนี้")
    return items