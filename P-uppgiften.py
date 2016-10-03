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
        if random.random() < 0.5: #Sannolikhet för desperado = 1/1000
            #TODO
            self.desperado = True
            print ("DESPERADOOOOO HEELP")

    def statusEnter(self):
        print(u"Kl ", clock.tellTime(),)
    def statusLeave(self):
        print(u"Kl ", clock.tellTime(), "går kund ", self.number, "och kund ",)

def arrive(clock, probability):
    arrive = False
    if random.random() < probability: #random returnerar värde mellan 1 och 0, sannolikheten att det är under 0.2 är 20%
        arrive = True
    if clock >= 1080:
        arrive = False
    return arrive #booleska värden 1/0

def errands(): #returnerar antalet ärenden, 50% return 1, 25% return 2, etc.
    errands = 0
    c = 0
    while c == 0:
        c = random.randrange(0,2) #50% sannolikhet att c blir 1 eller 0 vilket gör att sannolikheten halveras varje gång whileslingan körs
        errands += 2 #2 == 1 ärende, förenklar när ett ärende tar 2 min (2 iterationer) i while i main()
    return errands

def mrsFranco():
    return

#def main():
#    clock = Time(540) #skapa objekt från konstruktorn "Time" och ställ tiden till 09.00
#    queue = []
#    customerNumber = 0
#    workerTime = 2
#    wait = 0
#    while clock.counter <  1200 or len(queue) > 0: #Betjäna kunder så länge klockan är mindre än 18.00 eller om det finns kunder kvar
        
#        if arrive(clock.counter) is True: #Om kund kommer in genom dörren
#            customer = Customer(customerNumber,errands()) #skapa kund med könummer och antal ärenden
#            customerNumber += 1

#            if len(queue) is 0:
#                print('Kl',clock.tellTime(),'kommer kund',customer.number,'in och blir genast betjänad')
#            else:
#                print('Kl',clock.tellTime(),'kommer kund',customer.number,'in och ställer sig i kön som nr',len(queue)+1)

#            queue.append(customer) #Om kund kommer in 

#        if len(queue) > 0:
#            if workerTime == 0:
#                queue[0].errands -= 1
#                workerTime = 2
#            if queue[0].errands == 0:
#                if len(queue) > 1:
#                    print('Kl',clock.tellTime(),'går kund',queue[0].number,'och kund',queue[1].number,'blir betjänad')
#                else:
#                    print('Kl',clock.tellTime(),'går kund',queue[0].number)
#                queue.pop(0)
#            workerTime -= 1

#        if len(queue) > 1:
#            wait += 1
#        clock.advanceTime()

#        if clock.counter == 1080: #Om klockan är 18.00
#            print('Kl',clock.tellTime(),'stängs dörren')
            
#    print('STATISTIK:',customerNumber,'kunder, kundväntetid', wait, 'minuter =',int((wait*60)/customerNumber),'s/kund')

def printMessage(message ,currentTime, customerNumber=0, queueNumber=0):
    if message == 0: 
        print('Kl', currentTime, 'kommer kund', customerNumber, 'in och blir genast betjänad')
    elif message == 1:
        print('Kl', currentTime, 'kommer kund', customerNumber, 'in och ställer sig i kön som nr', queueNumber)
    elif message == 2:
        print('Kl',currentTime,'går kund', customerNumber,'och kund', queueNumber, 'blir betjänad')
    elif message == 3:
        print('Kl',currentTime,'går kund', customerNumber)
    elif message == 4:
        print('Kl',currentTime,'stängs dörren')
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
    errorcode5 = ""

    while validInput == False:
        textInput = input(instruction)
        length = len(textInput)

        if length == 5:
            textInput = textInput[:2] + ":" + textInput[3:] #Slicing away any delimiter, standardizing it
      
        #timeHours, timeMinutes = map(int, textInput.split(":")) #Delar värdena och samtidigt konverterar till int

        if 0 < length < 5: #H, HH, HHMM, fråga om input korrekt
            try: 
                #H -> HH:MM
                if length == 1: 
                    textInput = "0" + textInput[0] + ":00"

                #HH -> HH:MM
                elif length == 2: 
                    textInput = textInput[:2] + ":00"

                #Ologisk input
                elif length == 3: 
                    print(errorcode3, errorcode1)

                #HHMM -> HH:MM
                elif length == 4: 
                    textInput = textInput[:2] + ":" + textInput[2:]

        elif length == 0: #om längd på input = 0
            print (errorcode2, errorcode1)

        try:
            timeHours, timeMinutes = map(int, textInput.split(":")) #Delar värdena och samtidigt konverterar till int
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
def main():

    clock = Time(540) #skapa objekt från konstruktorn "Time" och ställ tiden till 09:00, (9*60 = 540)
    queue =  collections.deque()
    customerNumber = 0
    wait = 0

    officeOpen  = inputTime("Mata in när postkontoret öppnar: ")
    print (officeOpen)

    officeClose  = input("Mata in när postkontoret stänger: ")
    print (officeClose)

    while clock.counter <  1080 or len(queue) > 0: #Betjäna kunder så länge klockan är mindre än 18:00 (18*60 = 1080) eller om det finns kunder kvar
        
        if arrive(clock.counter, 0.2) is True:                   #Om kund kommer in genom dörren
            customerNumber += 1   
            customer = Customer(customerNumber, errands())  #skapa kund med könummer och antal ärenden
            queue.append(customer)                          #lägg till kund i kö

            if len(queue) == 1:
                printMessage(0,clock.tellTime(), customer.number)
            else:
                printMessage(1,clock.tellTime(), customer.number, len(queue))
            
        if len(queue) > 0: #om kö finns

            if queue[0].errands > 0: #Om det finns ärenden kvar att utföra
                queue[0].errands -= 1

            if queue[0].errands == 0: #om färdigbehandlad
                if len(queue) > 1:
                    printMessage(2, clock.tellTime(), queue[0].number, queue[1].number)
                else:
                    printMessage(3, clock.tellTime(), queue[0].number)

                queue.popleft() #Ta bort betjänad kund från kö

        if len(queue) > 1:
            wait += 1

        clock.advanceTime()

        if clock.counter == 1080: #Om klockan är 18.00

            printMessage(4, clock.tellTime())
            
    print('STATISTIK:',customerNumber,'kunder, kundväntetid', wait, 'minuter =',int((wait*60)/customerNumber),'s/kund')
    
def testErrands():
    print('\nTEST av errands()\nSannolikheter för antal ärenden:')
    stat = 500*[0]
    for n in range(100000):
        number = int(errands() / 2)
        stat[number] += 1
    print('Antal Sannolikhet Förekomst')
    for i,n in enumerate(stat):
        if n > 0:
            print('',str(i).zfill(2),'   ',str(round(100*(n/sum(stat)),2)).ljust(5,'0'),'%   ',str(n).rjust(5,' '))

def testArrive():
    print('\nTEST av arrive()\nSannolikhet för kundinträde:')
    stat = 2*[0]
    for n in range(1000000):
        state = arrive(500, 0.3)
        if state is True:
            stat[0] += 1
        else:
            stat[1] += 1
    print('True:',stat[0],'\nFalse:',stat[1],'\nSannolikhet för att True ges:',round(100*(stat[0]/sum(stat)),2),'%')

#Huvudprogram
main()
testErrands()
testArrive()
# 