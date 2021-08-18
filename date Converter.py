#Inputing the European date

Myear = int(input('Enter year: '))
Mmonth = int(input ('Enter month: '))
Mday = int(input ('Enter day: '))

# Function to convert European date to Shamsi date
def dateConv(Myear, Mmonth, Mday):
    Mmonthlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    #Number of european Months days
    Smonthlist = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]    #Number of solar Months days
    
#Checking 366-days year in european calendar
    if Myear%4 == 0:
        Mmonthlist[1] = 29
        
#total number of days
    Mdays = (Myear - 1) * 365 + sum(Mmonthlist[0:Mmonth-1]) + Mday + (Myear -1)// 4
    
    Sdays = Mdays -226899          #Difference between the first day of solar and European year
    Syear = ((Sdays - (((Myear -1)//4) - 155) ) //365) + 1         #Calculating solar year
    
    if ((Sdays - (((Myear -1)//4) - 155) ) %365)==0:
        Syear -= 1
        if Syear % 4 == 3:
            Sdays = 366
        else:
            Sdays = 365
    else:
        Sdays = ((Sdays - (((Myear - 1) // 4) - 155)) % 365)

    if  Syear %4 ==3:           #Checking 366-days year in solar calendar
        Smonthlist[11] = 30
#
#Calculating the day and month in solar year
    i = 0
    Smonth = 1

    while Sdays > Smonthlist[i]:
        Sdays -= Smonthlist[i]
        Smonth += 1
        i += 1

    Sday = Sdays

    return [Syear, Smonth, Sday]          # output of the dateconv function


[Syear, Smonth, Sday] = dateConv(Myear, Mmonth, Mday)

print('{} \ {} \ {}'.format(Syear, Smonth, Sday))
