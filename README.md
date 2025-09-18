<h1 align="center">🍋 Little Lemon - Django Restaurant Project</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Django-5.x-green?logo=django&logoColor=white" alt="Django Badge"/>
  <img src="https://img.shields.io/badge/HTML-5-orange?logo=html5&logoColor=white" alt="HTML Badge"/>
  <img src="https://img.shields.io/badge/CSS-3-blue?logo=css3&logoColor=white" alt="CSS Badge"/>
  <img src="https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite&logoColor=white" alt="SQLite Badge"/>
</p>

---

## Overview

**Little Lemon** is a demonstration web application built with **Django**, showcasing the creation of a simple restaurant website.  
It covers **basic CRUD operations**, working with **models, views, and templates**, and demonstrates the use of **media files, static assets, and forms**.  
This project is intended as a learning and portfolio exercise for web development with **Python/Django** and **basic front-end tools** (HTML, CSS).


---

## Features

- **Menu Management**  
  Display menu items with name, description, price, and image. Each menu item can be clicked to view a detailed page.

- **Reservation System**  
  Users can submit reservations through a form that captures first name, last name, guest number, and comments.  

- **Admin Panel Integration**  
  - Superusers can add, edit, and delete **menu items** and **reservations**.
  - Fully demonstrates **Django's built-in admin functionality**.

- **Media & Static Files Handling**  
  - Images for menu items stored in a **media folder**.
  - CSS, favicon, and other static assets managed with Django's **static files system**.

---

## Technologies Used

- **Backend**: Python 3.x, Django 5.x
- **Database**: SQLite (default Django DB for simplicity)
- **Frontend**: HTML, CSS, basic templating with Django Template Language (DTL)
- **Libraries**:
  - Pillow (for `ImageField` support in menu images)
- **Development Tools**:
  - VSCode (with integrated terminal)
  - Git & GitHub for version control

---

## Project Structure
```
littlelemon/
├─ littlelemon/ # Main project folder
│ ├─ settings.py # Django project settings
│ ├─ urls.py # Root URL configurations
│ ├─ wsgi.py / asgi.py # WSGI/ASGI entry points
├─ restaurant/ # Application folder
│ ├─ models.py # Booking and Menu models
│ ├─ views.py # Views for pages and menu item detail
│ ├─ forms.py # ReservationForm
│ ├─ admin.py # Admin registration for models
│ ├─ templates/ # HTML templates
│ ├─ static/ # CSS, images, favicon
|
├─ media/ # Uploaded images (menu items)
|
├─ manage.py # Django management script
```
---

## Installation and Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/littlelemon.git
   cd littlelemon
   ```

2. **Create and activate a virtual environment**
   ```
   python -m venv venv
    source venv/bin/activate      # Linux/Mac
    venv\Scripts\activate         # Windows
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   pip install Pillow    
   ```

4. **Apply migrations**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```
    python manage.py createsuperuser
   ```

6. **Run the development server**
   ```
    python manage.py runserver
   ```

7. **Access the application**

- Home: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/
