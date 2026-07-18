import json


def load_items(path="item.json"):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"ไม่พบไฟล์ {path}")
        return []
    except json.JSONDecodeError:
        print(f"ไฟล์ {path} มีรูปแบบ JSON ไม่ถูกต้อง")
        return []


def update_quantity(items, code, change):
    for item in items:
        if item.get("code") == code:
            current_quantity = item.get("quantity", 0)
            new_quantity = current_quantity + change

            if new_quantity < 0:
                print("จำนวนคงเหลือไม่พอ")
                return items

            item["quantity"] = new_quantity
            return items

    print(f"ไม่พบสินค้ารหัส {code}")
    return items


if __name__ == "__main__":
    items = load_items()

    print(">>> เริ่มต้น:", items)

    print("\n[ทดสอบ Task-06] สั่งตัด P001 จำนวน 100 ชิ้น:")
    update_quantity(items, "P001", -100)

    print("\n[ทดสอบปกติ] สั่งตัด P002 จำนวน 10 ชิ้น:")
    update_quantity(items, "P002", -10)

    print(">>> ล่าสุด:", items)