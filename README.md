
python -m venv venv
source venv/Scripts/activate  # Windows (Git Bash)
pip install -r requirements.txt
flask db init
flask db migrate -m "initial migration"
flask db upgrade
flask run
