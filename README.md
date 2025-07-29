# 📝 Django Blog API

A simple and clean RESTful Blog API built with **Django REST Framework** and **JWT Authentication**. It lets users register, log in, and manage blogs and comments — all protected with secure tokens.

---

## 🚀 Main Features (in simple terms)

- 🧑‍💻 **User Signup & Login**  
  Users can create accounts and log in with secure passwords and JWT tokens.

- 🔐 **Secure Endpoints**  
  Only logged-in users (via tokens) can create, edit, or delete blogs/comments.

- ✍️ **Blogs CRUD**  
  Create, view, update, delete blogs — but only your own blogs!

- 💬 **Comments System**  
  Add comments to any blog. Edit or delete your own comments only.

- 🔍 **Search & Pagination**  
  Easily search blogs by title, and browse through pages of results.

---

## 📂 API Endpoints

Here’s a quick reference of all available endpoints:

### 🔑 Authentication

| Method | Endpoint             | Description                  |
|--------|----------------------|------------------------------|
| POST   | `/create-user/`      | Register a new user          |
| POST   | `/login-user/`       | Login and get JWT token      |
| POST   | `/token/refresh/`    | Refresh access token         |

### 🖋 Blog Management

| Method | Endpoint                         | Description                     |
|--------|----------------------------------|---------------------------------|
| POST   | `/create-blog/`                  | Create a new blog               |
| GET    | `/view-blogs/`                   | View all blogs (paginated)      |
| GET    | `/view-blogs-by-user/`           | View blogs by the logged-in user|
| GET    | `/search-blogs/?title=xyz`       | Search blogs by title           |
| PATCH  | `/update-blog/<id>/`             | Update your blog                |
| DELETE | `/delete-blog/<id>/`             | Delete your blog                |

### 💬 Comment Management

| Method | Endpoint                                | Description                       |
|--------|-----------------------------------------|-----------------------------------|
| POST   | `/create-comment/`                      | Add a comment to a blog           |
| GET    | `/view-comments-on-blog/<blog_id>/`     | View comments on a specific blog  |
| PATCH  | `/update-comment/<id>/`                 | Update your comment               |
| DELETE | `/delete-comment/<id>/`                 | Delete your comment               |

---

## ⚙️ Tech Stack

- **Python 3.10+**
- **Django 4.x**
- **Django REST Framework**
- **SimpleJWT (for authentication)**
- **SQLite (default dev DB)**

---
## 🔧 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/alibassam24/Blog-App-Backend-Django.git
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