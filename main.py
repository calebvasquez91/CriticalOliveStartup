print("Welcome to the rollercoaster")
height=int(input("What is your height in cm? "))

if height >= 120:
  print("you can ride")
  age=int(input("what is your age? "))
  if age >= 12:
    print("that will be $5")
  elif age >= 18:
    print("that will be $7")
  else:
    print("that will be $12")
  

else:
  print("sorry no go")