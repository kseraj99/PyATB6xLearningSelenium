# Selenium 4.x with Python – Automation Notes

Author: Seraj

---

# 📌 Overview

This repository is a **hands-on learning and reference project** for **Web Automation using Selenium 4.x with Python**.
It is based on structured notes, practical examples, and assignments covering **Selenium fundamentals to advanced concepts**, including waits, locators, actions, Selenium Grid, Docker, PyTest, and Allure reporting.

The goal of this repository is to:

* Learn Selenium concepts step by step
* Practice real-world automation scenarios
* Build a strong foundation for **SDET / Automation Tester roles**
* Maintain reusable, well-structured automation code

---

# 🛠️ Tech Stack

* **Language:** Python 3.x
* **Automation Tool:** Selenium 4.x
* **Test Framework:** PyTest
* **Reporting:** Allure Reports
* **IDE:** PyCharm / VS Code
* **Version Control:** Git & GitHub
* **Optional:** Docker, Selenium Grid

---

# 📂 Repository Structure

```
selenium-python-automation/
│
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── pytest.ini                 # PyTest configuration (logging, markers)
├── .gitignore                 # Ignored files & folders
│
├── src/
│   ├── ex_01_selenium_basic/  # Selenium basics & first scripts
│   ├── ex_02_locators/        # ID, Name, Class, CSS, XPath examples
│   ├── ex_03_waits/           # Implicit, Explicit, Fluent waits
│   ├── ex_04_navigation/      # Browser navigation commands
│   ├── ex_05_actions/         # Keyboard & mouse actions
│   ├── ex_06_alerts/          # JS alerts handling
│   ├── ex_07_frames_windows/  # iFrames & window handling
│   ├── ex_08_webtables/       # Static & dynamic web tables
│   ├── ex_09_file_upload/     # File upload examples
│   ├── ex_10_grid_remote/     # Selenium Grid & Remote WebDriver
│
├── tests/
│   ├── test_vwo_login_valid.py      # Valid login test cases
│   ├── test_vwo_login_invalid.py    # Invalid login & error validation
│
├── utils/
│   ├── driver_factory.py      # Browser initialization logic
│   ├── logger.py              # Centralized logging setup
│
├── reports/
│   └── allure-results/        # Allure raw results
│
└── docs/
    └── selenium_notes.pdf     # Reference notes used in this project
```

---

# ⚙️ Setup Instructions

# 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/selenium-python-automation.git
cd selenium-python-automation
```

# 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

# 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How to Run Tests

# Run All Tests

```bash
pytest
```

# Run a Specific Test File

```bash
pytest tests/test_vwo_login_valid.py
```

# Run with Allure Results

```bash
pytest --alluredir=reports/allure-results
```

# Generate Allure Report

```bash
allure serve reports/allure-results
```

---

# 📊 Reporting (Allure)

Allure provides:

* Step-wise execution details
* Test status (Pass / Fail / Skip)
* Logs and screenshots (if enabled)

This repository is configured to generate **Allure-compatible results** for every test execution.

---

# 🧪 Covered Concepts

✔ Selenium Architecture (Selenium 4 – W3C)
✔ WebDriver & Browser Drivers
✔ Locators (ID, Name, Class, CSS, XPath – Advanced)
✔ XPath Functions & Axes
✔ CSS Selectors (Advanced)
✔ Waits (Implicit, Explicit, Fluent)
✔ Actions Class (Keyboard & Mouse)
✔ Alerts, Frames, Windows
✔ Web Tables (Static & Dynamic)
✔ File Upload & Downloads
✔ Selenium Grid & Remote WebDriver
✔ Docker + Selenium (Optional)
✔ PyTest Framework & Logging
✔ Allure Reporting

---

# 🧠 Assignments Implemented

* VWO Login Automation (Valid & Invalid)
* Error Message Validation
* Heatmap Page Automation (Actions + iFrame + Window Handling)
* Dynamic Web Table Validation

---

# 🚀 Future Enhancements

* Page Object Model (POM)
* Data-driven testing
* CI/CD integration (GitHub Actions)
* Cross-browser execution
* Screenshot & video recording

---

# 👤 Author

Seraj
Automation Testing Enthusiast | Selenium | Python | PyTest

---

## ⭐ Support

If you find this repository useful, please give it a ⭐ on GitHub.

Happy Testing! 🚀

""
Key Points to remember:-
## **XPath Functions **


- **Known Attribute** - //*[@id='btn-make-appointment']
- **TAG Name** - //a[@id='btn-make-appointment']


**Text Matching**

1. Full Visible Text. 
    1.  -> text()  -> `//a[text()='Make Appointment']` 
    2. `//a[normalize-space()='Make Appointment']` 

2. Partial Text -
    1.  contain() -> `//a[contains(text(),'Make')]` 
    2. `//a[starts-with(text(),'Make')]` 
    3. `//a[ends-with(text(),'Make')]` 

""
