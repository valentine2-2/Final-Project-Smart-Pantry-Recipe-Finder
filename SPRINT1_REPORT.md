# 📄 SPRINT 1 RESULT REPORT

**Project Name:** Smart Pantry & Recipe Finder  
**Sprint:** 1 (CLI & OOP Foundation)  
**Date:** September 15, 2026  

---

## 👥 Team Members & Roles

* 🏗️ **Planner / Team Leader (Architect):** ไทน์ (Phattharawadee Songsrirod) — *ออกแบบสถาปัตยกรรม OOP และ Data Flow*
* 🔨 **Coders (Builders):** ฟ่า & ภีม (Sujeephon Poobanchuen & Team) — *เขียนคลาส PantryStore, RecipeManager และประมวลผลระบบ*
* 🐞 **Debugger (Finisher):** โดนัท — *จัดการ Validation, ตรวจสอบการคำนวณวันหมดอายุ และจัดฟอร์แมต Output*

---

## 1. 📌 Sprint Progress Summary

* [x] Defined project scope and Definition of Done (DoD) in `PLAN.md`
* [x] Designed the CLI main application flow and output formatting
* [x] Implemented core architecture using Object-Oriented Programming (OOP) classes: `PantryStore`, `RecipeManager`, and `SmartPantryApp`
* [x] Implemented `PantryStore.add_item()` with item name, quantity, unit, and expiry date (`YYYY-MM-DD`)
* [x] Implemented `PantryStore.get_expiring_items()` calculating 3-day threshold using Python `datetime`
* [x] Implemented `RecipeManager.analyze_recipes()` matching pantry contents against target recipes (identifying matched vs. missing ingredients)
* [x] Implemented automated Shopping List calculation for missing recipe items
* [x] Added input validation for non-numeric quantities, date formats, and empty strings
* [x] Added error handling to prevent runtime crashes
* [x] Conducted comprehensive manual testing on core features and edge cases
* [x] Tested and delivered code via Pull Request on GitHub

---

## 2. 🐞 Quality Assurance & Debugging Report

| Test Item | Input Used | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Add Pantry Item** | Name: `egg`, Qty: `3`, Unit: `ฟอง`, Expiry: `2026-09-16` | Record saved and confirm message printed | `✅ เพิ่มวัตถุดิบ: egg (3 ฟอง) [หมดอายุ: 2026-09-16]` | **PASSED** |
| **Invalid Input Handling** | Qty: `three` or Date: `16-09-2026` | Validation error prompt displayed; no crash | System caught exception and requested valid input | **PASSED** |
| **Expiring Alert** | Expiry date within 3 days (e.g., `2026-09-16`) | List expiring items with remaining quantity | `⚠️ วัตถุดิบที่กำลังจะหมดอายุใน 3 วัน:`<br>`- egg (เหลือ 3.0 ฟอง, หมดอายุ 2026-09-16)` | **PASSED** |
| **Recipe Matching** | Pantry contains `egg`, `pork` | Separate matched and missing ingredients for each recipe | `📌 เมนู: ไข่เจียวหมูสับ (Pork Omelette)`<br>`- วัตถุดิบที่มี: egg, pork`<br>`- วัตถุดิบที่ขาด: ไม่มี (ทำได้เลย!)` | **PASSED** |
| **Shopping List Generation** | Target: "สปาเก็ตตี้คาโบนาร่า (Carbonara)" | Calculate exact quantity needed for missing items | `🛒 Shopping List สำหรับเมนู 'สปาเก็ตตี้คาโบนาร่า (Carbonara)':`<br>`- ซื้อเพิ่ม: spaghetti จำนวน 100`<br>`- ซื้อเพิ่ม: bacon จำนวน 50`<br>`- ซื้อเพิ่ม: cheese จำนวน 30` | **PASSED** |

---

## 3. 💬 Weekly Retrospective (Wow! & Whoops!)

### 🌟 Wow! (What went well)
* Successful separation of concerns using clean OOP architecture (`PantryStore` handling data, `RecipeManager` handling logic, and `SmartPantryApp` driving execution).
* The algorithm accurately compares pantry inventory against recipe requirements, identifying exact missing quantities for the automated **Shopping List**.
* Precise date math implementation using Python's `datetime` module for real-time expiry checking.
* Output formatting is clean, readable, and user-friendly with explicit icons (`✅`, `⚠️`, `🍳`, `🛒`).

### ⚠️ Whoops! (Problems found & Action plan)
1. **Problem:** Data is stored in-memory (`dict`) and resets when the program terminates.  
   * **Fix / Next Step:** SQLite database persistence (`pantry.db`) was scope-managed for Sprint 1 and will be integrated in **Sprint 2**.
2. **Problem:** External API (Spoonacular) is not yet connected; recipes are matched against structured Mock Data.  
   * **Fix / Next Step:** Real API integration via `requests` is scheduled as a primary task for **Sprint 2**.
3. **Problem:** No automated test framework (e.g., `pytest`) was included in Sprint 1.  
   * **Fix / Next Step:** Core functions were verified manually via QA end-to-end testing. Automated unit testing is carried over to **Sprint 2**.

---

## 4. ✅ Definition of Done — Sprint 1 Status

Derived from the project-wide DoD in `PLAN.md`, scoped to Sprint 1 deliverables:

* [x] Core feature works according to requirements (Pantry tracking, Expiry checking, Recipe matching, Shopping list output)
* [x] User input is validated (quantity formatting, date parsing, empty checks)
* [x] Errors are handled gracefully without program crashes
* [x] Code strictly follows modular OOP structure (`PantryStore`, `RecipeManager`, `SmartPantryApp`)
* [ ] **Automated test suite implemented** — *Not met:* Verified via manual QA; `pytest` suite carried over to Sprint 2.
* [x] Interface functions correctly in CLI
* [x] Technical implementation documented via docstrings and `PLAN.md`
* [ ] **Connected to real Spoonacular API** — *Not met:* Mock data used for Sprint 1 prototype; real API carried over to Sprint 2.
* [ ] **Data persisted to SQLite** — *Not met:* In-memory storage used for Sprint 1; SQLite integration carried over to Sprint 2.
* [x] Tested and delivered via Pull Request on GitHub

**Overall Status:** **Sprint 1 Core Delivered (with planned carry-overs)**  
The core OOP structure and business logic run end-to-end successfully. Three items carry over to Sprint 2: (1) Real API integration, (2) SQLite database persistence, and (3) Automated testing suite (`pytest`).
