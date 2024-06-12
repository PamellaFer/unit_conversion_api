from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Unidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    para_unidade_base = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
