import Convertort as con
scales = {
    'Celsius' : 'C',
    'Fahrenheit' : 'F',
    'Kelvin' : 'K'
}
    
while True :
    print('Enter the value:')
    value = float(input())
    print('Enter the input scale (C, F, K):')
    inScale = input().upper()
    print('Enter the output scale (C, F, K):')
    outScale = input().upper()
    convert = con.tempConvertor(value, inScale, outScale)
    print(f'{value} {inScale} = {convert} {outScale}')
    print('Enter (quit) to quit, or any other key to continue:')
    choice = input()
    if choice.lower() == 'quit':
        break