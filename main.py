h = float(input("Enter height: "))
w = float(input("Enter weight: "))

BMI = w/(h/100)**2

print("BMI: ",BMI)

if BMI <= 18.4:
    print("Under Weight")

elif BMI <= 24.9:
    print("healthy")
    
elif BMI <= 29.9:
    print("Over Weight")
    
elif BMI <= 34.9:
    print("Severly Over Weight")
    
elif BMI <= 39.9:
    print("obese")

else:
    print("Severly obese")