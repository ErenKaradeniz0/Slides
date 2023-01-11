def bmi_calc(weight, height):
    height_sq=(height/100)**2
    bmi = weight/height_sq
    if (bmi < 18.4):
        print("you're underweight")
    elif (18.5 < bmi < 24.9):
        print("normal")
    elif (25.0 < bmi < 39.9):
        print("overweight")
    else:
        print("Obese")

bmi_calc(60,190)
bmi_calc(70,190)
bmi_calc(100, 190) 
bmi_calc(80,70)

def main():
    x, y, z=1,2,3
    print(x,y,z)
    mystery(z,y,x)
    mystery(y,x,z)

def mystery(x,z,y):
    print(z,"and",(y-x))

main()


def strange (x):
    x=x+1
    print("1. x =",x)
def test():
    x=23
    strange(x)
    print("2. x =",x)

test()