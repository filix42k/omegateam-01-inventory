import json
import os

DB_FILE = 'items.json'

def create_initial_db():
    """สร้างไฟล์ items.json พร้อมข้อมูลเริ่มต้น หากยังไม่มีไฟล์"""
    if not os.path.exists(DB_FILE):
        initial_items = [
            {
                "id": 1,
                "name": "Mechanical Keyboard",
                "category": "Electronics",
                "price": 3200.00,
                "quantity": 15
            },
            {
                "id": 2,
                "name": "Ergonomic Mouse",
                "category": "Electronics",
                "price": 1850.50,
                "quantity": 30
            }
        ]
        
        # เขียนข้อมูลลงไฟล์ JSON
        with open(DB_FILE, 'w', encoding='utf-8') as file:
            json.dump(initial_items, file, ensure_ascii=False, indent=4)
        print(f"✅ สร้างไฟล์ {DB_FILE} สำเร็จ")
    else:
        print(f"ℹ️ ไฟล์ {DB_FILE} มีอยู่แล้ว")

def load_items():
    """อ่านข้อมูลสินค้าทั้งหมดจากไฟล์ JSON"""
    if not os.path.exists(DB_FILE):
        return []
        
    with open(DB_FILE, 'r', encoding='utf-8') as file:
        items = json.load(file)
        return items

# ทดสอบการทำงานเมื่อรันไฟล์นี้โดยตรง
if __name__ == "__main__":
    create_initial_db()
    
    # ทดสอบฟังก์ชัน load_items
    current_items = load_items()
    print(f"📦 จำนวนสินค้าในระบบ: {len(current_items)} รายการ")
    for item in current_items:
        print(f"- [{item['id']}] {item['name']} ({item['price']} THB) เหลือ: {item['quantity']}")