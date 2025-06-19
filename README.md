# Project Title
**Django Learning**

## Project Description
A small project to practice Django. It includes:

- Django setup
- Two APIs: one for user signup and another for login
- A Celery background task to send a welcome email after signup
- A Telegram bot to register users

## Features
- ✅ User signup & login with Django REST Framework
- 🤖 Telegram bot integration
- 📧 Welcome email after registration using Celery

## Setup Instructions
1. Create and activate virtual environment
2. Install requirements using `pip install -r requirements.txt`
3. Start Redis server (ensure Redis is installed and running)
4. Run Django development server
5. Start Celery worker

## How to Run
```bash
python manage.py runserver
celery -A backend worker --loglevel=info

# API Endpoints
* POST-/api/signup/	 for  user register
* POST-/api/login/	for Login user
* GET-/api/hello/ for Hello test
* GET-/api/protected/ for JWT authentication
# Tech Stack
* Django
* Django REST Framework
* Celery
* Redis
* Telegram Bot

