scales = {
    'Celsius' : 'C',
    'Fahrenheit' : 'F',
    'Kelvin' : 'K'
}

def convertor(value, inScale, outScale):
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
    
    
while True :
    print('Enter the value:')
    value = float(input())
    print('Enter the input scale (C, F, K):')
    inScale = input().upper()
    print('Enter the output scale (C, F, K):')
    outScale = input().upper()
    convert = convertor(value, inScale, outScale)
    print(f'{value} {inScale} = {convert} {outScale}')
    print('Enter (quit) to quit, or any other key to continue:')
    choice = input()
    if choice.lower() == 'quit':
        break