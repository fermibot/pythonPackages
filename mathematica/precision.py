def Round(x):
    try:
        if x % int(x) < 0.5:
            return int(x)
        elif x % int(x) >= 0.5:
            return int(x) + 1
    except TypeError:
        print("Input needs to be integer or float")