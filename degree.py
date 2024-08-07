#WAP to convet temperature from user input
a= input("Enter 1 if you want to convert celcius to ferenhiet\n"
         "Enter 2 if you want to convert ferenhiet to celcius: ")
if a=="1":
    c= int(input("Enter the celcius: "))
    f= (c*9/5)+32
    print(f"{c} degrees Celsius is {f} degrees Fahrenheit.")
elif a=="2":
    f= int(input("Enter the ferenhiet: "))
    c= (f-32)*5/9
    print(f"{f} degrees Fahrenheit is {c} degrees Celsius.")
else:
    print("Invalid input")
