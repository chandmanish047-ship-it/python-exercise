class Car:
    def __init__(self,registeration_number,max_speed):
        self.registeration_number=registeration_number
        self.max_speed=max_speed
        self.current_speed=0
        self.travelled_distance=0
    def accelerate(self,speed_change):
        new_speed=self.current_speed+speed_change
        if new_speed>self.max_speed:
            self.current_speed=self.max_speed
        elif new_speed<0:
            self.current_speed=0
        else:
            self.current_speed=new_speed
        return self.current_speed
    def drive(self,hours):
        self.travelled_distance+=self.current_speed*hours
c1=Car("abc",160)
c1.accelerate(30)
c1.accelerate(60)
c1.accelerate(98)
c1.drive(1.5)
print(f"Current speed: {c1.current_speed} km/h")
print(f"Travelled distance: {c1.travelled_distance} km")