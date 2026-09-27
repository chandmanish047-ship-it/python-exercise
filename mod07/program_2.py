class Car():
    def __init__(self, registeration_number,max_speed):
        self.registeration_number=registeration_number
        self.max_speed=max_speed
        self.current_speed=0
        self.travelled_distance=0
    def accelerate(self, speed_change):
        self.speed_change=speed_change
        new_speed=self.current_speed+self.speed_change
        if new_speed>self.max_speed:
            self.current_speed=self.max_speed
        elif self.current_speed<0:
            self.current_speed=0
        else:
            self.current_speed=new_speed
        return self.current_speed
    
c1=Car("ab32",160)
c1.accelerate(30)
c1.accelerate(60)
c1.accelerate(98)
print(f"current speed after acceleration {c1.current_speed}")