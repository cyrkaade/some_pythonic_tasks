def sqrt(number):
    if round(number ** (1 / 2)) == number ** (1 / 2):
        return int(number ** (1 / 2))
    else:
        return None


print(sqrt(144))
