def tempConvertor(value, inScale, outScale):
    if inScale == 'C':
        if outScale == 'F' : 
            return value * 1.8 + 32
        elif outScale == 'K' :
            return value + 273.15
        else :
            return value
    elif inScale == 'F' :
        if outScale == 'C' :
            return ( value - 32 ) / 1.8
        elif outScale == 'K' :
            return ( value - 32 ) / 1.8 + 273.15
        else :
            return value
    elif inScale == 'K' :
        if outScale == 'C' :
            return value - 273.15
        elif outScale == 'F' :
            return ( value - 273.15 ) * 1.8 + 32
        else :
            return value
    else :
        return value