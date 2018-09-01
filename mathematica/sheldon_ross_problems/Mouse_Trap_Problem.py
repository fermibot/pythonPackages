import random
a = []
def mouse_trap(n):
    for r in range(0, n):
        trap = True
        time = 0
        while trap:
            nu = random.random()           
            if nu <= 1/3:
                time += 2
                trap = False
                a.append(time)
            elif (nu > 1/3 and nu <= 2/3):  time +=  3
            elif (nu > 2/3 and nu <= 1.0):  time +=  5
    print("The mean time spent by the mouse in {} trials is {}" .format(n, round(sum(a) / float(len(a)), 10 )))



mouse_trap(1000)