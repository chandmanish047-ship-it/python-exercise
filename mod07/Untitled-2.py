class person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    @property
    def fullname(self):
        return(f"{self.firstname}-{self.lastname}")
p=person("manish","chand")
print(p.fullname)