def player_stats(playerObj, score=False):
    print("Health: " + str(playerObj.health) + "%")
    print("Strength: " + str(playerObj.strength) + "%")
    print("Hunger: " + str(playerObj.food) + "%")
    if score:
        print("Score: " + str(score))
