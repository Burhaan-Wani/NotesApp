echo "BUILD START"
python3.9  pip install sqlite3
python3.9 -m pip install -r requirements.txt
python3.9 manage.py migrate
python3.9 manage.py collectstatic --noinput --clear

echo "Build end"