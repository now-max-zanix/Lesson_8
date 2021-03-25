import math

import time

class Rectangle:
    def pir(self, storona_a, storona_b):
        return float((storona_a + storona_b) * 2)
        
    def plo(self, storona_a, storona_b):
        return float(storona_a * storona_b)

    def volume(self, storona_a, storona_b, high):
        return float(storona_a * storona_b * high)


class Triangle():
    def pir(self, storona_a, storona_b, storona_c):
        return float((storona_a + storona_b + storona_c))
        
    def plo(self, storona_a, storona_b, storona_c):
        pol_per = (storona_a + storona_b + storona_c)/ 2
        return float(math.sqrt(pol_per * (pol_per - storona_a) * (pol_per - storona_b) * (pol_per - storona_c)))

    def volume(self, storona_a, storona_b, storona_c, high):
        return float(self.plo * high)

class Kub():
    def pir(self, storona_a):
        return float((storona_a  * 12))
        
    def plo(self, storona_a):
        return float(6 * (storona_a ** 2))

    def volume(self, storona_a):
        return float(storona_a ** 3)

class shar():
    def plo(self, radius):
        pi = 3.14
        return float(4 * pi *(radius ** 2))

    def volume(self, radius):
        pi = 3.14
        return float(4 * pi * (radius ** 3) / 3)

while True:
    step = input("""
Какая фигура?
Прямоугольник      - 1
Треугольник (2D)   - 2
Куб                - 3
Шар                - 4
Выход              -  Enter
Что выбираем: """)

    if not step:
        print("Печалька...")
        time.sleep(1)
        break
    elif step == "1":
        vib = input("""
Что вычисляем?
Периметр - 1
Площадь  - 2
Объем    - 3
Что выбираем: """)
        storona_a = float(input("\nВведите сторону A:"))
        storona_b = float(input("Введите сторону B:"))
        if vib == "1":
            z = Rectangle()
            print("Периметр ={:.2f}".format(z.pir(storona_a, storona_b)))
            time.sleep(2)
        elif vib == "2":
            z = Rectangle()
            print("Площадь = {:.2f}".format(z.plo(storona_a, storona_b))) 
            time.sleep(2)
        elif vib == "3":
            high = float(input("Введите высоту Н:"))
            z = Rectangle()
            print("Объем = {:.2f}".format(z.volume(storona_a, storona_b, high)))
            time.sleep(2)
    
    elif step == "2":
        vib = input("""
Что вычисляем?
Периметр - 1
Площадь  - 2
Объем    - 3
Что выбираем: """)
        storona_a = float(input("\nВведите сторону A:"))
        storona_b = float(input("Введите сторону B:"))
        storona_c = float(input("Введите сторону C:"))
        if vib == "1":
            p = Triangle()
            print("Периметр ={:.2f}".format(p.pir(storona_a, storona_b, storona_c)))
            time.sleep(2)
        elif vib == "2":
            p = Triangle()
            print("Площадь = {:.2f}".format(p.plo(storona_a, storona_b, storona_c)) )
            time.sleep(2)
        elif vib == "3":
            high = float(input("Введите высоту Н:"))
            p = Triangle()
            print("Объем  = {:.2f}".format(p.volume(storona_a, storona_b, storona_c, high)) )
            time.sleep(2)
            
    elif step == "3":
        vib = input("""
Что вычисляем?
Периметр - 1
Площадь  - 2
Объем    - 3
Что выбираем: """)
        storona_a = float(input("\nВведите сторону A:"))
        if vib == "1":
            z = Kub()
            print("Периметр ={:.2f}".format(z.pir(storona_a)))
            time.sleep(2)
        elif vib == "2":
            z = Kub()
            print("Площадь ={:.2f}".format(z.plo(storona_a)))
            time.sleep(2)
        elif vib == "3":
            z = Kub()
            print("Объем = {:.2f}".format(z.volume(storona_a)))
            time.sleep(2)
    elif step == "4":
        vib = input("""
Что вычисляем?
Площадь  - 1
Объем    - 2
Что выбираем: """)
        radius = float(input("\nВведите радиус:"))
        if vib == "1":
            z = shar()
            print("Площадь = {:.2f}".format(z.plo(radius)))
        if vib == "2":
            z = shar()
            print("Объем = {:.2f}".format(z.volume(radius)))
            time.sleep(2)
    else:
        print("Повторите")
        time.sleep(2)



