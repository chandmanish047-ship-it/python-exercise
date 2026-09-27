class publication:
    def __init__(self,name):
        self.name=name
class book(publication):
    def __init__(self,name,author,page_count):
        super().__init__(name)
        self.author=author
        self.page_count=page_count
    def print_information(self):
        print(f"book:{self.name}")
        print(f"author{self.author}")
        print(f"page count is{self.page_count}")
class magazine(publication):
    def __init__(self,name,chief_editor):
        super().__init__(name)
        self.chief_editor=chief_editor
    def print_information(self):
        print(f"Magazine: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")
if __name__ == "__main__":
    magazine = magazine("Donald Duck", "Aki Hyyppä")
    book = book("Compartment No. 6", "Rosa Liksom", 192)
    magazine.print_information()
    book.print_information()