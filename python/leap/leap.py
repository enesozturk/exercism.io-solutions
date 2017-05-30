def is_leap_year(param):
    pass
    if (param%100==0):
        if(param%400==0):
            return True
    else:
        if(param%4==0):
            return True
        else:
            return False