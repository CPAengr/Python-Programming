temperatures=[38.5,100,-275]

def writer(temperatures):
    with open("temps.ext", 'w') as file:
        for f in temperatures:
            if f>-273.15:
                c=(f-32)*5/9
                file.write(str(c)+"\n")

writer(temperatures)
