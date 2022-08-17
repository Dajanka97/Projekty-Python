 #Ponizsze zmienne sa polami gry
p0 = " "
p1 = " "
p2 = " "
p3 = " "
p4 = " "
p5 = " "
p6 = " "
p7 = " "
p8 = " "

#Siatka do gry
print(f"{p0}|{p1}|{p2}\n"
        f"{p3}|{p4}|{p5}\n"
            f"{p6}|{p7}|{p8}")

#zmienna ktora przechowuje informacje o aktualnym graczu
gracz = "O"

#Petla w ktorej wykonuje sie gra
while True:
    liczba = int(input("Wpisz liczbe od 1 do 9: "))
    if liczba == 1:
        if p0 != " ":
            print("To pole jest zajęte!")
            continue
        p0 = gracz
    if liczba == 2:
        if p1 != " ":
            print("To pole jest zajęte!")
            continue
        p1 = gracz
    if liczba == 3:
        if p2 != " ":
            print("To pole jest zajęte!")
            continue
        p2 = gracz
    if liczba == 4:
        if p3 != " ":
            print("To pole jest zajęte!")
            continue
        p3 = gracz
    if liczba == 5:
        if p4 != " ":
            print("To pole jest zajęte!")
            continue
        p4 = gracz
    if liczba == 6:
        if p5 != " ":
            print("To pole jest zajęte!")
            continue
        p5 = gracz
    if liczba == 7:
        if p6 != " ":
            print("To pole jest zajęte!")
        p6 = gracz
    if liczba == 8:
        if p7 != " ":
            print("To pole jest zajęte!")
            continue
        p7 = gracz
    if liczba == 9:
        if p8 != " ":
            print("To pole jest zajęte!")
            continue
        p8 = gracz

#Zmiana aktulalnego gracza na przeciwnego
    if gracz == "O":
        gracz = "X"
    elif gracz == "X":
        gracz = "O"

    print(f"{p0}|{p1}|{p2}\n"
            f"{p3}|{p4}|{p5}\n"
             f"{p6}|{p7}|{p8}")


#Zmienne sprawdzające warunki wygranej
    if p0 == p1 and p1 == p2 and p0 != " ":
        print("Wygrałeś!")
        break
    if p3 == p4 and p4 == p5 and p3 != " ":
        print("Wygrałeś!")
        break
    if p6 == p7 and p7 == p8 and p7 != " ":
        print("Wygrałeś!")
        break
    if p0 == p3 and p3 == p6 and p6 != " ":
        print("Wygrałeś!")
        break
    if p2 == p5 and p5 == p8 and p5 != " ":
        print("Wygrałeś!")
        break
    if p1 == p4 and p4 == p7 and p4 != " ":
        print("Wygrałeś!")
        break
    if p0 == p4 and p4 == p8 and p8 != " ":
        print("Wygrałeś!")
        break
    if p2 == p4 and p4 == p6 and p2 != " ":
        print("Wygrałeś!")
        break

#Zmienne sprawdzajace czy nastapil remis
    if p0 != " " and p1 != " " and p2!= " " and p3 != " " and p4 != " " and p5 != " " and p6 != " " and p7 != " " and p8 != " ":
        print("Remis!")
        break






