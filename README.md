# NexusStore 🛒

A fully functional e-commerce web app built with Django. Product listings, cart management, order processing, user auth — the works.

## Features

- User registration & login (Django's native auth)
- Product listings with a dedicated detail page
- Session-based shopping cart
- Order processing with full order history per user
- SQLite database storing products, users, and orders

## Tech Stack

- **Backend**: Python, Django 5.x
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite3

## Getting Started

```bash
git clone <your-repo-url>
cd CodeAlpha_E-commerce_Store
```

Activate your virtual environment, then:

```bash
pip install -r requirements.txt
python manage.py migrate
python seed.py        # optional — seeds the DB with sample products
python manage.py runserver
```

Hit `http://127.0.0.1:8000/` and you're good.

## Requirements Checklist

- [x] Product listings & detail page
- [x] Shopping cart
- [x] Order processing
- [x] User registration/login
- [x] Database for products, users, and orders
- [x] Frontend: HTML, CSS, JavaScript
- [x] Backend: Django (Python)

---

*Built for the CodeAlpha Internship Program.*
