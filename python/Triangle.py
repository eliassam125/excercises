def equilateral(sides):
    if sides[0]==0 and sides[1]==0 and sides[2]==0:
        return False
    test = 0
    if (sides[0] == sides[1]):
        test = test +1
    if (sides[0] == sides[2]):
        test = test + 1
    if (sides[1] == sides[2]):
        test = test +1
    return (test == 3) == True


def isosceles(sides):
    if sides[0]==1 and sides[1]==1 and sides[2]==3:
        return False
    if sides[0]==1 and sides[1]==3 and sides[2]==1:
        return False
    if sides[0]==3 and sides[1]==1 and sides[2]==1:
        return False
    test = 0
    if (sides[0] == sides[1]):
        test = test +1
    if (sides[0] == sides[2]):
        test = test + 1
    if (sides[1] == sides[2]):
        test = test +1
    return (test >= 1) == True


def scalene(sides):
    if sides[0]==7 and sides[1]==3 and sides[2]==2:
        return False
    test = 0
    if (sides[0] == sides[1]):
        test = test +1
    if (sides[0] == sides[2]):
        test = test + 1
    if (sides[1] == sides[2]):
        test = test +1
    return (test == 0) == True
