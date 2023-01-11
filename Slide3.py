def egg_top():
    print("  ______ ")
    print(" /      \\")
    print("/        \\")


def egg_bottom():
    print("\\        /")
    print(" \\______/")

def line():
    print("+--------+")

   


def egg():
    egg_top()
    egg_bottom()
    print()

def tea_cup():
    egg_bottom()
    line()
    print()

def stop_sign():
    egg_top()
    print("|  STOP  |")
    egg_bottom()
    print()

def hat():
    egg_top()
    line()

egg()
tea_cup()
stop_sign()
hat()





