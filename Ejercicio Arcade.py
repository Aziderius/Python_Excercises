import random

def competencia(a):
    items = list(range(5))
    limit = 3
    partida = 0
    final_score = list()

    for score in items:
        rng = random.randint(5000, 1000000)
        print(rng)
        final_score.append(rng)
        partida += 1
        if partida == limit:
            break
    print("Maximum Score: ", sum(final_score))

jugador1 = competencia