import world

class Player:
    def __init__(self):
        self.inventory = []
        self.location = "Buero"

    def print_inventory(self):
        print("Inventar")
        for item in self.inventory:
            print('* ' + str(item))

    def walk(self,room):
        #need to see whether or not it accsessible -- via map
        
        if isinstance(room, world.Room): #or issubclass() ? 
            print("Ich trete ein.")
            self.location = room
            print(self.location.name)
            print(self.location.description)
        else:
            print("Dort kann ich nicht eintreten.")


    def take(self,item):
        #need to check if item is in scene beforehand (and a "takeable")! but might make that on action lvl
        name = getattr(item,'name')
        self.inventory.append(name)
        print("Mein Inventar ist jetzt: ")
        self.print_inventory()
        #take item out of scene
        #self.location.scene.remove(str(item.key))

