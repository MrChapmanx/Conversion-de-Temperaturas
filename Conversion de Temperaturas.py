import math
while True:
    print("Hola usuario!")
    t1 = int(input("Ingrese la temperatura de ºC a ºF"))
    t2 = 1.8 * t1 + 32
    t3 = print("La tamperatura en Fahrenheit es: ",t2)
    t4 = float(input("Ingrese la temperatura de ºF a ºC"))
    t5 = 32 - t4
    result = t5 * 1/1.8
    t6 = print("La temperatura en Celsius es: ",result)
    t7 = int(input("Ingrese la temperatura de ºC a ºK"))
    t8 = t7 + 273
    t9 = print("La temperatura en Kelvin es: ",t8)
    t10 = int(input("Ingrese la temperatura de ºK a ºC"))
    t11 = t10 - 273
    t12 = print("La temperatura en Celsius es: ",t11)
    t13 = int(input("Ingrese la temperatura de ºK a ºF"))
    t14 = (t13 - 273.15) * 9/5 + 32
    t15 = print("La temperatura en Fahrenheit es: ",t14)
    t16 = int(input("Ingrese la temperatura de ºF a ºK"))
    t17 = (t16 - 32) * 5/9 + 273.15
    t18 = print("La temperatura en Kelvin es: ",t17)
    print("Fue un placer ayudarlo!")
    break











































