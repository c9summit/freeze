#Harsahil Basra
#18/03/22
#Practice Loops

pin = int(input("Enter your 4 digit pin: "))

secretpin = 456
("%02d" % (secretpin,))



if pin == secretpin:
    print("Welcome to your account")
else:
    while pin != 456:
        print("That is the incorrect Code")
        pin = int(input("Please Try Again: "))



