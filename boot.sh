export FLASK_APP=run.py
export FLASK_ENV=development
pip freeze > requirements.txt
python run.py
