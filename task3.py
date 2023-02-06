#I converted the list manually to Mbps and removed all text,
# so I just have numberts

#åpne fil og konvert til list (https://www.tutorialsteacher.com/articles/convert-file-to-list-in-python)
fileobj=open("values3")
lines=[]
for line in fileobj:
    lines.append(line.strip())


#cast list to float
listCastedToFloat = [float(i) for i in lines]


#Using the same code as in task2
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
print("JMI is", finalJFI)
