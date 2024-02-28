import stanza
nlp = stanza.Pipeline('de')
import worldmap
import world


def get_player_command():
    print('.')
    print('.')
    command = input('>>> ')
    print('.')
    print('.')

    #doc = nlp(command)
    #doc.sentences[0].print_dependencies()
    
    return command

Action_verbalias = dict(
    lookat = ["schauen","sehen","ansehen","anschauen","gucken","angucken","seh","schau", "Schau","Seh","gucken","guck","Guck","umschauen"],
    take = ["nehmen","nimm"],
    goto = ["gehen","eintreten","tritt","Tritt","treten","geh"],
    open = ["öffnen","aufmachen","oeffnen","öffne","oeffne"],
    close = ["schließen","schließe","schliessen","schliesse"],
    talkto = ["reden","sprechen","sprich","Sprich"],
    giveto = ["geben"],
    use = ["benutze","mit","benutz"],
    #usewith = ["benutze"]
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
    #empty spaces crash the program, because the doc will be length 0
    if len(doc.sentences) == 0:
        print("Hm? Has du was gesagt? Nochmal bitte.")
        return
    doc.sentences[0].print_dependencies()
    s,v,o = SVOfinder(doc)

    #unravelling all of the available things back into categories
    items,doors,rooms,stuff = availableworld
    inventory = [worldmap.checkaliases(thing,Welt) for thing in player.inventory]
    print(availableworld)
    print(inventory)

    #getting the object class name from the alias that was used
    subj = "NAN"
    obj = "NAN"
    if len(s)>0:
        subj = worldmap.checkaliases(s[0].text,Welt)
    if len(o)>0:
        obj = worldmap.checkaliases(o[0].text,Welt)
    print("Das Objekt ist "+str(obj))
    print("Das Subjekt ist "+str(subj))
    if subj not in stuff+tuer+inventory:
        subj = "NAN"
        print("Dieses Subjekt kenne ich nicht")
    if obj not in stuff+tuer+inventory:
        obj = "NAN"
        print("Dieses Objekt kenne ich nicht")

    #if command=="benutze Schlüssel mit Tür":
    #    Welt["Schluessel"].usewith("AbstellkammerBuero",Karte,Welt,player)
    #    print("WHOOOSUCCSESSFUL")


    #check if I know the action
    action = "NAN"
    for x in Action_verbalias:
        if (v.text in Action_verbalias[x]) or (v.lemma in Action_verbalias[x]):
            if "mit" in command and x == "use":
                action="usewith"
                print("Ich kenne diese Aktion, es ist "+action)
                break
            else:
                action = x
                print("Ich kenne diese Aktion, es ist "+str(x))
                break

    #if this is true, the input is probably useless
    if (subj=="NAN" and obj=="NAN"):
        #print("Das habe ich nicht verstanden, versuch es nochmal")
        return

        
    #if (subj not in stuff+tuer+inventory) and (obj not in stuff+tuer+inventory):
    #    print("Das sehe ich nicht, was meinst du?")
    #    return
    #else:
    #    print("Das Objekt ist "+str(obj))
    #    print("Das Subjekt ist "+str(subj))

    #this is a door fix, so you don't have to type out the full name of the door available to open it, instead the code will always just list the number of available doors to try, and ask the user which one they meant. 
    if ((obj in tuer) or (subj in tuer)) or (any(b in command for b in tuer)):
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
            print(dooraliases)   
            answer=get_player_command()
            if answer in dooraliases: #if the answer was written out
                a = dooraliases.index(answer)
                if action in ["usewith"]:
                    #i feel like this part could be done more elegantly, but this will suffice for now, problem is nmod sentence thingy
                    if s[0].text in tuer: #if the frst subj or obj is the door
                        getattr(Welt[doors[a]],action)(Welt[s[1].text].key,Karte,Welt,player)
                    elif s[1].tetx in tuer:
                        getattr(Welt[doors[a]],action)(Welt[s[0].text].key,Karte,Welt,player)
                    elif o[0].text in tuer: #if the frst subj or obj is the door
                        getattr(Welt[doors[a]],action)(Welt[o[1].text].key,Karte,Welt,player)
                    elif o[1].tetx in tuer:
                        getattr(Welt[doors[a]],action)(Welt[o[0].text].key,Karte,Welt,player)
                        
                else:
                    getattr(Welt[doors[a]],action)()
                if action in ["open","close","use"]:
                    Karte.update_door_status(Welt[doors[a]])

            try: #if the answer was written as a number
                if action in ["usewith"]:
                    getattr(Welt[doors[int(answer)-1]],action)(Welt[obj].key,Karte,Welt,player)
                else:
                    getattr(Welt[doors[int(answer)-1]],action)()
                if action in ["open","close","use"]:
                    Karte.update_door_status(Welt[doors[int(answer)-1]])

            except Exception as e:
                print(e)
                print("Irgendetwas ist schief gelaufen")

        #this part is to ease the user experience, when there is only one door, there is no need to ask which one              
        elif len(doors)>0:
            if action in ["usewith"]:
                getattr(Welt[doors[int(answer)-1]],action)(Welt[obj].key,Karte,Welt,player)
            else:
                getattr(Welt[doors[0]],action)()
            if action in ["open","close","use"]:
                Karte.update_door_status(Welt[doors[0]])

        else:
            print("Hier sind keine Türen.") #this should never appear.
        return


    #easy actions here, the others need special treatment as they change something about the player or scene or both. Which is not possible to be done from inside the object classes at the moment
    if (action not in ["take","goto","giveto","talkto","usewith","use"]) and (obj in stuff+inventory)  :
        getattr(Welt[obj],action)()
    if action not in ["take","goto","giveto","talkto","usewith","use"] and (subj in stuff+inventory):
        getattr(Welt[subj],action)()

    #and the missing actions
    if action=="take":
        #print(isinstance(Welt[obj],world.Thing))
        if obj in stuff and isinstance(Welt[obj],world.Thing) and obj!="NAN": #we already know that either obj or subj are there but not which one, so gotta check again. also need to make sure that the object is of type "thing" since that means it is takeable
            player.take(Welt[obj])
            Welt[player.location].scene.remove(obj)
        elif subj in stuff and isinstance(Welt[subj],world.Thing) and subj!="NAN":
            player.take(Welt[subj])
            Welt[player.location].scene.remove(subj)
        else:
            print("Das kann ich nicht nehmen")

    if action=="goto":
        if obj in rooms: #gotta make sure it's actually walkable
            player.walk(Welt[obj])              
        elif subj in rooms:
            player.walk(Welt[subj])                
        else:
            print("Dort kann ich nicht eintreten.")

    if action=="giveto":
        if obj in inventory:
            ok = getattr(Welt[obj],action)()
            if ok == "ok": #if the giveto function returned an ok, only then actually remove item from inventory
                player.inventory.remove(obj)

        if subj in inventory:
            ok = getattr(Welt[obj],action())
            if ok == "ok": #if the giveto function returned an ok, only then actually remove item from inventory
                player.inventory.remove(obj)

    if action=="talkto":
        if obj in stuff:
            item = getattr(Welt[obj],action)()
            if item != None: #the talk to function may return an item if the npc gives one to the player
                print(item)
                player.take(Welt[item])

        if subj in stuff:
            item = getattr(Welt[subj],action)()
            if item != None: #the talk to function may return an item if the npc gives one to the player
                player.take(Welt[item])

    #we have to find out if the action is use or usewith. main difference is the use of the word "mit" (eng: with). since use is earlier in the list of acitons, it
