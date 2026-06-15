# KTH Clinic

A Django web application for a clinic website built in the `kth_clinic` workspace.

## Project Structure

- `manage.py` — Django management script.
- `db.sqlite3` — SQLite database file.
- `kth_clinic/` — Django project configuration.
- `kth/` — main Django app with models, views, templates, static files, and urls.
- `templates/` — project-level HTML templates.
- `kth/static/` — static assets including CSS and images.

## Features

- Clinic website pages: home, doctors, departments, doctor detail, contact, about, login.
- Uses Django templates and static files.
- Includes Tailwind support via `tailwind` in `INSTALLED_APPS`.

## Requirements

- Python 3.11+ (or compatible version)
- Django 5.x
- Optional: `django-tailwind` if you are using the Tailwind integration in this project.

## Setup

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install django django-tailwind
```

3. Apply database migrations:

```powershell
python manage.py migrate
```

4. Create a superuser (optional):

```powershell
python manage.py createsuperuser
```

5. Run the development server:

```powershell
python manage.py runserver
```

6. Open the site in your browser:

```text
http://127.0.0.1:8000/
```

## Notes

- The project uses SQLite by default (`db.sqlite3`).
- Debug mode is enabled in `kth_clinic/settings.py`.
- Static files are served from `kth/static`.

## Useful Commands

- `python manage.py runserver` — start the development server.
- `python manage.py makemigrations` — create new migrations.
- `python manage.py migrate` — apply migrations.
- `python manage.py createsuperuser` — create an admin user.
- `python manage.py collectstatic` — collect static files for deployment.

---

Enjoy working on the KTH Clinic Django project!
