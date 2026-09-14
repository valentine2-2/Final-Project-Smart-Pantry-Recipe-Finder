# 📄 SPRINT1_REPORT.md

**Project Name:** Smart Pantry & Recipe Finder  
**Sprint:** 1 (Foundation & Core Structure)[cite: 1, 2]  
**Date:** September 15, 2026[cite: 1, 2]  

---

## 👥 1. Team Members & Code Responsibilities

* **🏗️ Planner (Architect):** ไทน์ (Phattharawadee) — Designed system architecture, flow, UI headers (`display_welcome`, `display_credits`), and continuous execution loop (`main()`)[cite: 1, 2].
* **🔨 Coders (Builders):** ฟ่า & ภีม (Sujeephon & Team) — Implemented core functions: `add_item()` dictionary storage, `view_pantry()` display, and `search_item()` partial string matching[cite: 1, 2].
* **🐞 Debugger (Finisher):** โดนัท — Added input validation for empty strings, positive number verification (`qty > 0`), `ValueError` handling, and fallback for invalid commands[cite: 1, 2].

---

## 📌 2. Progress Summary & Function Traceability

* **`display_welcome()` & `display_credits()`**: Renders onboarding banners and attributes team roles[cite: 1, 2].
* **`add_item(pantry)`**: Saves new items into a dictionary, aggregates quantities for existing items, and validates non-empty names with positive numeric inputs[cite: 1, 2].
* **`view_pantry(pantry)`**: Displays active stock using `qty.is_integer()` to remove trailing decimals for whole numbers[cite: 1, 2].
* **`search_item(pantry)`**: Performs case-insensitive partial keyword matching (`keyword in item`)[cite: 1, 2].
* **`main()`**: Manages main control flow with normalized input processing (`.strip().lower()`)[cite: 1, 2].

---

## 🐞 3. Quality Assurance & Debugging Report

| Test Item / Function | Input Used | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :---: |
| **Welcome & Credits** | `credits` | Display team member roles | Showed full team credits correctly | **PASSED**[cite: 1, 2] |
| **Add New Item** | Name: `egg`, Qty: `12` | Save to pantry dict | `✅ เพิ่มวัตถุดิบ 'egg' จำนวน 12.0 เข้าคลังเรียบร้อย!` | **PASSED**[cite: 1, 2] |
| **Update Existing Item** | Name: `egg`, Qty: `6` | Aggregate quantity to 18 | `✅ อัปเดตจำนวน 'egg' เพิ่มขึ้น 6.0 (รวมทั้งหมด: 18.0)` | **PASSED**[cite: 1, 2] |
| **Validation: Empty Name** | Name: ` ` (space) | Block and display error prompt | `❌ ข้อผิดพลาด: ชื่อวัตถุดิบห้ามเป็นค่าว่าง!` | **PASSED**[cite: 1, 2] |
| **Validation: Non-Numeric** | Qty: `abc` | Catch ValueError gracefully | `❌ ข้อผิดพลาด: กรุณากรอกจำนวนเป็นตัวเลขเท่านั้น!` | **PASSED**[cite: 1, 2] |
| **Validation: Negative Qty** | Qty: `-5` | Block non-positive values | `❌ ข้อผิดพลาด: จำนวนวัตถุดิบต้องมากกว่า 0!` | **PASSED**[cite: 1, 2] |
| **View Pantry** | `view` | Display items without trailing `.0` | `• egg: 18` | **PASSED**[cite: 1, 2] |
| **Search Item** | Keyword: `eg` | Find matching key `egg` | `พบวัตถุดิบที่เกี่ยวข้องกับ 'eg': • egg: 18` | **PASSED**[cite: 1, 2] |
| **Input Normalization** | ` ADD `, `QUIT` | Strip spaces and lowercase | Commands routed without syntax errors | **PASSED**[cite: 1, 2] |
| **Invalid Command** | `delete` | Prompt invalid command alert | `❌ คำสั่งไม่ถูกต้อง กรุณากรอกพิมพ์คำสั่ง...` | **PASSED**[cite: 1, 2] |

---

## 💬 4. Weekly Retrospective (Wow! & Whoops!)

**🌟 Wow! (What Went Well)**
* **Robust Input Validation:** Donut's validation logic prevents application crashes across empty strings, non-numerics, and negative values[cite: 1, 2].
* **Partial Search Utility:** Peem's search logic allows locating items using partial keywords[cite: 1, 2].
* **Clean Number Rendering:** `qty.is_integer()` converts floats like `12.0` to `12` while preserving decimal values[cite: 1, 2].
* **User Interface Polish:** Command normalization ensures robust navigation regardless of capitalization or whitespace[cite: 1, 2].

**⚠️ Whoops! (Found & Action Plan)**
* **In-Memory Storage Only:** Data resets when the program terminates; action plan is to migrate to SQLite in Sprint 2[cite: 1, 2].
* **Flat Quantity Structure:** Pantry maps `string -> float` without units or expiry dates; action plan is to refactor data structures to OOP classes in Sprint 2[cite: 1, 2].
* **No Recipe Engine Yet:** Sprint 1 focused on Pantry CLI foundation; action plan is to implement Recipe Finder and Spoonacular API in Sprint 2[cite: 1, 2].

---

## 🚀 5. Sprint 2 Roadmap & Transition Plan

* **OOP Refactoring:** Convert procedural functions into `PantryStore`, `RecipeManager`, and `SmartPantryApp` classes[cite: 1, 2].
* **Expiry & Unit Tracking:** Support units (grams, pcs) and expiry date calculations using `datetime`[cite: 1, 2].
* **Recipe Matching Engine:** Match inventory with recipes and calculate Shopping Lists[cite: 1, 2].
* **Database Integration:** SQLite persistence to store user inventory permanently[cite: 1, 2].
