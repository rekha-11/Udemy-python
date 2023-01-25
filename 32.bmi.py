def bmi(h,w):
    bmi = w/(pow(h,2))
    print(bmi)

h = int(input("Enter height in meter "))
w = int(input("Enter weight in kg"))
bmi(h,w)

