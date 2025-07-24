# 📝 Django Blog API

A minimal RESTful Blog API built with **Django REST Framework** and **JWT Authentication**. Users can register, login, and perform CRUD operations on blog posts.

---

## 🚀 Features

- ✅ User registration with password hashing  
- ✅ JWT login (access + refresh tokens)  
- ✅ Create / Read / Update / Delete blog posts  
- ✅ Blog search with partial title match  
- ✅ Pagination (PageNumberPagination)  
- ✅ Field validation via serializers  
- ✅ Protected routes with JWT auth  

---

## ⚙️ Tech Stack

- Django 4.x  
- Django REST Framework  
- SimpleJWT  
- Python 3.10+ 
- sqlite

---

## 🔧 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/django-blog-api.git
cd django-blog-api

# Create virtual environment
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## 🙋‍♂️ Author
Ali Bassam
📧 alibassam063@gmail.com
🔗 https:www.linkedin.com/in/alibassam1