from datetime import date, datetime

myDate = date(2023, 5, 26)
today = date.today()

myTime = datetime.now()


def printing():
    print(myTime)
    print(myDate)
    print(today)
    print(today.year)
    print(today.month)
    print(today.day)


printing()
printing()
printing()
printing()
