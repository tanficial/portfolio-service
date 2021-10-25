export FLASK_APP=racer_portfolio
export FLASK_ENV=production
export DB_USER=[]
export DB_PASSWORD=[]
# python -c "import os; print(os.urandom(16))"
export SECRET_KEY=[]

# nohup flask run -h 0.0.0.0 -p 5000 &
nohup uwsgi --socket 0.0.0.0:5000 --protocol=http -w racer_portfolio --master --processes=4 --threads=4 &