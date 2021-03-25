import time

class plus:
    def __init__(self, a):
        self.a = a
    # добавление двух объектов
    def __add__(self, prim):
        return self.a + prim.a 


class sravn:
    def __init__(self, a):
        self.a = a
    def __gt__(self, other):
        if(self.a > other.a):
            return True
        else:
            return False


while True:
    step = input("""
Plus -1
<>   -2
Exit - Enter    
What -> """)
    if step == "1":
        obj1 = plus(input("VV:"))
        obj2 = plus(input("VV:"))
        z = plus(obj1)
        print(obj1 + obj2)
        time.sleep(2)

    if step == "2":
        obj1 = sravn(input("VV:"))
        obj2 = sravn(input("VV:"))
        z = sravn(obj1)
        if(obj1>obj2):
            print("obj1 > obj2")
        else:
            print("obj1 < obj2")
            time.sleep(2)
