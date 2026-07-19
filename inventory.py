import json
import os


DATA_FILE = "items.json"


def create_initial_db(filename=DATA_FILE):
    
    if not os.path.exists(filename):
        initial_items = [
            {
                "code": "N1001",
                "name": "Mechanical Keyboard",
                "quantity": 15,
            },
            {
                "code": "N1002",
                "name": "Ergonomic Mouse",
                "quantity": 30,
            },
        ]

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(initial_items, file, ensure_ascii=False, indent=4)


def load_items(filename=DATA_FILE):
    """อ่านข้อมูลสินค้าจากไฟล์ JSON และคืนค่าเป็น list"""
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            items = json.load(file)

        if isinstance(items, list):
            return items

        return []
    except (json.JSONDecodeError, OSError):
        return []


def save_items(items, filename=DATA_FILE):
    """บันทึกข้อมูลสินค้าลงในไฟล์ JSON"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(items, file, ensure_ascii=False, indent=4)


def list_items(items):
    """แสดงรายการสินค้าทั้งหมดพร้อมจำนวนคงเหลือ"""
    if not items:
        print("ยังไม่มีสินค้าในระบบ")
        return

    print(f"{'รหัส':<12} {'ชื่อสินค้า':<25} {'จำนวนคงเหลือ':>12}")
    print("-" * 52)

    for item in items:
        code = item.get("code", "-")
        name = item.get("name", "-")
        quantity = item.get("quantity", 0)
        print(f"{code:<12} {name:<25} {quantity:>12}")


def add_item(items, code, name, quantity, filename=DATA_FILE):
    """เพิ่มสินค้าใหม่ โดยตรวจสอบรหัสซ้ำและจำนวนติดลบ"""
    if not (code.startswith('N') or code.startswith('P')):
        print("รหัสสินค้าต้องขึ้นต้นด้วย N (สำหรับสินค้าใหม่) หรือ P (สำหรับสินค้าที่เพิ่มจากตัวเดิม)")
        return None

    if not code[1:].isdigit() or len(code) == 1:
        print("รหัสสินค้าต้องตามด้วยตัวเลขเท่านั้น")
        return None

    duplicate = any(item.get("code") == code for item in items)

    if duplicate:
        print("รหัสสินค้าซ้ำ")
        return None

    if quantity < 0:
        print("จำนวนสินค้าต้องไม่ติดลบ")
        return None

    new_item = {
        "code": code,
        "name": name,
        "quantity": quantity,
    }

    items.append(new_item)
    save_items(items, filename)
    return new_item


def receive_stock(items, code, quantity, filename=DATA_FILE):
    """รับสินค้าเข้าและบันทึกจำนวนคงเหลือใหม่"""
    if quantity <= 0:
        print("จำนวนรับเข้าต้องมากกว่า 0")
        return None

    for item in items:
        if item.get("code") == code:
            item["quantity"] = item.get("quantity", 0) + quantity
            save_items(items, filename)
            return item

    print("ไม่พบสินค้า")
    return None


def issue_stock(items, code, quantity, filename=DATA_FILE):
    """จ่ายสินค้าออกโดยป้องกันจำนวนคงเหลือติดลบ"""
    if quantity <= 0:
        print("จำนวนจ่ายออกต้องมากกว่า 0")
        return None

    for item in items:
        if item.get("code") == code:
            current_quantity = item.get("quantity", 0)

            if quantity > current_quantity:
                print("จำนวนคงเหลือไม่พอ")
                return None

            item["quantity"] = current_quantity - quantity
            save_items(items, filename)
            return item

    print("ไม่พบสินค้า")
    return None