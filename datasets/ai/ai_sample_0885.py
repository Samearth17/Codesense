def RGB_to_HSL(RGBList):
    output = []
    for color in RGBList:
        r = color[0]/255
        g = color[1]/255
        b = color[2]/255
        c_max = max(r, g, b)
        c_min = min(r, g, b)
        delta = c_max - c_min

        h = 0
        if delta == 0:
            h = 0
        elif c_max == r:
            h = 60 * (((g - b)/delta) % 6)
        elif c_max == g:
            h = 60 * (((b - r)/delta) + 2)
        elif c_max == b:
            h = 60 * (((r - g)/delta) + 4)

        l = (c_max + c_min)/2

        s = 0
        if delta == 0:
            s = 0
        else:
            s = delta/(1 - abs((2 * l) - 1))

        output.append([h,s,l])
    return output