
Win = input("Coloque suas vitorias \n")

lose = input("Coloque suas derrotas \n")

games = int(Win) + int(lose)

print("Você jogou " + str(games) + " jogos!")

print("Você ganhou " + Win + " jogos!")

print("Você perdeu " + lose + " jogos!")

porcenVIT = (int(Win) / int(games)) * 100

print("Você venceu " + str(porcenVIT) + " dos jogos!")

