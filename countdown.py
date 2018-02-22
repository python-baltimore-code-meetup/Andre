import time
from datetime import date
    
def countdown():
    # Get date user wants for countdown, parses to int
    year = int(input('[x] Year:'))
    month = int(input('[x] month:'))
    day = int(input('[x]day:'))
    #assigns first and last dates (need to make today's date) 
    first = date(2018, 2, 22)
    last = date(year, month, day)
    #calculates the difference in order to get countdown
    difference = last - first
    # while ticker > 0:         -wanted to loop through the countdown...-
    #     print (ticker)
    #     ticker = ticker - 1
    #     if ticker == 0:
    #         print('Your count is...' + ticker)
    print(str(year) + '-' + str(month) + '-' + str(day) + ' is ' + str(difference.days) + ' day(s) away!')

#countdown()
