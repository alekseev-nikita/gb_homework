from warehouse import Warehouse
from office_equipment import *


wh = Warehouse()

p1 = Printer(100, 10, True, False)
p2 = Printer(450, 25, True, True)
s1 = Scaner(200, 20, 8)
s2 = Scaner(300, 15, 15)
x1 = Xerox(240, 13, 20)
x2 = Xerox(270, 17, 16)

wh.add_equipment(p1)
wh.add_equipment(p2)
wh.add_equipment(s1)
wh.add_equipment(s2)
wh.add_equipment(x1)
wh.add_equipment(x2)
print(wh)
wh.remove_equipement(p2)
wh.remove_equipement(p2)
print(wh)
