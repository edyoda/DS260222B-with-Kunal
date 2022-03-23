import math

pie = math.pi

def area(shape, *side):
    if shape.lower() == "circle":
        return pie*(side[0]**2)
    elif shape.lower() == "square":
        return side[0]**2
    elif shape.lower() == "rectangle":
        return side[0]*side[1]
    elif shape.lower() == "triangle":
        s = (side[0]+side[1]+side[2])/2
        v = s*(s-side[0])(s-side[1])(s-side[2])
        return math.sqrt(v)
    else:
        print("This shape is currently under progress")