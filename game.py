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
    print(Welt[player.location].name)
    print(Welt[player.location].description)
    #vis = worldmap.visibleworld(Karte,Welt,player.location) #visible world available to interact with for the player
    while True:
        action_input = get_player_command()
        vis = worldmap.visibleworld(Karte,Welt,player.location) #visible world available to interact with for the player

        player_action(action_input,vis,Karte,Welt,player)
        
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


def SVOfinder(doc):
    s,v,o = [],"NONE",[]
    for token in doc.sentences[0].words:
        if token.deprel in "root":
            v = token
        elif token.deprel in ["nobj","obj","obl","nmod"]:
            o.append(token)
        elif token.deprel in ["nsubj","subj","nmod"]:
            s.append(token)
    return s,v,o
        


def get_player_command():
    print('.')
    print('.')
    command = input('>>> ')
    print('.')
    print('.')

    doc = nlp(command)
    doc.sentences[0].print_dependencies()
    
    return command

def get_available_actions(dict):
    available = ["benutzen","sehen", "nehmen", "geben", "öffnen", "schließen", "gehen", "reden", "geben", "Inventar", "i", "Aktion", "Aktionen", "A", "a","wo bin ich"]
    return available

Action_verbalias = dict(
    lookat = ["schauen","sehen","ansehen","anschauen","gucken","angucken","seh","schau", "Schau","Seh","gucken","guck","Guck"],
    take = ["nehmen","nimm"],
    goto = ["gehen","eintreten","tritt","Tritt","treten","geh"],
    open = ["öffnen","aufmachen"],
    close = ["schließen"],
    talkto = ["reden","sprechen"],
    giveto = ["geben"],
    use = ["benutze"],
    usewith = ["benutze"]
)

def player_action(command,availableworld,Karte,Welt,player):

    #parsing
    doc = nlp(command)
    doc.sentences[0].print_dependencies()
    s,v,o = SVOfinder(doc)

    available = []
    for key,value in Action_verbalias.items():
        for i in value:
            available.append(i)

    items,doors,rooms,stuff = availableworld

    print(stuff)
    
    if v.lemma or v.text in available:
        if (v.lemma in Action_verbalias["lookat"]):# and (s[0].text or o[0].text in availableworld):
            print("Ich kenne diese Akiton!! es ist lookat")
            if len(o)>0:
                print(o[0].text)
                if o[0].text in stuff:
                    Welt[o[0].text].lookat()
                if o[0].text in ["Tür","tür"]:
                    if len(doors)>1:
                        print("Moment, welche Tür soll ich mir ansehen?")
                        dooraliases = []
                        counter = 0
                        for i in doors:
                            counter +=1
                            print("\n")
                            print(counter)
                            print(Welt[i].name)
                            dooraliases.append(Welt[i].name)
                            
                            #print(Welt[i].description) 
                            
                        answer=get_player_command()
                        if answer in dooraliases:
                            a = dooraliases.index(answer)
                            Welt[doors[a]].lookat()
                        try:
                            Welt[doors[int(answer)-1]].lookat()
                        except:
                            print("Irgendetwas ist schief gelaufen beim Versuch die Tür an zu sehen")
                            
                    elif len(doors)>0:
                        Welt[doors[0]].lookat()
                    else:
                        print("Hier sind keine Türen die ich ansehen kann.")
                    
            elif len(s)>0:
                if s[0].text in stuff:
                    print(Welt[s[0].text].lookat())
                if s[0].text in ["Tür","tür"]:
                    if len(doors)>1:
                        print("Moment, welche Tür soll ich mir ansehen?")
                        dooraliases = []
                        counter = 0
                        for i in doors:
                            counter +=1
                            print("\n")
                            print(counter)
                            print(Welt[i].name)
                            dooraliases.append(Welt[i].name)
                            
                            #print(Welt[i].description) 
                            
                        answer=get_player_command()
                        if answer in dooraliases:
                            a = dooraliases.index(answer)
                            print(Welt[doors[a]].lookat())
                            #print(Welt[doors[a]].description)
                        try:
                            print(Welt[doors[int(answer)-1]].lookat())
                            #print(Welt[doors[int(answer)-1]].description)
                        except:
                            print("Irgendetwas ist schief gelaufen beim Versuch die Tür an zu sehen")
                            
                    elif len(doors)>0:
                        print(Welt[doors[0]].lookat())
                        #print(Welt[doors[0]].description)
                    else:
                        print("Hier sind keine Türen die ich ansehen kann.")
                        
        if (v.lemma in Action_verbalias["open"]):# and (s[0].text or o[0].text in availableworld):
            if len(o)>0:
                if o[0].text in stuff:
                    Welt[o[0].text].open()
                if o[0].text in ["Tür","tür"]:
                    if len(doors)>1:
                        print("Moment, welche Tür soll ich öffnen?")
                        dooraliases = []
                        counter = 0
                        for i in doors:
                            counter +=1
                            print("\n")
                            print(counter)
                            print(Welt[i].name)
                            dooraliases.append(Welt[i].name)
                            
                            #print(Welt[i].description) 
                            
                        answer=get_player_command()
                        if answer in dooraliases:
                            a = dooraliases.index(answer)
                            Welt[doors[a]].open()
                            Karte.update_door_status(Welt[o[0].text])
                        try:
                            Welt[doors[int(answer)-1]].open()
                            Karte.update_door_status(Welt[doors[int(answer)-1]])
                        except:
                            print("Irgendetwas ist schief gelaufen beim Versuch eine Tür zu öffnen")
                            
                    elif len(doors)>0:
                        Welt[doors[0]].open()
                        Karte.update_door_status(Welt[doors[0]])
                    else:
                        print("Hier sind keine Türen die ich öffnen kann. (Um Himmelswillen wie habe ich das den geschafft, irgendwo muss ich doch rein gekommen sein)")
                
                    
            elif len(s)>0:
                if s[0].text in stuff:
                    Welt[s[0].text].open()
                
                if s[0].text in ["Tür","tür"]:
                    if len(doors)>1:
                        print("Moment, welche Tür soll ich öffnen?")
                        dooraliases = []
                        counter = 0
                        for i in doors:
                            counter +=1
                            print("\n")
                            print(counter)
                            print(Welt[i].name)
                            dooraliases.append(Welt[i].name)
                            
                            #print(Welt[i].description) 
                            
                        answer=get_player_command()
                        if answer in dooraliases:
                            a = dooraliases.index(answer)
                            Welt[doors[a]].open()
                            Karte.update_door_status(Welt[doors[a]])
                        try:
                            Welt[doors[int(answer)-1]].open()
                            Karte.update_door_status(Welt[doors[int(answer)-1]])
                        except:
                            print("Irgendetwas ist schief gelaufen beim Versuch eine Tür zu öffnen")
                            
                    elif len(doors)>0:
                        print(Welt[doors[0]].open())
                        Karte.update_door_status(Welt[doors[0]])
                    else:
                        print("Hier sind keine Türen die ich öffnen kann. (Um Himmelswillen wie habe ich das den geschafft, irgendwo muss ich doch rein gekommen sein)")

        if (v.lemma in Action_verbalias["close"]):# and (s[0].text or o[0].text in availableworld):
            print("ICH KENNE DIESE AKTION!")
            if len(o)>0:
                if o[0].text in stuff:
                    Welt[o[0].text].close()
                if o[0].text in ["Tür","tür"]:
                    if len(doors)>1:
                        print("Moment, welche Tür soll ich schließen?")
                        dooraliases = []
                        counter = 0
                        for i in doors:
                            counter +=1
                            print("\n")
                            print(counter)
                            print(Welt[i].name)
                            dooraliases.append(Welt[i].name)
                            
                            #print(Welt[i].description) 
                            
                        answer=get_player_command()
                        if answer in dooraliases:
                            a = dooraliases.index(answer)
                            Welt[doors[a]].close()
                            Karte.update_door_status(Welt[doors[a]])
                        try:
                            Welt[doors[int(answer)-1]].close()
                            Karte.update_door_status(Welt[doors[int(answer)-1]])
                        except:
                            print("Irgendetwas ist schief gelaufen beim Versuch eine Tür zu schließen")
                            
                    elif len(doors)>0:
                        Welt[doors[0]].close()
                        Karte.update_door_status(Welt[doors[a]])
                    else:
                        print("Hier sind keine Türen die ich schließen kann. (Um Himmelswillen wie habe ich das den geschafft, irgendwo muss ich doch rein gekommen sein)")
                
                    
            elif len(s)>0:
                if s[0].text in stuff:
                    print(Welt[s[0].text].close())
                
                if s[0].text in ["Tür","tür"]:
                    if len(doors)>1:
                        print("Moment, welche Tür soll ich schließen?")
                        dooraliases = []
                        counter = 0
                        for i in doors:
                            counter +=1
                            print("\n")
                            print(counter)
                            print(Welt[i].name)
                            dooraliases.append(Welt[i].name)
                            
                            #print(Welt[i].description) 
                            
                        answer=get_player_command()
                        if answer in dooraliases:
                            a = dooraliases.index(answer)
                            Welt[doors[a]].close()
                            Karte.update_door_status(Welt[doors[a]])
                        try:
                            print(Welt[doors[int(answer)-1]].close())
                            Karte.update_door_status(Welt[doors[int(answer)-1]])
                        except:
                            print("Irgendetwas ist schief gelaufen beim Versuch eine Tür zu schließen")
                            
                    elif len(doors)>0:
                        print(Welt[doors[0]].close())
                        Karte.update_door_status(Welt[doors[0]])
                    else:
                        print("Hier sind keine Türen die ich schließen kann. (Um Himmelswillen wie habe ich das den geschafft, irgendwo muss ich doch rein gekommen sein)")


        if (v.lemma in Action_verbalias["take"]):# and (s[0].text or o[0].text in availableworld):
            if len(o)>0:
                if o[0].text in stuff:
                    player.take(Welt[o[0].text])
                    Welt[player.location].scene.remove(o[0].text)
                
                    
            elif len(s)>0:
                if s[0].text in stuff:
                    player.take(Welt[s[0].text])
                    Welt[player.location].scene.remove(s[0].text)

        if (v.lemma in Action_verbalias["goto"]):# and (s[0].text or o[0].text in availableworld):
            if len(o)>0:
                if o[0].text in rooms:
                    player.walk(Welt[o[0].text])
                
                    
            elif len(s)>0:
                if s[0].text in rooms:
                    player.walk(Welt[s[0].text])
                
            else:
                print("Dort kann ich nicht eintreten.")

        if (v.lemma in Action_verbalias["use"]):# and (s[0].text or o[0].text in availableworld):
            if len(o)>0:
                if o[0].text in stuff:
                    Welt(o[0].text).use()
                
                    
            elif len(s)>0:
                if s[0].text in stuff:
                    Welt(o[0].text).use()
                
            else:
                print("Dort kann ich nicht eintreten.")
                
    else:
        print("Diese Aktion kenne ich nicht.")
    

play()
