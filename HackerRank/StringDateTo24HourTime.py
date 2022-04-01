from datetime import datetime


def timeConversion(s):
    
    #d = datetime.strptime("22:30", "%H:%M")
    #print(d.strftime("%I:%M %p"))

    dt = datetime.strptime(s, '%I:%M:%S%p')    
    return dt.strftime('%H:%M:%S')

if __name__ == '__main__':
    print(timeConversion('01:45:56PM'))
    print(timeConversion('12:45:56AM'))

