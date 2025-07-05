Django>=4.0
# 🏪 Ghala Core Systems Simulation - Django Project

A simplified system simulating merchant payment configurations and order processing built with Django and Bootstrap 5.

# Ghala Intern Challenge – Core Systems Simulation

This project is a full-stack web application that simulates **merchant payment configuration** and **order processing**, built as part of the **Ghala Technical Intern Challenge**.

---

## 🚀 Features

* 🧞 Merchant onboarding
* 💳 Payment method configuration (e.g. Mobile, Card, Online)
* 📦 Order placement linked to payment method
* 📊 Grouped merchant display
* 🧠 Clean and intuitive UI (Django + Bootstrap)

---

## ⚙️ Requirements

* Python 3.8+
* Django 4.x+
* SQLite (default)

---

## 💠 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/kijumbejames/ghala-system.git
cd ghala-system
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Apply migrations**

```bash
python manage.py migrate
```

4. **(Optional) Load sample data**

```bash
python manage.py loaddata sample_merchants.json
```

5. **Run development server**

```bash
python manage.py runserver
```

6. **Access the app**

Go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Admin Login (optional)

To create a superuser:

```bash
python manage.py createsuperuser
```

Login at: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🧪 Sample Usage

Once the server is running:

* Visit `/` to see homepage
* Navigate to `/merchants/` to view grouped merchants
* Add new merchant via admin or form
* Orders can be placed via `/orders/`

---

## 📁 Project Structure

```
ghala_intern/
│
├── core/              # Main app: models, views, forms
├── templates/         # All HTML pages
├── static/            # CSS, JS, images
├── db.sqlite3         # Default database
├── manage.py
└── requirements.txt
```

---

## 👨‍💻 Author

> **Kijumbe James**
> Ghala Intern Challenge Submission
> [GitHub](https://github.com/kijumbejames)

---

## 📌 Notes

* The app is ready for testing and extension.
* SQLite is used by default and requires no configuration.

