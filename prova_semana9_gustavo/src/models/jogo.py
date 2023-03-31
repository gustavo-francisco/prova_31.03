from src.models.base import Base
from sqlalchemy import Column, Integer, Float, String

class Jogo(Base):
    __tablename__ = "Jogo"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    plataforma = Column(String)
    preco = Column(Float)
    quantidade = Column(Integer)


    def __repr__(self):
        return f"Jogo(id={self.id!r}, nome={self.nome!r}, plataforma={self.plataforma!r}, preco={self.preco!r}, quantidade={self.quantidade!r})"