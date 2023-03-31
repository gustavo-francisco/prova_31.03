from main import session
from src.models.jogo import Jogo

Jogos = session.query(Jogo).all()

print(Jogos)