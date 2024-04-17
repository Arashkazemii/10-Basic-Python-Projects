import tkinter as tk

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

def convert():
    try:
        value = float(entry_temp.get())
        inScale = entry_inScale.get().upper()
        outScale = entry_outScale.get().upper()
        
        converted_value = tempConvertor(value, inScale, outScale)
        label_result.config(text=f"{value} {inScale} = {converted_value:.2f} {outScale}")
    except ValueError:
        label_result.config(text="Invalid input!")

root = tk.Tk()
root.title("Temperature Converter")
root.resizable(False,False)

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_temp = tk.Label(frame, text="Temperature:")
label_temp.grid(row=0, column=0, padx=5, pady=5)

entry_temp = tk.Entry(frame)
entry_temp.grid(row=0, column=1, padx=5, pady=5)

label_inScale = tk.Label(frame, text="Input Scale:")
label_inScale.grid(row=1, column=0, padx=5, pady=5)

entry_inScale = tk.Entry(frame)
entry_inScale.grid(row=1, column=1, padx=5, pady=5)

label_outScale = tk.Label(frame, text="Output Scale:")
label_outScale.grid(row=2, column=0, padx=5, pady=5)

entry_outScale = tk.Entry(frame)
entry_outScale.grid(row=2, column=1, padx=5, pady=5)

button_convert = tk.Button(frame, text="Convert", command=convert)
button_convert.grid(row=3, columnspan=2, padx=5, pady=5)

label_result = tk.Label(root, text="")
label_result.pack(padx=10, pady=10)

root.mainloop()