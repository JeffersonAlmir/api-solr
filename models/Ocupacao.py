from sqlalchemy import Integer, String
from sqlalchemy.orm import  Mapped, mapped_column

from database import db

class Ocupacao(db.Model):
    __tablename__ = "tb_ocupacao"

    codigo: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(200))


    def __init__(self, codigo:int, titulo:str):
        self.codigo = codigo
        self.titulo = titulo
        