import validation
import prettyprint

def print_stats(playerObj):
    playerValid = validation.Player()
    playerValid.validate(playerObj)
    prettyprint.player_stats(playerObj)

def check_dead(playerObj):
    playerValid = validation.Player()
    playerValid.validate(playerObj)
    if playerObj.health == 0:
        return True
    else:
        return False
