system = input("Metric or Imperial?\n").lower()

def metric():
  height = float(input("Enter your height in m: "))
  weight = float(input("Enter your weight in kg: "))

  bmi = round((weight / (height)**2 ), 2)

# Check entered values to make sure they are placed correctly
  if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are slightly underweight.")
  elif bmi < 25:
    print(f"Your BMI is {bmi}, you are normal weight.")
  elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
  elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
  else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


def imperial():
  height = float(input('Enter your height in ft: '))
  height_inch = float(input('Enter your height in in: '))
  weight = float(input("Enter your weight in lbs: "))

  total_height = (height * 12) + height_inch

  bmi = round(((weight / (total_height)**2 ) * 703 ), 2)

  if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are slightly underweight.")
  elif bmi < 25:
    print(f"Your BMI is {bmi}, you are normal weight.")
  elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
  elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
  else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

if system == "metric":
   metric()
elif system == "imperial":
  imperial()
