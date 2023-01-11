def intro():
    print("This program reads data for two")
    print("people and computes their basal")
    print("metabolic rate and burn rate.")
    print()


def bmr_calculator():
    print("Next Person's information:")
    height = int(input("height "))
    weight = int(input("weight "))
    age = int(input("age "))
    gender = input("gender ")
    print()

    if (gender == "male"):
        return 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    elif (gender == "female"):
        return 447.593 + 9.247 * weight + 3.098 * height - (4.330 * age)
    else:
        return "invalid gender"

def report_status(bmr):
    if bmr<1200:
        print("low resting burn rate")
    elif bmr<=2000:
        print("moderate resting burn rate")
    else:
        print("high resting burn rate")
    

def report_results(bmr1,bmr2):
    print()
    print("Person #1 bmr = ", round(bmr1,1))
    report_status(bmr1)
    print("Person #2 bmr = ", round(bmr2,1))
    report_status(bmr2)

intro()
bmr1=bmr_calculator()
bmr2=bmr_calculator()
report_results(bmr1,bmr2)