listInputdata = [123, 2.234, 3.5, 4, 243]

#casts the list to flot
listCastedToFloat = [float(i) for i in listInputdata]

#___TOP PART OF CALCULATION______

#SUM THE LIST
sumNummer = sum(listCastedToFloat)

#POWER 2 THE SUM OF THE LIST
JFIoppe = sumNummer**2


#BOTTOM PART OF CALCULATION_____

#-- makes the bottom of the formula to power (2)
def turn_to_power(list, power=2):
    return [number**power for number in list]
opphoyd = turn_to_power(listCastedToFloat)

#Sums the list after power
sumOpphoyd = sum(opphoyd)

#--- mulitplies the list in power with N
JFInede = sumOpphoyd*len(listCastedToFloat)

#DIVIDES THE TOP WITH THE BOTTOM______
finalJFI = JFIoppe/JFInede
print(finalJFI)
