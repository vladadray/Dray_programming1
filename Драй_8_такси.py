def taxi_fare(distance):
    return(round((tarif + add * distance/140), 2))
    
tarif = 240
add = 15
distance = int(input("Введите расстояние: "))
print('Стоимость поездки: ', taxi_fare(distance))
