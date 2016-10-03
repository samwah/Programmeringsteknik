# P-uppgift
# coding: utf-8
# Kösimulering

import random
import collections
import re #regex, regular expressions

class Settings:
    def __init__ (self, pEnter, open, close, pRobber):
        self.pEnter = pEnter
        self.pRobber = pRobber
        #self.
        self.open = open
        self.close = close

#Tidsklass
class Time:
    def __init__ (self,startTime):
        self.counter = startTime #Hur många minuter som passerat från 00:00

    def tellTime(self): #Denna metod returnerar tiden i standardformat 00.00
        timeHour, timeMinute = divmod(self.counter, 60) #omvandla med modulo till timmar, (hela, rest) (timmar, minuter)

        if timeMinute < 10: #lägg till 0 om ental, alltså "5" blir "05"
            timeMinute = "0"+str(timeMinute)
        else:
            timeMinute = str(timeMinute)

        timeStr = str(timeHour)+'.'+timeMinute
        return timeStr
    
    def advanceTime(self): #stega fram tiden med 1 minut
        self.counter += 1
        return

#Kundklass med statusutskrifter
class Customer:
    def __init__ (self, number, errands):
        self.number = number 
        self.errands = errands
        self.desperado = False
        if random.random() < 0.001: #Sannolikhet för desperado = 1/1000
            #TODO
            self.desperado = True

    def statusEnter(self):
        print(u"Kl ", clock.tellTime(),)
    def statusLeave(self):
        print(u"Kl ", clock.tellTime(), "går kund ", self.number, "och kund ",)

def arrive(probability):
    arrive = False
    if random.random() < probability: #random returnerar värde mellan 1 och 0, sannolikheten att det är under 0.2 är 20%
        arrive = True
    return arrive #booleska värden 1/0

def errands(): #returnerar antalet ärenden, 50% return 1, 25% return 2, etc.
    errands = 0
    c = 0
    while c == 0:
        c = random.randrange(0,2) #50% sannolikhet att c blir 1 eller 0 vilket gör att sannolikheten halveras varje gång whileslingan körs
        errands += 2 #2 == 1 ärende, förenklar när ett ärende tar 2 min (2 iterationer) i while i main()
    return errands
def desperado():
    desperado = False
    if random.random() < 0.001:
        desperado = True
    return desperado

def mrsFranco():
    return

def printMessage(message, currentTime, customerNumber=0, queueNumber=0):
    if message == 0: 
        print('Kl', currentTime, 'kommer kund', customerNumber, 'in och blir genast betjänad')
    elif message == 1:
        print('Kl', currentTime, 'kommer kund', customerNumber, 'in och ställer sig i kön som nr', queueNumber)
    elif message == 2:
        print('Kl', currentTime,'går kund', customerNumber,'och kund', queueNumber, 'blir betjänad')
    elif message == 3:
        print('Kl', currentTime,'går kund', customerNumber)
    elif message == 4:
        print('Kl', currentTime,'stängs dörren')
    else:
        print("nothing")
    return
#Allowed forms: H, HH, HHM, HHMM, HH:MM, HH.MM
def inputTime(instruction):

    validInput = False
    decodedTime = 0
    timeHours = 0
    timeMinutes = 0

    errorcode1 = "Vänligen mata in en tid i formatet HH:MM eller HH, exempelvis 15:00."
    errorcode2 = "Du matade inte in någonting!"
    errorcode3 = "Fel format!"
    errorcode4 = "Angiven tid existerar inte!"

    while validInput == False:
        textInput = input(instruction)
        length = len(textInput)

        if 0 < length < 5: #Någon av dessa format H, HH, HHMM, gissa output och fråga
            if length == 1: #konvertera H -> 0H:00
                textInput = "0" + textInput[0] + ":00"

            elif length == 2: #konvertera HH -> HH:00
                textInput = textInput[:2] + ":00"

            elif length == 3: #Ologisk input
                print(errorcode3, errorcode1)

            elif length == 4: #konvertera HHMM -> HH:MM
                textInput = textInput[:2] + ":" + textInput[2:]

        elif length == 0: #om längd på input = 0
            print (errorcode2, errorcode1)

        elif length == 5:
            textInput = textInput[:2] + ":" + textInput[3:] #Slicing away any delimiter, standardizing it

        try:
            timeHours, timeMinutes = map(int, textInput.split(":")) #Delar värdena och samtidigt konverterar till int
            if 0 <= timeHours <= 24 and 0 <= timeMinutes < 60:
                validInput = True
            else:
                print(errorcode4)
        except ValueError:
                print(errorcode3, errorcode1)
                
    decodedTime = (timeHours*60) + timeMinutes
    return decodedTime
def validate(data):
    while True:
        response = input("Är "+str(data)+" korrekt? J/N: ").lower()
        if response == "j":
            return True
        elif response == "n":
            return False
        else:
            print("Felaktigt svar, endast J och N är giltiga")

class PostOffice(object):
    def __init__(self, *args):
        self.queue = collections.deque()
        
def main():

    while True:
        officeOpen = inputTime("Mata in när postkontoret öppnar: ")
        officeClose = inputTime("Mata in när postkontoret stänger: ")
        if officeOpen < officeClose:
            break
        else:
            print("Butiken måste öppna innan den stänger")
    arriveProb = float(input("Mata in sannolikheten för att kund kommer in en given minut"))

    clock = Time(officeOpen) #skapa objekt från konstruktorn "Time" och ställ tiden till vad som angavs av användaren
    queue =  collections.deque()
    customerNumber = 0
    wait = 0
    postOffice = PostOffice()
    while clock.counter < officeClose or len(queue) > 0: #Betjäna kunder så länge det är öppet eller om det finns kunder kvar
        
        if arrive(arriveProb):                   #Om kund kommer in genom dörren
            customerNumber += 1   
            customer = Customer(customerNumber, errands())  #skapa kund med könummer och antal ärenden
            queue.append(customer)                          #lägg till kund i kö

            if len(queue) == 1:
                printMessage(0,clock.tellTime(), customer.number)
            else:
                printMessage(1,clock.tellTime(), customer.number, len(queue))
            
        if len(queue) > 0: #om kö ej tom

            if queue[0].errands > 0: #Om kund har ärenden kvar att utföra
                queue[0].errands -= 1

            if queue[0].errands == 0: #om kund är färdigbehandlad
                if len(queue) > 1:
                    printMessage(2, clock.tellTime(), queue[0].number, queue[1].number)
                else:
                    printMessage(3, clock.tellTime(), queue[0].number)

                queue.popleft() #Ta bort betjänad kund från kö

        if len(queue) > 1: #om kunder står i kö, lägg till väntetid.
            wait += 1

        clock.advanceTime()

        if clock.counter == officeClose: #Om det är stängninstid:
            printMessage(4, clock.tellTime())
            
    print('STATISTIK:',customerNumber,'kunder, kundväntetid', wait, 'minuter =',int((wait*60)/customerNumber),'s/kund')
    
def testErrands():
    print('\nTEST av errands()\nSannolikheter för antal ärenden:')
    stat = [0]
    state = " PASS "
    testLength = 100000
    progress = 0
    percent = 0
    for n in range(testLength):
        if n == progress:
            print("progress: ", round(n/(testLength/100)),"%")
            percent += 1
            progress += testLength/10
        number = int(errands()/2)
        while len(stat) <= number+1:
                stat.append(0)
        stat[number] += 1
    print('Antal Sannolikhet Förekomst')
    previousNumber = 0
    currentNumber = 0
    for i,n in enumerate(stat):
        if i > 0:
            print('',str(i).zfill(2),'   ',str(round(100*(n/sum(stat)),2)).ljust(5,'0'),'%   ',str(n).rjust(5,' '))
            if i == 1:
                previousNumber = round(100*(n/sum(stat)))
            else:
                currentNumber = round(100*(n/sum(stat)))
                if currentNumber-1 <= round(previousNumber/2) <= currentNumber+1:
                    None
                else:
                    state = " FAIL "
                previousNumber = currentNumber
    print('errands() function test: '+state)
def testArrive(probability):
    print('\nTEST av arrive()\nSannolikhet för kundinträde:')
    stat = 2*[0]
    
    for n in range(1000000):
        state = arrive(probability)
        if state is True:
            stat[0] += 1
        else:
            stat[1] += 1

    calculatedProbabilty = 100*(stat[0]/sum(stat))

    print('True:',stat[0],'\nFalse:',stat[1],'\nSannolikhet för att True ges:',round(calculatedProbabilty,2),'%')
    if(probability*100 == round(calculatedProbabilty)):
        state = " PASS "
    else:
        state = " FAIL "
    print('arrive() function test: '+state)

#Huvudprogram
#main()
testErrands()
testArrive(0.2)
# 