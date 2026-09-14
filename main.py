"""
==============================================================================
📦 Project: Smart Pantry & Recipe Finder
🎯 Sprint: 1 - Foundation & Core Structure

👥 รายชื่อและบทบาทหน้าที่ของสมาชิกในทีม:
  - 🏗️ Planner (Architect) : ไทน์  (วางโครงสร้างระบบ ออกแบบ Flow และความสัมพันธ์ของข้อมูล)
  - 🔨 Coders (Builders)    : ฟ่า & ภีม (เขียนฟังก์ชันหลัก เช่น เพิ่ม, ดูรายการ, ค้นหา)
  - 🐞 Debugger (Finisher)  : โดนัท  (ดักจับ Error, จัดการ Input Validation และขัดเกลาโค้ด)
==============================================================================
"""

# ==============================================================================
# 🏗️ SYSTEM ARCHITECTURE & INTERFACE (Planner: ไทน์)
# ==============================================================================

def display_welcome():
    """
    [Architect: ไทน์ | Builder: ฟ่า]
    แสดงข้อความต้อนรับและแบนเนอร์เริ่มต้นของโปรแกรม
    """
    print("==========================================")
    print("  ยินดีต้อนรับสู่ Smart Pantry & Recipe Finder! 🥣 ")
    print("==========================================")


def display_credits():
    """
    [Architect: ไทน์ | Finisher: โดนัท]
    แสดงข้อมูลบทบาทหน้าที่ของทีมพัฒนาโปรเจกต์
    """
    print("\n--- 👥 รายชื่อทีมพัฒนาโปรเจกต์ ---")
    print("• 🏗️ Planner (Architect) : ไทน์  [ออกแบบโครงสร้าง & Flow]")
    print("• 🔨 Coders (Builders)    : ฟ่า & ภีม [พัฒนาฟังก์ชันระบบ]")
    print("• 🐞 Debugger (Finisher)  : โดนัท  [ตรวจสอบ Error & Input Validation]")


# ==============================================================================
# 🔨 CORE FUNCTIONS (Builders: ฟ่า & ภีม)
# ==============================================================================

def add_item(pantry):
    """
    [Builder: ฟ่า | Finisher: โดนัท]
    รับค่าและเพิ่มวัตถุดิบเข้าคลัง (หรืออัปเดตจำนวนเดิม)
    """
    print("\n--- ➕ เพิ่มวัตถุดิบเข้าคลัง ---")
    item_name = input("ระบุชื่อวัตถุดิบ: ").strip().lower()

    # [Finisher: โดนัท] Validation - ป้องกันการใส่ชื่อว่างเปล่า
    if not item_name:
        print("❌ ข้อผิดพลาด: ชื่อวัตถุดิบห้ามเป็นค่าว่าง!")
        return

    quantity_input = input(f"ระบุจำนวนของ '{item_name}': ").strip()

    # [Finisher: โดนัท] Validation - ตรวจสอบว่ากรอกตัวเลขถูกต้องและมากกว่า 0
    try:
        quantity = float(quantity_input)
        if quantity <= 0:
            print("❌ ข้อผิดพลาด: จำนวนวัตถุดิบต้องมากกว่า 0!")
            return
    except ValueError:
        print("❌ ข้อผิดพลาด: กรุณากรอกจำนวนเป็นตัวเลขเท่านั้น!")
        return

    # [Builder: ฟ่า] บันทึกข้อมูลลงใน Dictionary
    if item_name in pantry:
        pantry[item_name] += quantity
        print(f"✅ อัปเดตจำนวน '{item_name}' เพิ่มขึ้น {quantity} (รวมทั้งหมด: {pantry[item_name]})")
    else:
        pantry[item_name] = quantity
        print(f"✅ เพิ่มวัตถุดิบ '{item_name}' จำนวน {quantity} เข้าคลังเรียบร้อย!")


def view_pantry(pantry):
    """
    [Builder: ภีม | Finisher: โดนัท]
    แสดงรายการวัตถุดิบทั้งหมดในคลัง
    """
    if not pantry:
        print("\nℹ️ ขณะนี้ยังไม่มีวัตถุดิบในคลังของคุณ")
        return

    print(f"\n--- 🧺 รายการวัตถุดิบในคลัง ({len(pantry)} รายการ) ---")
    for item, quantity in pantry.items():
        # แสดงผลถ้าเป็นจำนวนเต็ม ให้แสดงแบบไม่มีจุดทศนิยม
        qty_display = int(quantity) if quantity.is_integer() else quantity
        print(f"• {item}: {qty_display}")


def search_item(pantry):
    """
    [Builder: ภีม | Finisher: โดนัท]
    ค้นหาวัตถุดิบที่มีอยู่ในคลัง
    """
    print("\n--- 🔍 ค้นหาวัตถุดิบ ---")
    keyword = input("พิมพ์ชื่อวัตถุดิบที่ต้องการค้นหา: ").strip().lower()

    # [Finisher: โดนัท] Validation
    if not keyword:
        print("❌ ข้อผิดพลาด: กรุณากรอกคำค้นหา!")
        return

    # [Builder: ภีม] ค้นหาแบบ Partial Match (พิมพ์แค่บางคำก็เจอ)
    results = {item: qty for item, qty in pantry.items() if keyword in item}

    if results:
        print(f"\nพบวัตถุดิบที่เกี่ยวข้องกับ '{keyword}':")
        for item, qty in results.items():
            qty_display = int(qty) if qty.is_integer() else qty
            print(f"• {item}: {qty_display}")
    else:
        print(f"❌ ไม่พบวัตถุดิบที่มีคำว่า '{keyword}' ในคลัง")


# ==============================================================================
# 🎮 MAIN PROGRAM LOOP (Planner: ไทน์ | Finisher: โดนัท)
# ==============================================================================

def main():
    """
    [Architect: ไทน์] วาง Loop ควบคุมทิศทางโปรแกรม
    [Finisher: โดนัท] เพิ่ม Exception Control และดักจับคำสั่งที่ไม่ถูกต้อง
    """
    pantry = {}
    display_welcome()

    while True:
        print("\n------------------------------------------")
        print("เลือกคำสั่ง: [add] เพิ่ม | [view] ดูคลัง | [search] ค้นหา | [credits] ทีมงาน | [quit] ออก")
        command = input("> ").strip().lower()

        if command == "quit":
            print("\n👋 ขอบคุณที่ใช้งาน Smart Pantry & Recipe Finder สวัสดีครับ/ค่ะ!")
            break
        elif command == "add":
            add_item(pantry)
        elif command == "view":
            view_pantry(pantry)
        elif command == "search":
            search_item(pantry)
        elif command == "credits":
            display_credits()
        else:
            # [Finisher: โดนัท] จัดการคำสั่งที่ไม่ตรงกับรายการที่รองรับ
            print("❌ คำสั่งไม่ถูกต้อง กรุณากรอกพิมพ์คำสั่งที่ระบุในวงเล็บเท่านั้น")


if __name__ == "__main__":
    main()
