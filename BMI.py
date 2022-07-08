print("BMI Calculator: ")
peso=float(input("What's your weight?" ))
altura=float(input("What's your height?" ))
altura**=2
imc=peso/altura
print("Your BMI is: %.2f\n" % imc)

if imc < 16:
    print("Severe Thiness")
elif imc >=16 and imc < 17:
    print("Moderate Thiness")
elif imc >= 17 and imc <18.5:
    print("Thiness")
elif imc >= 18.5 and imc < 25:
    print("Normal")
elif imc >= 25 and imc < 30:
    print("Overweight")
elif imc >= 30 and imc < 35:
    print("Obese Class I")
elif imc >= 35 and imc < 40:
    print("Obese Class II")
else:
    print("Obese Class III")