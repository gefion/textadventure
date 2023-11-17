import random

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
        
    def give(self,npc):
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
        if self.status == "auf":
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
        
    def give(self,npc):
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
        
    def give(self,npc):
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
        
    def give(self,npc):
        print("Nein, das mache ich lieber nicht.")


class Buero(Room):
    def __init__(self):
        self.name = "Büro"
        self.key = "Buero"
        self.description = "Das Büro in dem ich arbeite. Es liegt im Keller der Universität und hausiert die drei Doktoranden in unserer Arbeitsgrupppe, sowie hin und wieder Studierende unterer Semester die an Bachelor oder Masterarbeiten arbeiten. Es stehen vier Schreibtische an den Wänden und es gibt nur eine Tür zum Flur."
        self.scene = ["Daten","Stift","Schreibtische"]
        self.doors = ["AbstellkammerBuero","FlurBuero"]

class Flur(Room):
    def __init__(self):
        self.name =  "Flur"
        self.key = self.name
        self.description = "Der Flur unserer Arbeitsgruppe. Es gibt keine Fenster und ein Ende des Flurs ist seit einigen monaten tiefschwarz weil die Glühbirne fehlt. Wenn man durch läuft findet man irgendwann die Teeküche. Am anderen Ende ist die Tür zum Büro unserer Arbeitsgruppenleiterin. Daneben ist die Tür des Sektretariats, unter ihr schimmert ein wenig Licht"
        self.scene = []
        self.doors = ["FlurBuero"]

class Abstellkammer(Room):
    def __init__(self):
        self.name = "Abstellkammer"
        self.key = self.name
        self.description = "Büromaterialien, einige Kaputte Stühle, Ordner mit kryptischen Namen und eine verstaute Garnitur von Bettzeug."
        self.scene = ["AbstellkammerBuero"]


class FlurBuero(Openable):
    def __init__(self):
        self.name = "Tür zwischen Büro und Flur"
        self.key = "FlurBuero"
        self.description = "Da ist nichts besonderes zu sehen, es ist nur eine Tür."
        self.status = "zu"


class AbstellkammerBuero(Openable):
    def __init__(self):
        self.name = "Tür zur Abstellkammer"
        self.key = "AbstellkammerBuero"
        self.description = "Jemand hat Eine Postkarte aus Spanien aufgehangen. Dem Vergilbungsgrad nach zu urteiln war das vor mindestens fünf Jahren."
        self.status = "zu"


    def use(self):
        print("Es ist abgeschlossen.")
            
    def open(self):
        print("Es ist abgeschlossen.")
        

    def close(self):
        print("Es ist schon zu.")
    
    

class Daten(Thing):
    def __init__(self):
        self.name = "Daten"
        self.key = self.name
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
        self.description = "Ein normaler Kugelschreiber."


class Schreibtische(Scene):
    def __init__(self):
        self.name = "Schreibtische"
        self.key = self.name
        self.description = "Zwei der Schreibtische gehören den anderen beiden Doktoranden in der Arbeitsgruppe, Martina und Pierre. Einer ist gerade frei, aber wird normalerweise von Studierenden benutzt die ihre Bachelor oder Masterarbeiten schreiben. Auf Martinas Schreibtisch liegt ein einsamer Kugelschreiber."


def idontunderstand():
    r = random.random()
    if r < 0.50:
        print("Das ergibt keinen Sinn.")
    elif r < 0.80:
        print("Wirklich? Ich glaube ich mache das lieber nicht.")
    elif r < 0.95:
        print("Was denkst du denn das dann passiert? Ich versuche es lieber nicht")
