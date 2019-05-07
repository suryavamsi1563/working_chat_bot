from datetime import datetime
import parsedatetime
from dateutil.parser import parse


def date_formater(dt):
    try:
        dt = parse(dt)
        if datetime.today().strftime("%m")>=dt.strftime("%m"):
            
            print("3")
            return dt.strftime("%b %d, %Y")
        else:
           print("4")
           return dt.strftime("%b %d"),int(dt.strftime("%Y"))-1  
    except ValueError:
        cal = parsedatetime.Calendar()
        time_struct, parse_status = cal.parse(dt)
        date=datetime(*time_struct[:6])
        if datetime.today().strftime("%m")>=date.strftime("%m"):
            print("1")
            return date.strftime("%b %d, %Y")
        else:
           print("2")
           print(date.strftime("%b %d"),int(date.strftime("%Y")))

print(date_formater("25th june"))
