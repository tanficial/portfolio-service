import os

BASE_DIR = os.path.dirname(__file__)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'portfolio.db'))
SECRET_KEY = "dev"

if os.environ.get("FLASK_ENV") == "production":
    USER = os.environ.get("DB_USER")
    PASSWORD = os.environ.get("DB_PASSWORD")
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@localhost/racer_portfolio?charset=utf8mb4'
    SECRET_KEY = os.environ.get("SECRET_KEY")
