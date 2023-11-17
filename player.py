#import world
import worldmap

class Player:
    def __init__(self):
        self.inventory = []
        self.location = "Buero"

    def print_inventory(self):
        print("Inventar")
        for item in self.inventory:
            print('* ' + str(item))

    def walk(self, place):
        #need to see whether or not it accsessible -- via map
        #place should be a diciotnary entry in worldmap object Welt

        self.location = place.key
        print(place.name)
        print(place.description)


    def take(self,item):
        #need to check if item is in scene beforehand (and a "takeable")! but might make that on action lvl
        name = getattr(item,'name')
        self.inventory.append(name)
        print("Mein Inventar ist jetzt: ")
        self.print_inventory()
        #take item out of scene
        #self.location.scene.remove(str(item.key))

