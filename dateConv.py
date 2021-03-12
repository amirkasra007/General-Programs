#vared kardane tarikhe milady
Myear = int(input('Enter year: '))
Mmonth = int(input ('Enter month: '))
Mday = int(input ('Enter day: '))
#tarif kardan tabE baraye tabdil be tarikhe shamsi
def dateConv(Myear, Mmonth, Mday):
    Mmonthlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    Smonthlist = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
#chek kardane sale kabise
    if Myear%4 == 0:
        Mmonthlist[1] = 29
#mohasebeye kolle roozha
    Mdays = (Myear - 1) * 365 + sum(Mmonthlist[0:Mmonth-1]) + Mday + (Myear -1)// 4
    Sdays = Mdays -226899          #tafavot beyne avlin rooze miladi v shamsi
    Syear = ((Sdays - (((Myear -1)//4) - 155) ) //365) + 1         #mohasebeye sale shamsi
    if ((Sdays - (((Myear -1)//4) - 155) ) %365)==0:
        Syear -= 1
        if Syear % 4 == 3:
            Sdays = 366
        else:
            Sdays = 365
    else:
        Sdays = ((Sdays - (((Myear - 1) // 4) - 155)) % 365)

    if  Syear %4 ==3:           #chek kardane sale kabise
        Smonthlist[11] = 30
#mohasebeye mah v rooz dar tarikhe shamsi
    i = 0
    Smonth = 1

    while Sdays > Smonthlist[i]:
        Sdays -= Smonthlist[i]
        Smonth += 1
        i += 1

    Sday = Sdays

    return [Syear, Smonth, Sday]          # khoroooji tabE


[Syear, Smonth, Sday] = dateConv(Myear, Mmonth, Mday)

print('{} \ {} \ {}'.format(Syear, Smonth, Sday))
