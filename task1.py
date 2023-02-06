#Enter input
t1input= input("Enter input1 ")
t2input= input("Enter input1 ")

#cast entry to float and print error message if it's not a number
validEntry = False
try:
    t1 = float(t1input)
    t2 = float(t2input)
    validEntry = True
except:
    print("error with imput, enter numbers")

#the formula
def jains(t1, t2, n):
    JFI = ((t1 + t2) ** 2) / (n * (t1 ** 2 + t2 ** 2))
    #JFI = ((t1 +t2)**2) / (n*(t1**2 + t2**2))
    print(JFI)

#check if numbers are valid and then run formula. Error message if not
if validEntry == True:
    jains(t1,t2,2)
elif validEntry == False:
    print("Please try again")



