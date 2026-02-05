# Snake Game - Django Web Application

A classic Snake game built with Django and HTML5 Canvas. Control the snake, eat food, and avoid hitting walls or yourself!

## Overview

This project is a simple *Snake Game* developed using *Python and Django* for learning and practice purposes. The game runs in a web browser and demonstrates how Django can be used to serve a game interface while the core game logic is handled on the frontend using *HTML, CSS, and JavaScript*.

The objective of the game is to control the snake using the keyboard arrow keys, eat food to increase the snake's length and score, and avoid collisions with the walls or the snake's own body.

## Prerequisites

Before running this project, make sure you have the following installed:
- **Python 3.8 or higher**
- **pip** (Python package manager)

## Installation & Setup

### 1. Navigate to the Project Directory

```bash
cd /Users/hamzaiqbal/Desktop/projects/snakegame
```

### 2. Create a Virtual Environment (Recommended)

Create and activate a virtual environment to isolate project dependencies:

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Django

Install Django using pip:
```bash
pip install django
```

### 4. Configure Django Settings

⚠️ **Important:** This project references `sankegame.settings` in manage.py, but the settings file might be missing. You have two options:

**Option A: Create the settings module (Recommended for proper Django setup)**

Create the settings directory and file:
```bash
mkdir -p sankegame
touch sankegame/__init__.py
```

Then create `sankegame/settings.py` with the following basic configuration:

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-your-secret-key-here'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'snakegame',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'snakegame.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

Also create `sankegame/urls.py`:
```python
from django.urls import path, include

urlpatterns = [
    path('', include('snakegame.urls')),
]
```

**Option B: Quick fix (Simpler but less organized)**

You can also modify the project to work without the separate settings module, though Option A is recommended for proper Django structure.

### 5. Create Template Directory

Move the snake.html file to the proper template location:
```bash
mkdir -p snakegame/templates/snakegame
mv snake.html snakegame/templates/snakegame/
```

Or update views.py to point to the correct template location.

### 6. Run Database Migrations

Initialize the database:
```bash
python manage.py migrate
```

## Running the Application

### Start the Development Server

Run the Django development server:
```bash
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Access the Game

Open your web browser and navigate to:
```
http://127.0.0.1:8000/
```

Or:
```
http://localhost:8000/
```

## How to Play

1. Click the **"▶ Start Game"** button to begin
2. Use the arrow buttons on screen OR keyboard arrow keys to control the snake:
   - ⬆ Up Arrow - Move Up
   - ⬇ Down Arrow - Move Down
   - ⬅ Left Arrow - Move Left
   - ➡ Right Arrow - Move Right
3. Eat the red food to grow and increase your score
4. Avoid hitting the walls or your own tail!
5. Game ends when you collide with a wall or yourself

## Project Structure

```
snakegame/
├── manage.py              # Django management script
├── views.py               # View function to render the game
├── urls.py                # URL routing for the app
├── snake.html             # Game interface with HTML5 Canvas
├── apps.py                # App configuration
├── models.py              # Database models
├── admin.py               # Admin configuration
├── tests.py               # Unit tests
├── db.sqlite3             # SQLite database
├── README.md              # This file
└── sankegame/             # Main project directory (may need to create)
    ├── __init__.py
    ├── settings.py        # Django settings
    └── urls.py            # Main URL configuration
```

## Technologies Used

### Backend (Django)
Django is responsible for managing the project structure, handling URL routing, and rendering templates. It serves the frontend files to the browser while the game logic remains on the client side.

### Frontend (HTML, CSS, JavaScript)
The frontend consists of a single HTML page where the game canvas is displayed:
- **HTML** - Structure of the game interface  
- **CSS** - Basic styling and layout
- **JavaScript** - Snake movement, collision detection, food generation, score updates, and game logic

## Troubleshooting

### Django Not Found
If you get an error about Django not being installed:
```bash
pip install django
```

### Settings Module Error
If you get `ModuleNotFoundError: No module named 'sankegame.settings'`:
- Follow **Step 4** above to create the settings module
- Make sure the `sankegame` directory exists with `__init__.py` and `settings.py`

### Template Not Found
If you get a template error:
- Make sure `snake.html` is in the correct location: `snakegame/templates/snakegame/snake.html`
- Or update the template path in views.py

### Port Already in Use
If port 8000 is already in use, run the server on a different port:
```bash
python manage.py runserver 8080
```
Then access at `http://127.0.0.1:8080/`

### Permission Errors
Make sure you have write permissions in the project directory. If using a virtual environment, make sure it's activated.

## Learning Outcomes

This project is intended for beginners who want to understand how Python and Django integrate with frontend technologies. It helps in learning:
- Django project structure and configuration
- URL routing and view functions
- Template rendering
- Integrating JavaScript-based game logic within a Django application
- Canvas API for game development

## Future Enhancements

The project can be extended with additional features such as:
- Difficulty levels (speed adjustment)
- Restart and pause functionality
- High score saving to database
- Animations and sound effects
- Multiplayer support
- Mobile-friendly touch controls
- Leaderboard system

## License

This is a simple educational project. Feel free to modify and use as needed.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!
