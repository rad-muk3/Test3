c = 0
total = 0.0

while True:
    str = input("Enter a number: ")
    if(str == "done"):
        break
    fVal = float(str) 
    print(fVal)
    c=c+1
    total = total + fVal

    print("All Done")
       
