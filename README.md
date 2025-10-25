# redirect (Django project) with core app

Project name: `redirect`  
App name: `core`

This project demonstrates middleware that detects requests from Googlebot (by User-Agent)
and redirects requests to the home endpoint (`/`) to `/about/` when the User-Agent contains `Googlebot`.

## Quick start

1. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # on Windows use: .venv\Scripts\activate
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations and start server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. Visit http://127.0.0.1:8000/ as a normal user (you'll see Home).
   To simulate Googlebot, send a request with User-Agent containing "Googlebot" (it will be redirected to /about/).

Note: For production, replace SECRET_KEY in settings.py with a secure value and set ALLOWED_HOSTS appropriately.
