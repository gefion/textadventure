import world

class Worldmap:
    def __init__(self):

        #self.doors = [[world.Flur(),world.Buero(),world.FlurBuero(),world.FlurBuero().status],[world.Buero(),world.Abstellkammer(),world.AbstellkammerBuero(),world.AbstellkammerBuero().status]]
        self.doors = []
        #self.doors_num = len(self.doors)

    def add_door(self, room1, room2, name, status): #add a door from room to room with status
        self.doors.append([room1,room2,name,status])
        self.doors.append([room2,room1,name,status])

    def update_door_status(self,door):
        for i in range(len(self.doors)):
            if door in self.doors[i]:
                if self.doors[i][3] == door.status:
                    print("nothing changes, this message should not appear")
                elif self.doors[i][3] == "zu":
                    self.doors[i][3] = door.status
                elif self.doors[i][3] == "auf":
                    self.door[i][3] = door.status

    def tell_doors(self,loc):
        doors = []
        for i in range(len(self.doors)):
            if loc in self.doors[i]:
                doors.append(self.doors[i][2])
        return list(set(doors)) #throw away duplicates

    def print_map(self):
        for i in range(len(self.doors)):
            print("Tür \""+str(self.doors[i][2])+"\" zwischen ",self.doors[i][0], " und ", self.doors[i][1], " ist ", self.doors[i][3])

def createworld():
    Karte = Worldmap()

    Welt = dict(

        mapdict = dict(
            Flur = world.Flur(),
            Buero = world.Buero(),
            Abstellkammer = world.Abstellkammer(),
            AbstellkammerBuero = world.AbstellkammerBuero(),
            FlurBuero = world.FlurBuero()
        ),
        itemsdict = dict(
            Data = world.Data(),
            Stift = world.Stift(),
            Schreibtische = world.Schreibtische()
        )
    )

    
    #Karte.add_door(Welt[mapdict["Flur"]],Welt[mapdict["Buero"]],Welt[mapdict["FlurBuero"]],Welt[mapdict["FlurBuero"]].status)
    #Karte.add_door(Welt[mapdict["Buero"],Welt["AbstellkammerBuero"],Welt["AbstellkammerBuero"],Welt["AbstellkammerBuero"].status)

    Karte.add_door(Welt["mapdict"]["Flur"],Welt["mapdict"]["Buero"],Welt["mapdict"]["FlurBuero"],Welt["mapdict"]["FlurBuero"].status)
    Karte.add_door(Welt["mapdict"]["Buero"],Welt["mapdict"]["AbstellkammerBuero"],Welt["mapdict"]["AbstellkammerBuero"],Welt["mapdict"]["AbstellkammerBuero"].status)

    Karte.print_map()
    return Welt, Karte


def visibleworld(Karte, Welt, loc):
    #this is not optimal, it would probably be better if the locaiton of a thing was stored in the room, instead of the thing....
    print("visible objects:")
    for i in range(len(loc.scene)):
        print(loc.scene[i].name)
    for i in range(len(Karte.tell_doors(loc))):
        print(Karte.tell_doors(loc)[i])
    
    pass
