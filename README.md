# 🎓 KTU Grade Analyzer

A Django-based web application to calculate the **minimum external marks required to pass or achieve a target grade**, based on your internal marks.

---

## 💡 About the Project

This project is built to help KTU students understand **how much they need to score in the external exam** to pass or reach a desired grade.

Instead of guessing or doing manual calculations, you can simply enter your internal marks and get the required external marks instantly.

---

## 🚀 Features

* Calculate **required external marks** for passing or target grade
* Works based on your **internal marks**
* Includes curriculum data for:

  * 2019 Scheme (CSE, ECE, EEE)
  * 2024 Scheme (CSE – Semester 3 to 8)
  * Supports electives (PEC & OEC)

---

## ⚠️ Note on Electives

Elective subject names are not included in the system because they vary across colleges.
Instead, generic elective options are used to keep the system flexible.

---

## 🛠 Tech Stack

* Python
* Django
* SQLite
* HTML / CSS

---

## ⚙️ How to Run

```bash
git clone https://github.com/Anna-Jaison/Ktu_Grade_Analyzer.git
cd Ktu_Grade_Analyzer
pip install -r requirements.txt
python manage.py runserver
```

Then open:
http://127.0.0.1:8000/

---

## Why I Built This

I originally started this out of curiosity (and a bit of boredom 😅), but it turned into something actually useful.

As a student, I often wanted a quick way to estimate how much I needed to score in externals based on internals, so I built this tool to make that process simple.

---

## 🔧 Future Improvements

* PDF result upload and auto extraction
* Add more departments and schemes
* Improve UI/UX
* Deploy as a live web app

---

## 👩‍💻 Author

Anna Jaison
