class Printer:
    color_printer = "White"

    def __init__(self, name_printer="Name", printing_speed=0, price=0, masa=0, producer="Producer", guarantee=12):
        self.name_printer = name_printer
        self.printing_speed = printing_speed
        self.price = price
        self.masa = masa
        self.producer = producer
        self.guarantee = guarantee

    def __del__(self):
        print("Delete ", self.name_printer)

    def __str__(self):
        return self.name_printer + " " + str(self.printing_speed) + " " + str(self.price) + " " + str(self.masa) + " "
        + str(self.producer) + " " + str(self.guarantee)  + " " + str(self.name_printer)

    @staticmethod
    def getcolor_printer():
        return Printer.color_printer

def main():
     Epson = Printer("L3050", 20, 1000, 5, "Epson", 12)
     Canon = Printer("PIXMA Ink Efficiency E414", 30, 2500, 3.4, "Canon", 14)
     Brother = Printer("Pro M426fdw", 40, 3000, 2, "Brother", 48)
     print("-------------")
     print(Epson.__str__() +  Printer.color_printer)
     print(Canon.__str__() +  Printer.color_printer)
     print(Brother.__str__() +  Printer.color_printer)
     print("-------------")


if "main" == "main":
 main()