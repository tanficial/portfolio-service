from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from racer_portfolio import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    app.config.from_object(config)
    db.init_app(app)
    Migrate().init_app(app, db)
    app.config["PERMANENT_SESSION_LIFETIME"] = 3600

    from racer_portfolio.apis import auth_api
    from racer_portfolio.apis import user_api
    from racer_portfolio.apis import portfolio_api
    from racer_portfolio.apis import award_api
    from racer_portfolio.apis import education_api
    from racer_portfolio.apis import license_api
    from racer_portfolio.apis import project_api
    app.register_blueprint(auth_api.bp, url_prefix="/api/auth")
    app.register_blueprint(user_api.bp, url_prefix="/api/user")
    app.register_blueprint(portfolio_api.bp, url_prefix="/api/portfolio")
    app.register_blueprint(award_api.bp, url_prefix="/api/award")
    app.register_blueprint(education_api.bp, url_prefix="/api/education")
    app.register_blueprint(license_api.bp, url_prefix="/api/license")
    app.register_blueprint(project_api.bp, url_prefix="/api/project")

    @app.route("/api")
    def landing():
        return "Hello portFolio"

    return app

application = create_app()

if __name__ == "__main__":
    application.run()
