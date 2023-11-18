import stanza
nlp = stanza.Pipeline('de')
import worldmap


def get_player_command():
    print('.')
    print('.')
    command = input('>>> ')
    print('.')
    print('.')

    doc = nlp(command)
    doc.sentences[0].print_dependencies()
    
    return command

Action_verbalias = dict(
    lookat = ["schauen","sehen","ansehen","anschauen","gucken","angucken","seh","schau", "Schau","Seh","gucken","guck","Guck"],
    take = ["nehmen","nimm"],
    goto = ["gehen","eintreten","tritt","Tritt","treten","geh"],
    open = ["öffnen","aufmachen","oeffnen","öffne","oeffne"],
    close = ["schließen","schließe","schliessen","schliesse"],
    talkto = ["reden","sprechen"],
    giveto = ["geben"],
    use = ["benutze"],
    usewith = ["benutze"]
)
tuer = ["Tür","tür","Tuer","tuer"]

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
        


def player_action(command,availableworld,Karte,Welt,player):

    #parsing
    doc = nlp(command)
    doc.sentences[0].print_dependencies()
    s,v,o = SVOfinder(doc)

    #unravelling all of the available things back into categories
    items,doors,rooms,stuff = availableworld
    print(availableworld)

    #getting the object class name from the alias that was used
    subj = "NAN"
    obj = "NAN"
    if len(s)>0:
        subj = worldmap.checkaliases(s[0].text,Welt)
    if len(o)>0:
        obj = worldmap.checkaliases(o[0].text,Welt)

    #check if I know the action
    action = "NAN"
    for x in Action_verbalias:
        if (v.text in Action_verbalias[x]) or (v.lemma in Action_verbalias[x]):
            action = x
            print("Ich kenne diese Aktion, es ist "+str(x))

    #if this is true, the input is probably useless
    if (subj=="NAN" and obj=="NAN"):
        print("Das habe ich nicht verstanden, versuch es nochmal")
        return
    #just making sure we're dealing with things in the available/visible world
    if (subj not in stuff+tuer) and (obj not in stuff+tuer):
        print("Das sehe ich nicht, was meinst du?")
        return
    else:
        print("Das Objekt ist "+str(obj))
        print("Das Subjekt ist "+str(subj))

    #this is a door fix, so you don't have to type out the full name of the door available to open it
    if ((obj in tuer) or (subj in tuer)):
        if len(doors)>1:
            print("Moment, welche Tür ist gemeint?")
            dooraliases = []
            counter = 0
            for i in doors:
                counter +=1
                print("\n")
                print(counter)
                print(Welt[i].name)
                dooraliases.append(Welt[i].name)
                            
            answer=get_player_command()
            if answer in dooraliases:
                a = dooraliases.index(answer)
                getattr(Welt[doors[a]],action)()
                if action in ["open","close"]:
                    Karte.update_door_status(Welt[doors[a]])
            try:
                getattr(Welt[doors[int(answer)-1]],action)()
                if action in ["open","close"]:
                    Karte.update_door_status(Welt[doors[int(answer)-1]])
            except:
                print("Irgendetwas ist schief gelaufen beim Versuch die Tür an zu sehen")
                            
        elif len(doors)>0:
            getattr(Welt[doors[0]],action)()
            if action in ["open","close"]:
                Karte.update_door_status(Welt[doors[0]])
        else:
            print("Hier sind keine Türen die ich ansehen kann.")
        return


    #most actions here
    if (action not in ["take","goto"]) and (obj!="NAN")  :
        getattr(Welt[obj],action)()
    if action not in ["take","goto"] and (subj!="NAN"):
        getattr(Welt[subj],action)()

    #and the missing actions
    if action=="take":
        if obj in stuff: #we already know that either obj or subj are there but not which one, so gotta check again
            player.take(Welt[obj])
            Welt[player.location].scene.remove(obj)
        if subj in stuff:
            player.take(Welt[subj])
            Welt[player.location].scene.remove(subj)

    if action=="goto":
        if obj in rooms: #gotta make sure it's actually walkable
            player.walk(Welt[obj])              
        if subj in rooms:
            player.walk(Welt[subj])                
        else:
            print("Dort kann ich nicht eintreten.")
