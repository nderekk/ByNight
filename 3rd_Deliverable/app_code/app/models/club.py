class Club:
    def __init__(self,id: int,name: str,location: str, manager: str):
        self.id=id
        self.name=name
        self.location=location
        self.__manager=manager
        self.events=[]
        self.staff_members=[]
        self.statistics=None

    def add_event(self, event):
        self.events.append(event)
        event.club = self

    def add_staff(self, staff):
        self.staff_members.append(staff)
        staff.club = self

        
        