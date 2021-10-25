export FLASK_APP=racer_portfolio
## development
export FLASK_ENV=development

## production
# export FLASK_ENV=production
# export DB_USER=[]
# export DB_PASSWORD=[]
# # python -c "import os; print(os.urandom(16))"
# export SECRET_KEY=[]

flask db init
flask db migrate
flask db upgrade
# flask db downgrade