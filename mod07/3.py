class elevator:
    def __init__(self,bottom,top):
        self.bottom=bottom
        self.top=top
        self.current=bottom
    def floor_up(self):
        self.current=self.current+1
        print(f"elevator is at floor{self.current}")
    def floor_down(self):
        self.current-=1
        print(f"elevator is at floor{self.current}")
    def go_to_floor(self,floor):
        while self.current!=floor:
            if self.current>floor:
                self.floor_down()
        else:
            self.floor_up()
e=elevator(1,18)
e.go_to_floor(5)
