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
        
        if action_input in ["benutze","schau an", "nimm", "gib", "öffne", "schließe", "tritt ein","t", "Inventar", "i", "Aktion", "Aktionen", "A", "a","wo bin ich"]:
            if action_input in ["Aktion", "Aktionen", "A", "a"]:
                print("Mögliche Eingaben: "+str(get_available_actions()))
            if action_input in ["Inventar", "i"]:
                player.print_inventory()

            if action_input in ["tritt ein","t"]:
                player.walk(Welt["Flur"])

            elif action_input in ["öffne"]:
                Welt["FlurBuero"].open()
                Karte.update_door_status(Welt["FlurBuero"])

            elif action_input in ["schließe"]:
                Welt["FlurBuero"].close()
                Karte.update_door_status(Welt["FlurBuero"])

            elif action_input in ["wo bin ich"]:
                print(Welt[player.location].name)
                print(Welt[player.location].description)
                Karte.print_map()

            elif action_input in ["nimm"]:
                player.take(Welt["Stift"])
                #worldmap.visibleworld()
                pass

            elif action_input in ["schau an"]:
                print(worldmap.visibleworld(Karte,Welt,player.location))
        #else:
        #    print("Das verstehe ich nicht, gebe 'Aktion' ein um die Liste der möglichen Aktionen zu sehen")


play()
