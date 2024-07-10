def is_leap(year):
    leap = False
    a = 4
    b = 100
    c = 400
    # Write your logic here
    if (year%b)==0 and (year%c)==0:
        return True
    else:
        if (year%b)==0:
            return False
        elif (year%a)==0:
            return True

    return leap

year = int(input())
print(is_leap(year))
