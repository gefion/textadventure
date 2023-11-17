import world

class Worldmap:
    def __init__(self):

        self.doors = []

    def add_door(self, room1, room2, name, status): #add a door from room to room with status
        self.doors.append([room1,room2,name,status])
        self.doors.append([room2,room1,name,status])

    def update_door_status(self,door):
        for i in range(len(self.doors)):
            if door in self.doors[i]:
                if self.doors[i][3] == door.status:
                    pass
                    #print("nothing changes, this message should not appear")
                elif self.doors[i][3] == "zu":
                    self.doors[i][3] = door.status
                elif self.doors[i][3] == "auf":
                    self.doors[i][3] = door.status

    def tell_doors(self,loc):
        doors = []
        #print("ich bin hier!"+loc)
        for i in range(len(self.doors)):
            if loc == self.doors[i][0].key:
                doors.append(self.doors[i][2].key)
        return list(set(doors)) #throw away duplicates

    def print_map(self):
        for i in range(len(self.doors)):
            print("Tür \""+str(self.doors[i][2])+"\" zwischen ",self.doors[i][0], " und ", self.doors[i][1], " ist ", self.doors[i][3])

def createworld():
    Karte = Worldmap()

#  Welt = dict(
#
#      mapdict = dict(
#          Flur = world.Flur(),
#          Buero = world.Buero(),
#          Abstellkammer = world.Abstellkammer(),
#          AbstellkammerBuero = world.AbstellkammerBuero(),
#          FlurBuero = world.FlurBuero()
#      ),
#      itemsdict = dict(
#          Data = world.Data(),
#          Stift = world.Stift(),
#          Schreibtische = world.Schreibtische()
#      )
#  )

    Welt = dict(
        Flur = world.Flur(),
        Buero = world.Buero(),
        Abstellkammer = world.Abstellkammer(),
        AbstellkammerBuero = world.AbstellkammerBuero(),
        FlurBuero = world.FlurBuero(),
        Daten = world.Daten(),
        Stift = world.Stift(),
        Schreibtische = world.Schreibtische()
    )
    

    Karte.add_door(Welt["Flur"],Welt["Buero"],Welt["FlurBuero"],Welt["FlurBuero"].status)
    Karte.add_door(Welt["Buero"],Welt["Abstellkammer"],Welt["AbstellkammerBuero"],Welt["AbstellkammerBuero"].status)

    Karte.print_map()
    return Welt, Karte


def visibleworld(Karte, Welt, loc):
    items = Welt[loc].scene
    doors = Karte.tell_doors(loc)
    rooms = [loc]

    for a in Karte.doors:
        if a[2].key in doors:
            if a[3] == "auf":
                rooms.append(a[0].key)

    rooms = list(set(rooms))

    return items,doors,rooms,items + doors + rooms

