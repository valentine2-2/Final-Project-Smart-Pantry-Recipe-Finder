# 📄 SPRINT 1 RESULT REPORT

**Project Name:** Smart Pantry & Recipe Finder  
**Sprint:** 1 (CLI & OOP Foundation)  
**Date:** September 15, 2026  

---

## 👥 Team Members & Roles

* 🏗️ **Planner / Team Leader (Architect):** ไทน์ (Phattharawadee) — *วางโครงสร้างระบบและแนวทางการพัฒนา*
* 🔨 **Coders (Builders):** ฟ่า & ภีม — *พัฒนาฟังก์ชันระบบ, OOP Logic และ UI แบบ CLI*
* 🐞 **Debugger (Finisher):** โดนัท — *ตรวจสอบความถูกต้อง (Input Validation) และทดสอบระบบ (QA)*

---

## 1. 📌 Sprint Progress Summary

* [x] Defined project scope and Definition of Done (DoD) in `PLAN.md`
* [x] Designed the CLI menu and main application flow
* [x] Implemented core system using Object-Oriented Programming (OOP) classes: `PantryStore`, `RecipeManager`, and `SmartPantryApp`
* [x] Implemented pantry management (adding items with quantity, unit, and expiry date)
* [x] Implemented expiring items alert (filters items expiring within 3 days)
* [x] Implemented recipe matching logic based on available ingredients (identifying matched vs. missing ingredients)
* [x] Implemented automated Shopping List calculation for missing ingredients
* [x] Added input validation for empty input, non-numeric values, and invalid date formats
* [x] Added error handling for invalid command input to prevent application crashes
* [x] Performed comprehensive manual testing for core functionality and edge cases
* [x] Tested and delivered code via Pull Request on GitHub

---

## 2. 🐞 Quality Assurance & Debugging Report

| Test Item | Input Used | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **CLI Menu Navigation** | Command: `view`, `ADD`, ` quit ` | Handles case-insensitivity and whitespace; routes correctly | Options rendered and executed properly without errors | **PASSED** |
| **Add Pantry Item** | Name: `egg`, Qty: `3`, Unit: `ฟอง`, Expiry: `2026-09-16` | Item saved into pantry data store | Item stored correctly in memory with formatted output | **PASSED** |
| **Invalid Input Handling** | Qty: `three` or Date: `16-09-2026` | Validation error message displayed; no crash | Showed error prompt and asked user to re-enter valid data | **PASSED** |
| **Expiring Items Alert** | Trigger `check_expiring_items` (3-day threshold) | Lists items expiring within 3 days | Displayed `egg` expiring in 2 days correctly | **PASSED** |
| **Recipe Matching** | Pantry contains `egg`, `pork` | Shows matching recipes and missing ingredients | Correctly identified "Pork Omelette" as ready, and listed missing items for "Carbonara" | **PASSED** |
| **Shopping List Generation** | Select target recipe: "Carbonara" | Calculates difference and generates itemized shopping list | Displayed missing items (`spaghetti`, `bacon`, `cheese`) with exact required quantities | **PASSED** |

---

## 3. 💬 Weekly Retrospective (Wow! & Whoops!)

### 🌟 Wow! (What went well)
* Implemented a clean, user-friendly CLI interface with complete navigation flow.
* Structured the codebase using solid OOP principles (`PantryStore`, `RecipeManager`, `SmartPantryApp`), keeping data persistence, business logic, and UI separate.
* Successfully implemented core smart features (expiry alerts, recipe matching, missing ingredients calculation, and shopping list generation).
* Strong collaboration on input validation—prevented runtime crashes caused by invalid dates, non-numeric inputs, or unexpected characters.

### ⚠️ Whoops! (Problems found & Action plan)
1. **Problem:** Data is currently kept in-memory (`dict` structure) and resets when the program restarts.  
   * **Fix / Next Step:** SQLite database integration was intentionally scope-managed and is scheduled for **Sprint 2** as outlined in `PLAN.md`.
2. **Problem:** Spoonacular API integration was not completed in Sprint 1.  
   * **Fix / Next Step:** Used structured Mock Recipe Data to keep progress moving on CLI interaction, OOP structure, and matching logic. Real API integration is prioritized as the first task of **Sprint 2**.
3. **Problem:** No automated test suite (e.g., `pytest`) exists yet; verification was completed via manual testing.  
   * **Fix / Next Step:** Manual QA confirmed core feature stability. Writing an automated test suite has been carried over to **Sprint 2**.

---

## 4. ✅ Definition of Done — Sprint 1 Status

Derived from the project-wide DoD in `PLAN.md`, scoped to Sprint 1 deliverables:

* [x] Feature works according to its requirements (CLI navigation, pantry management, expiry alert, recipe matching, shopping list generation)
* [x] User input is validated (non-numeric quantities, date formats, empty inputs)
* [x] Errors are handled appropriately (invalid inputs trigger helpful prompts without crashing the app)
* [x] Code follows the project's modular/OOP structure (`PantryStore`, `RecipeManager`, `SmartPantryApp`)
* [ ] **Automated tests implemented for core functionality** — *Not met:* Verified via manual QA; automated test suite (`pytest`) carried over to Sprint 2.
* [x] Feature works through the intended interface (CLI)
* [x] Implementation is documented in `PLAN.md` and inline Docstrings
* [ ] **Connected to real Spoonacular API** — *Not met:* Mock recipe data used for Sprint 1; real API connection carried over to Sprint 2.
* [ ] **Data persisted to SQLite** — *Not met:* Data is currently held in-memory; SQLite persistence carried over to Sprint 2.
* [x] Tested and delivered via Pull Request on GitHub

**Overall Status:** **Sprint 1 Core Delivered (with planned carry-overs)**  
The core CLI interface, OOP architecture, and business logic run end-to-end. Three items carry over to Sprint 2: (1) Real API integration, (2) SQLite database persistence, and (3) Automated testing suite.
