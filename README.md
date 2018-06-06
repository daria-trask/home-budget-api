# home-budget-api



##Setting Up Locally

1. Download the repo. And get to it`s folder in terminal
2. Set virtual environment for required packages:

```bash
    python virtualenv env
    source env/bin/activate
```
3. Install required packages
```bash
    pip install -r requirements.txt
```
4. Run local server on port 8000
```bash
    python manage.py runserver
```

P.S. You definitely need to run python manage.py migrate first time to apply migrations
