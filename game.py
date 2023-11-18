from player import Player
from collections import OrderedDict
#import world
import worldmap
import string
import action


def play():
    print("Lab Madness")
    Welt, Karte = worldmap.createworld()
    player = Player()
    print(Welt[player.location].name)
    print(Welt[player.location].description)
    #vis = worldmap.visibleworld(Karte,Welt,player.location) #visible world available to interact with for the player
    while True:
        action_input = action.get_player_command()
        vis = worldmap.visibleworld(Karte,Welt,player.location) #visible world available to interact with for the player

        action.player_action(action_input,vis,Karte,Welt,player)

        
        #a few extra actions for gameplay ease
        if action_input in ["Aktion", "Aktionen", "A", "a"]:
            print("Unter den möglichen Eingaben: benutze, schau an, nimm, gib, öffne, schließe, tritt ein, t, Inventar, i, Aktion, Aktionen, A, a, wo bin ich")
        if action_input in ["Inventar", "i"]:
            player.print_inventory()

        elif action_input in ["wo bin ich", "wo bin ich?"]:
            print(Welt[player.location].name)
            print(Welt[player.location].description)
            Karte.print_map()

play()
