monthNumber = int(input())

months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
seasons = ["зима", "весна", "лето", "осень"]

if(0 < monthNumber < 13):
    print(months[monthNumber - 1])
    
    if(monthNumber < 3 or monthNumber == 12): season = seasons[0]
    elif(monthNumber < 6): season = seasons[1]
    elif(monthNumber < 10): season = seasons[2]
    else: season = seasons[3]

    print(season)
else: 
    print("ошибка")