import datetime

maybe_kennitala = input("Enter valid kennitala: ")

try:
    if maybe_kennitala[-1] == '9':
        reference_year = 1900
    elif maybe_kennitala[-1] == '0':
        reference_year = 2000
    else:
        reference_year = -1000 #Ef síðasta tákn í kennitölu annað en 9 eða 0 kemur error á testið fyrir neðan.
    birthday_day = int(maybe_kennitala[0:2])
    birthday_month = int(maybe_kennitala[2:4])
    birthday_year = int(maybe_kennitala[4:6]) + reference_year
    birthday = datetime.date(birthday_year, birthday_month, birthday_day)
except ValueError:
    print("{} is not a valid kennitala!".format(maybe_kennitala))
