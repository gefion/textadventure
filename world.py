import random
import time

class Room:
    def __init__(self):
        raise NotImplementedError("Mache keinen leeres Raum Objekt")
    
    def __str__(self):
        return self.name

    def lookat(self):
        print(self.description)

    def use(self):
        print(idontunderstand())
    
    def usewith(self,item):
        print("Das funktioniert nicht")
        
    def open(self):
        print("Das kann ich nicht öffnen.")

    def close(self):
        print("Das kann ich nicht schließen.")
        
    def talkto(self):
        print("Ich rede lieber mit mir selber als mit dem Raum.")
        
    def giveto(self,npc):
        print("Das kann ich nicht geben.")

    
class Openable:
    def __init__(self):
        raise NotImplementedError("Erstelle kein leeres Door Objekt")
    def __str__(self):
        return self.name
    
    def lookat(self):
        print(self.description)

    def use(self):
        if self.status == "zu":
            print("Wird geöffnet!")
            self.status = "auf"
        elif self.status == "auf":
            print("Wird geschlossen")
            self.status = "zu"
        else:
            raise ValueError("Die Tür hat einen Status den sie nicht haben sollte")
    
    def usewith(self,item):
        print(idontunderstand())
        
    def open(self):
        if self.status == "zu":
            print("Ich öffne die Tür.")
            self.status = "auf"
        else:
            print("Die Tür ist schon offen.")

    def close(self):
        if self.status == "auf":
            print("Ich schließe die Tür.")
            self.status = "zu"
        else:
            print("Die Tür ist schon zu.")
            
    def talkto(self):
        print("\"Mit dir zu sprechen ist wie mit einer Wand zu reden!\"")
        
    def giveto(self,npc):
        print("Das kann ich nicht geben.")



class Thing:
    def __init__(self):
        raise NotImplementedError("Erstelle kein leeres Thing Objekt")
    def __str__(self):
        return self.name
    
    def lookat(self):
        print(self.description)

    def use(self):
        print("Das kann ich so nicht benutzen.")
    
    def usewith(self,item):
        print(idontunderstand())
        
    def open(self):
        print("Es geht nicht auf.")

    def close(self):
        print("Es geht nicht zu.")
            
    def talkto(self):
        print("Keine Antwort. Seltsam.")
        
    def giveto(self,npc):
        print("Nein, das mache ich lieber nicht.")

class Scene: #only lookable
    def __init__(self):
        raise NotImplementedError("Erstelle kein leeres Thing Objekt")
    def __str__(self):
        return self.name
    
    def lookat(self):
        print(self.description)

    def use(self):
        print("Das kann ich so nicht benutzen.")
    
    def usewith(self,item):
        print(idontunderstand())
        
    def open(self):
        print("Es geht nicht auf.")

    def close(self):
        print("Es geht nicht zu.")
            
    def talkto(self):
        print("Keine Antwort. Seltsam.")
        
    def giveto(self,npc):
        print("Nein, das mache ich lieber nicht.")

class NPC: #non player characters, lots of dialogue options
    def __init__(self):
        raise NotImplementedError("Erstelle kein leeres Thing Objekt")
    def __str__(self):
        return self.name
    
    def lookat(self):
        print(self.description)

    def use(self):
        print("Menschen sollte man nicht benutzen. Das wurde mir von Kindesbeinen an beigebracht. Wobei ich höre dass es in der Hinsicht in der anderen Arbeitsgruppe Probleme gibt.")
    
    def usewith(self,item):
        print(idontunderstand())
        
    def open(self):
        print("Es geht nicht auf.")

    def close(self):
        print("Es geht nicht zu.")
            
    def talkto(self):
        print("Hallo!")
        print("...")
        print("Keine Antwort")
        
        
    def giveto(self,npc):
        print("Nein, das mache ich lieber nicht.")


class Buero(Room):
    def __init__(self):
        self.name = "Büro"
        self.key = "Buero"
        self.aliases = ["Büro","Buero","büro","buero"]
        self.description = "Das Büro in dem ich arbeite. Es liegt im Keller der Universität und hausiert die drei Doktoranden in unserer Arbeitsgrupppe, sowie hin und wieder Studierende unterer Semester die an Bachelor oder Masterarbeiten arbeiten. Es stehen vier Schreibtische an den Wänden und es gibt eine Tür zum Flur. Eine andere Tür führt zu einer kleinen Abstellkammer.\nAn einem der Schreibtische sitzt Katrin, meine Kollegin."
        self.scene = ["Daten","Stift","Schreibtische","Postkarte","Katrin"]
        self.doors = ["AbstellkammerBuero","FlurBuero"]

class Flur(Room):
    def __init__(self):
        self.name =  "Flur"
        self.key = self.name
        self.aliases=["Flur","flur"]
        self.description = "Der Flur unserer Arbeitsgruppe. Es gibt keine Fenster und ein Ende des Flurs ist seit einigen monaten tiefschwarz weil die Glühbirne fehlt. Wenn man durch läuft findet man irgendwann die Teeküche. Am anderen Ende ist die Tür zum Büro unserer Arbeitsgruppenleiterin. Daneben ist die Tür des Sektretariats, unter ihr schimmert ein wenig Licht"
        self.scene = []
        self.doors = ["FlurBuero"]

class Abstellkammer(Room):
    def __init__(self):
        self.name = "Abstellkammer"
        self.key = self.name
        self.aliases = ["Abstellkammer","Kammer","abstellkammer","kammer","Abstellraum","abstellraum"]
        self.description = "Büromaterialien, einige kaputte Stühle, Ordner mit kryptischen Namen und eine verstaute Garnitur von Bettzeug."
        self.scene = ["AbstellkammerBuero"]


class FlurBuero(Openable):
    def __init__(self):
        self.name = "Tür zwischen Büro und Flur"
        self.key = "FlurBuero"
        self.aliases = ["FlurBüro","Tür zwischen FLur und Büro","Tür zwischen Büro und Flur"]
        self.description = "Da ist nichts besonderes zu sehen, es ist nur eine Tür."
        self.status = "zu"


class AbstellkammerBuero(Openable):
    def __init__(self):
        self.name = "Tür zur Abstellkammer"
        self.key = "AbstellkammerBuero"
        self.aliases = [self.name,self.key]
        self.description = "Jemand hat Eine Postkarte aus Spanien aufgehangen. Dem Vergilbungsgrad nach zu urteiln war das vor mindestens fünf Jahren."
        self.status = "zu"
        self.locked = "zu"


    def use(self):
        if self.locked == "zu":
            print("Es ist abgeschlossen.")
        else:
            if self.status == "zu":
                print("Wird geöffnet!")
                self.status = "auf"
            elif self.status == "auf":
                print("Wird geschlossen")
                self.status = "zu"
            
    def open(self):
        if self.locked == "zu":
            print("Es ist abgeschlossen.")
        else:
            if self.status == "zu":
                print("Ich öffne die Tür.")
                self.status = "auf"
            else:
                print("Die Tür ist schon offen.")
        

    def close(self):
        if self.locked == "zu":
            print("Es ist sogar abgeschlossen. Zu-er geht es nicht.")
        else:
            if self.status == "auf":
                print("Ich schließe die Tür.")
                self.status = "zu"
            else:
                print("Die Tür ist schon zu.")

    def usewith(self,item,Karte,Welt,player):
        print("i am in the usewith funciton")
        if item == "Schluessel":
            print("ich benutze den Schlüssel")
            self.locked ="auf" 
            self.open()
            player.inventory.remove(Welt[item].name)
            Karte.update_door_status(Welt[self.key])
            
    
    

class Daten(Scene):
    def __init__(self):
        self.name = "Daten"
        self.key = self.name
        self.aliases= ["Datum","daten","Daten"]
        self.description_first = "Landschaftsdaten von einem entlegenen Ort in Nordsibirien. Die Gegend ist geprägt von wilder Natur, eineigen Weidewiesen und ein wenig Agrarlandschaft.\nAußerdem gibt es einen besonders großen See der mir auf den Daten vom Vohrjahr nicht aufgefallen ist. Zumindest den Spektraldaten nach sollte es ein See sein. Ich suche im Institusserver nach besagten Daten vom Vorjahr bis ich sehe dass meine Kollegin Martina sie mit einem Passwort geschützt hat. Ich werde sie fragen müssen."
        self.description = "Da ist ein See in meinen Daten der vorher nicht da war, wie kommt auf einmal so viel Wasser in eine Gegend wo eigentlich keines war? Ich muss dringend Martina nach dem Passwort fragen um mir die Daten des Vorjahres an zu sehen."
        self.objective = "Martinas Passwort für den Ordner mit der Daten des Vorjahres heraus finden"
        self.found = False #something to mark wether or not the item has been looked at before



    def lookat(self):
        if self.found == False:
            print(self.description_first)
            self.found = True
        else:
            print(self.description)

class Stift(Thing):
    def __init__(self):
        self.name = "Stift"
        self.key =self.name
        self.aliases=["Stift","stift","Kugelschreiber","kugelschreiber","Stifte","stifte","Kulli","kulli"]
        self.description = "Ein normaler Kugelschreiber."

    def use(self):
        print("Ich brauche etwas worauf ich schreiben kann")


class Schreibtische(Scene):
    def __init__(self):
        self.name = "Schreibtische"
        self.key = self.name
        self.aliases = ["Schreibtische","schreibtische","Schreibtisch","schreibtisch"]
        self.description = "Zwei der Schreibtische gehören den anderen beiden Doktoranden in der Arbeitsgruppe, Martina und Pierre. Einer ist gerade frei, aber wird normalerweise von Studierenden benutzt die ihre Bachelor oder Masterarbeiten schreiben. Auf Martinas Schreibtisch liegt ein einsamer Kugelschreiber."


class Postkarte(Thing):
    def __init__(self):
        self.name = "Postkarte"
        self.key = self.name
        self.aliases = ["postkarte","Karte","karte"]
        self.description = "Auf der einen Seite ist eine pittoreske Gasse zu sehen, mit einem enthusiastischem Schriftzug \"Schöner in Spanien\". Auf der Rückseite steht nur \"Wartet nicht auch mich\", ohne Absender."

    def use(self):
        print("Niemand wird mir glauben dass ich in Wahrheit gerade in Spanien bin.")
    def giveto(self,npc):
        if npc == "Katrin":
            if npc.status == "talked to": #action only happens if player talked to Katrin before, otherwise they would not know she would like a postcard
                print("Hier. Hilft das Bild ein bisschen?")
                return "ok"
            else:
                print("Was soll sie denn damit? Ich habe keinen Grund ihr das zu geben")
            
class Schluessel(Thing):
    def __init__(self):
        self.name = "Schlüssel"
        self.key = "Schluessel"
        self.aliases = [self.name,self.key,"schlüssel","schluessel","Schluessel"]
        self.description = "Ein regulärer Schlüssel"

    def use(self):
        print("Der Schlüssel allein öffnet nicht die Tür")
    def usewith(self,item,Karte,Welt,player):
        if item == "AbstellkammerBuero":
            Welt[item].locked ="auf" 
            Welt[item].open()
            player.inventory.remove(self.name)
            Karte.update_door_status(Welt[item])

class Katrin(NPC): #non player characters, lots of dialogue options
    def __init__(self):
        self.name = "Katrin"
        self.key = "Katrin"
        self.aliases = ["katrin"]
        self.description = "Meine Co-Doktorandin Katrin. Sie sieht so müde aus wie ich mich fühle. Gerade sitzt sie am Tisch und starrt in ihren Kafee."
    
    def lookat(self):
        print(self.description)

    def use(self):
        print("Was meinst du! Katrin ist zu nett um sie zu \"benutzen\"")
    
    def usewith(self,item):
        print(idontunderstand())
        
    def open(self):
        print("Wenn ich mit ihr rede bekomme ich bestimmt hilfreiche Informationen aus ihr raus")

    def close(self):
        print("...das ergibt doch keinen Sinn.")
            
    def talkto(self):
        print("Ich: Hey Katrin, wie geht es dir heute")
        time.sleep(2)
        print("Katrin: Uff. Der Kafee ist noch nicht im System angekommen")
        time.sleep(2)
        print("Ich: Ich könnte den Schlüssel zur Abstellkammer gebrauchen, hast du den zufällig?")
        time.sleep(2)
        print("Katrin fängt an in ihrer Schreibtischschublade herum zu wühlen und holt nach einer Weile einen Schlüssel heraus.")
        print("Katrin: Probier mal den hier, ich glaube das könnte der sein.")
        return "Schluessel"
        


                

def idontunderstand():
    r = random.random()
    if r < 0.50:
        print("Das ergibt keinen Sinn.")
    elif r < 0.80:
        print("Wirklich? Ich glaube ich mache das lieber nicht.")
    elif r < 0.95:
        print("Was denkst du denn das dann passiert? Ich versuche es lieber nicht")
