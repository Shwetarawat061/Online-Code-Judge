from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from config import Config

# Initialize extensions globally
db = SQLAlchemy()
login_manager = LoginManager()
jwt = JWTManager()
socketio = SocketIO(cors_allowed_origins="*") # Adjust in production

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with app context
    db.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)
    socketio.init_app(app)

    # Register Blueprints
    from app.api.auth import auth_bp
    from app.api.clusters import clusters_bp
    from app.sockets.metrics import metrics_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(clusters_bp, url_prefix='/api/clusters')

    return app
