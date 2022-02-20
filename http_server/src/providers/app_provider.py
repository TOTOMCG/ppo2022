from flask import Flask
from config import CFG
from flask_sqlalchemy import SQLAlchemy

app_provider = Flask("HTTP server")
app_provider.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{CFG['database']['path']}"
db = SQLAlchemy(app_provider)
