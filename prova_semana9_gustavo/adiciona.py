from src.models.jogo import Jogo
from main import session

lista = []

def adiciona():
    jogo_DSR = Jogo(nome="DEAD SPACE REMAKE", plataforma="PS5", preco=350, quantidade=10)
    jogo_F = Jogo(nome="FORSPOKEN", plataforma="PC", preco=299, quantidade=8)
    jogo_DI = Jogo(nome="DEAD ISLAND 2", plataforma="PS5", preco=350, quantidade=10)
    jogo_H = Jogo(nome="HOGWARTS LEGACY", plataforma="PC", preco=219, quantidade=7)
    jogo_W = Jogo(nome="WILD HEARTS", plataforma="Xbox Series", preco=350, quantidade=7)
    jogo_R = Jogo(nome="RESIDENT EVIL 4", plataforma="PS5", preco=289, quantidade=10)
    jogo_L = Jogo(nome="THE LEGEND OF ZELDA: TEARS OF THE KINGDOM", plataforma="Switch", preco=350, quantidade=10)
    lista.append(jogo_DSR)
    lista.append(jogo_F)
    lista.append(jogo_DI)
    lista.append(jogo_H)
    lista.append(jogo_W)
    lista.append(jogo_R)
    lista.append(jogo_L)
    return lista

session.add_all(adiciona())
session.commit()