
1. python -m venv venv
2. source venv/Scripts/activate  # Windows (Git Bash)
3. pip install -r requirements.txt
4. flask db init
5. flask db migrate -m "initial migration"
6. flask db upgrade
7. flask run
