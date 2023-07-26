from player import Player
from collections import OrderedDict
#import world
import worldmap
import string
import stanza

nlp = stanza.Pipeline('de')

def play():
    print("Lab Madness")
    Welt, Karte = worldmap.createworld()
    player = Player()
    print(Welt["mapdict"][player.location].name)
    print(Welt["mapdict"][player.location].description)
    while True:
        action_input = get_player_command()
        if action_input in ["benutze","schau an", "nimm", "gib", "öffne", "schließe", "tritt ein","t", "Inventar", "i", "Aktion", "Aktionen", "A", "a","wo bin ich"]:
            if action_input in ["Aktion", "Aktionen", "A", "a"]:
                print("Mögliche Eingaben: "+str(get_available_actions()))
            if action_input in ["Inventar", "i"]:
                player.print_inventory()

            if action_input in ["tritt ein","t"]:
                player.walk(Welt["mapdict"]["Flur"])

            elif action_input in ["öffne"]:
                Welt["mapdict"]["FlurBuero"].open()
                Karte.update_door_status(Welt["FlurBuero"])

            elif action_input in ["wo bin ich"]:
                print(Welt["mapdict"][player.location].name)
                print(Welt["mapdict"][player.location].description)
                Karte.print_map()

            elif action_input in ["nimm"]:
                player.take(Welt["mapdict"][player.location].scene[1])
                #worldmap.visibleworld()
                pass

            elif action_input in ["schau an"]:
                worldmap.visibleworld(Karte,Welt,Welt["mapdict"][player.location])
        else:
            print("Das verstehe ich nicht, gebe 'Aktion' ein um die Liste der möglichen Aktionen zu sehen")


def SVOfinder(doc):
    s,v,o = [],[],[]
    for token in doc.sentences[0].words:
        if token.deprel in "root":
            v.append(token)
        elif token.deprel in ["nobj","obj","obl"]:
            o.append(token)
        elif token.deprel in ["nsubj","subj"]:
            s.append(token)
    return s,v,o
        


def get_player_command():
    command = input('>>> Was tue ich nun? ')

    doc = nlp(command)
    doc.sentences[0].print_dependencies()
    print(SVOfinder(doc))
    
    return command

def get_available_actions():
    available = ["benutzen","sehen", "nehmen", "geben", "öffnen", "schließen", "gehen", "reden", "geben", "Inventar", "i", "Aktion", "Aktionen", "A", "a","wo bin ich"]
    return available

def parse_player_action(command):
    
    doc = nlp(command)
    doc.sentences[0].print_dependencies()
    s,v,o = SVOfinder(doc)

    available = get_available_actions()
    if v.lemma in available:
        return doc
    else:
        print("Diese Aktion kenne ich nicht.")
    

play()
