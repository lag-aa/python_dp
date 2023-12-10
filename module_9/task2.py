from datetime import date 

def days_lived(year, month, day):
    now = date.today()
    birdthday = date(year, month, day)
    return (now - birdthday).days

print(days_lived(1983, 7, 3))