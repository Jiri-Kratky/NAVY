def line(x):
    return 3 * x + 2

#calculate if the point is bellow or above line
def above_below(x,y):
    if y > line(x):
        return 1
    else:
        return -1