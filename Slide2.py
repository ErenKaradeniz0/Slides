#this is a comment

def first_function():
    print("first function worked")
    print("the second line")

first_function()

def main():
    message1()
    message2()
    print("Done with everything.")
def message1():
    print("This is message1.")
def message2():
    print("This is message2.")
    message1()
    print("Done with message2.")
    
main()