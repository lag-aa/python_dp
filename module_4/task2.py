def last_discharge(a: str):
    point = a.find('.')
    number = ['0'] * len(a)
    number[point], number[-1] = '.', '1'
    res = float(a) - float(''.join(number))
    return res if point != -1 else int(res)
        
print(last_discharge(input()))