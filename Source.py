#Ferry Seating Classes
BCseatz = ['A1', 'A2', 'A3', 'A4', 'A5',
           'B1', 'B2', 'B3', 'B4', 'B5']

ECseatz = ['C1', 'C2', 'C3', 'C4', 'C5',
           'D1', 'D2', 'D3', 'D4', 'D5',
           'E1', 'E2', 'E3', 'E4', 'E5',
           'F1', 'F2', 'F3', 'F4', 'F5',
           'G1', 'G2', 'G3', 'G4', 'G5',
           'H1', 'H2', 'H3', 'H4', 'H5',
           'I1', 'I2', 'I3', 'I4', 'I5',
           'J1', 'J2', 'J3', 'J4', 'J5']

BC_seats_SC011 = [] + BCseatz
BC_seats_SC012 = [] + BCseatz
BC_seats_SC013 = [] + BCseatz
BC_seats_SC014 = [] + BCseatz
BC_seats_HC107 = [] + BCseatz
BC_seats_HC108 = [] + BCseatz
BC_seats_HC109 = [] + BCseatz
BC_seats_HC110 = [] + BCseatz
EC_seats_SC011 = [] + ECseatz
EC_seats_SC012 = [] + ECseatz
EC_seats_SC013 = [] + ECseatz
EC_seats_SC014 = [] + ECseatz
EC_seats_HC107 = [] + ECseatz
EC_seats_HC108 = [] + ECseatz
EC_seats_HC109 = [] + ECseatz
EC_seats_HC110 = [] + ECseatz
customerdata = []

#Ferry ID and Departure Time
PLTime = ["SC011 @ 10:00 AM", "SC013 @ 12:00 PM", "HC107 @ 02:00 PM", "HC109 @ 04:00 PM"]
LPTime = ["SC012 @ 11:00 AM", "SC014 @ 01:00 PM", "HC108 @ 03:00 PM", "HC110 @ 05:00 PM"]

#This function initiates the Main Menu
def MainMenu():
    print("""
            FERRY TICKETING SYSTEM
______________________________________________
Please enter the preferred option:
P - to Purchase the Ticket
V - to View the Seating Arrangement
Q - to Quit the System
______________________________________________""")
    m = str(input("Please enter the preferred option: ")).upper()
    if m == 'P':
        PurchaseMenu()
    elif m == 'V':
        SeatingModule()
        pass
    elif m == 'Q':
        print("Goodbye!")
        exit()
    else:
        print("\nInvalid Entry!")
        MainMenu()
    return m

#This Purchase Menu asks whether the user wants Business or Economy Class
def PurchaseMenu():
    print("""
            PURCHASING MODULE
______________________________________________
Please enter the preferred option:
B - to Purchase Ticket for Business Class
E - to Purchase Ticket for Economic Class
M - to Return to the Main Menu
______________________________________________""")
    cls = str(input("Please enter the preferred option: ")).upper()
    if cls == 'B':
        Business()
    elif cls == 'E':
        Economy()
    elif cls == 'M':
        MainMenu()
    else:
        print("\nInvalid Entry!")
        PurchaseMenu()
    return cls

#This function is used in Seating View for Efficiency
def InSeatingM():
    print("""
__________________________________
        BUSINESS CLASS
__________________________________""")
    for i in range(0, len(BCC), 5):
        print(BCC[i:i + 5])
    print("""
__________________________________
        ECONOMY  CLASS
__________________________________""")
    for i in range(0, len(ECC), 5):
        print(ECC[i:i + 5])
    print("Please note that if the seat number equals to '0' then the seat has been already booked")
    input("\n\nPress Enter to go back to Main Menu...")
    MainMenu()

#Seating View (Initiates when the user press V in the Main Menu)
def SeatingModule():
    global BCC
    global ECC
    print("""
            VIEW SEATING ARRANGEMENT
______________________________________________
""")
    viewm = input("""Please select the ferry you would like to view the seating arrangement:
    1. SC011 @ 10:00 AM from Penang to Langkawi
    2. SC013 @ 12:00 PM from Penang to Langkawi
    3. HC107 @ 02:00 PM from Penang to Langkawi
    4. HC109 @ 04:00 PM from Penang to Langkawi
    5. SC012 @ 11:00 AM from Langkawi to Penang
    6. SC014 @ 01:00 PM from Langkawi to Penang
    7. HC108 @ 03:00 PM from Langkawi to Penang
    8. HC110 @ 05:00 PM from Langkawi to Penang\n""")

    if viewm == "1":
        print("""
__________________________________
  Available seats for SC011 are:""")
        BCC = BC_seats_SC011
        ECC = EC_seats_SC011
        InSeatingM()
    elif viewm == "2":
        print("""
__________________________________
  Available seats for SC013 are:""")
        BCC = BC_seats_SC013
        ECC = EC_seats_SC013
        InSeatingM()
    elif viewm == "3":
        print("""
__________________________________
  Available seats for HC107 are:""")
        BCC = BC_seats_HC107
        ECC = EC_seats_HC107
        InSeatingM()
    elif viewm == "4":
        print("""
__________________________________
  Available seats for HC109 are:""")
        BCC = BC_seats_HC109
        ECC = EC_seats_HC109
        InSeatingM()
    elif viewm == "5":
        print("""
__________________________________
  Available seats for SC012 are:""")
        BCC = BC_seats_SC012
        ECC = EC_seats_SC012
        InSeatingM()
    elif viewm == "6":
        print("""
__________________________________
  Available seats for SC014 are:""")
        BCC = BC_seats_SC014
        ECC = EC_seats_SC014
        InSeatingM()
    elif viewm == "7":
        print("""
__________________________________
  Available seats for HC108 are:""")
        BCC = BC_seats_HC108
        ECC = EC_seats_HC108
        InSeatingM()
    elif viewm == "8":
        print("""
__________________________________
  Available seats for HC110 are:""")
        BCC = BC_seats_HC110
        ECC = EC_seats_HC110
        InSeatingM()
    else:
        print("Invalid Entry, redirecting you back to the Seating Module...")
        SeatingModule()

#This is the ticket or the receipt that prints after the user confirms their choice
#It also types all the booking information into a file
def TicketingModule():
    print("""
            TICKETING MODULE
______________________________________________
    Here is your ticket for your reference,
   please show the ticket when boarding the
                    ferry.
______________________________________________""")
    import datetime
    today = datetime.date.today()
    print("Date:", today)
    print("Name:", name1, name2)
    print("Destination:", destion)
    stir = 'Ferry ID: '
    if destion == 'Penang':
        spt = LPTime[int(time_ch) - 1].split(' @ ')
    else:
        spt = PLTime[int(time_ch) - 1].split(' @ ')
    for TID in spt:
        print(stir, end='')
        print(TID)
        stir = 'Departure Time: '
    print("Seat Number:", choice)
    if 'A' in choice or 'B' in choice:
        print("Class: Business")
    else:
        print("Class: Economy")
    print('\n\n                  NO REFUND'
          '\n______________________________________________')

    cfile = open("customerfile.txt", "a")
    cfile.write("\n_________________________________________\n")
    fname = 'First Name:' + str(name1)
    lname = 'Last Name:' + str(name2)
    des = 'Destination:' + str(destion)
    TOD = 'Time of Departure:' + str(TID)
    doy = 'Date: ' + str(today)
    seat = 'Seat No.:' + str(choice)
    cfile.write("\n")
    cfile.write(doy)
    cfile.write("\n")
    cfile.write(fname)
    cfile.write("\n")
    cfile.write(lname)
    cfile.write("\n")
    cfile.write(des)
    cfile.write("\n")
    cfile.write(TOD)
    cfile.write("\n")
    cfile.write(seat)
    cfile.write("\n_________________________________________\n")
    cfile.close()

#Initiates when the user presses B in the Main Menu
def Business():
    global typee
    typee = 'Business'
    namef()
    destionf()

#Initiates when the user presses E in the Main Menu
def Economy():
    global typee
    typee = 'Economy'
    namef()
    destionf()

#Accepts formal name from user (Only letters accepted, Auto Capitalization)
def namef():
    global name1
    global name2
    name1 = input("\nPlease enter your first name (No spaces): ").title()
    name2 = input("Last name: ").title()
    if not name1.isalpha() or not name2.isalpha():
        print("Inappropriate input!\n")
        namef()
    return

#Accepts the destination input
def destionf():
    global destion
    destion = input("""\nPlease enter the preferred destination:
                        P - Penang
                        L - Langkawi
--------->""").upper()
    if destion == 'P':
        destion = 'Penang'
        if typee == 'Business':
            time_penang_B()
        else:
            time_penang_E()
    elif destion == 'L':
        destion = 'Langkawi'
        if typee == 'Business':
            time_lank_B()
        else:
            time_lank_E()
    else:
        print("Invalid Entry!\n")
        destionf()
    return

#Asks the user for desired Departure Time
def time_penang_B():
    print("\nChoose departure time: (1-4)")
    global seating
    global alternate
    global time_ch
    num = 0
    for i in LPTime:
        num += 1
        print(num, end=". ")
        print(i)
    time_ch = input("--------->")
    print()
    if time_ch == '1':
        seating = BC_seats_SC012
        alternate = EC_seats_SC012
        seatf()
    elif time_ch == '2':
        seating = BC_seats_SC014
        alternate = EC_seats_SC014
        seatf()
    elif time_ch == '3':
        seating = BC_seats_HC108
        alternate = EC_seats_HC108
        seatf()
    elif time_ch == '4':
        seating = BC_seats_HC110
        alternate = EC_seats_HC110
        seatf()
    else:
        print("Invalid Entry!\n")
        time_penang_B()
    return


def time_lank_B():
    print("\nChoose departure time: (1-4)")
    global seating
    global alternate
    global time_ch
    num = 0
    for i in PLTime:
        num += 1
        print(num, end=". ")
        print(i)
    time_ch = input("--------->")
    print()
    if time_ch == '1':
        seating = BC_seats_SC011
        alternate = EC_seats_SC011
        seatf()
    elif time_ch == '2':
        seating = BC_seats_SC013
        alternate = EC_seats_SC013
        seatf()
    elif time_ch == '3':
        seating = BC_seats_HC107
        alternate = EC_seats_HC107
        seatf()
    elif time_ch == '4':
        seating = BC_seats_HC109
        alternate = EC_seats_HC109
        seatf()
    else:
        print("Invalid Entry!\n")
        time_lank_B()
    return


def time_penang_E():
    print("\nChoose departure time: (1-4)")
    global seating
    global alternate
    global time_ch
    num = 0
    for i in LPTime:
        num += 1
        print(num, end=". ")
        print(i)
    time_ch = input("--------->")
    print()
    if time_ch == '1':
        seating = EC_seats_SC012
        alternate = BC_seats_SC012
        seatf()
    elif time_ch == '2':
        seating = EC_seats_SC014
        alternate = BC_seats_SC014
        seatf()
    elif time_ch == '3':
        seating = EC_seats_HC108
        alternate = BC_seats_HC108
        seatf()
    elif time_ch == '4':
        seating = EC_seats_HC110
        alternate = BC_seats_HC110
        seatf()
    else:
        print("Invalid Entry!\n")
        time_penang_E()
    return


def time_lank_E():
    print("\nChoose departure time: (1-4)")
    global seating
    global alternate
    global time_ch
    num = 0
    for i in PLTime:
        num += 1
        print(num, end=". ")
        print(i)
    time_ch = input("--------->")
    print()
    if time_ch == '1':
        seating = EC_seats_SC011
        alternate = BC_seats_SC011
        seatf()
    elif time_ch == '2':
        seating = EC_seats_SC013
        alternate = BC_seats_SC013
        seatf()
    elif time_ch == '3':
        seating = EC_seats_HC107
        alternate = BC_seats_HC107
        seatf()
    elif time_ch == '4':
        seating = EC_seats_HC109
        alternate = BC_seats_HC109
        seatf()
    else:
        print("Invalid Entry!\n")
        time_lank_E()
    return

###This function accepts seat choice and initiates ticket print
def seatf():
    global choice
    global alternate
    global seating
    #This feature lets the user choose their desired seat
    for i in range(0, len(seating), 5):
        print(seating[i:i + 5])
    if len(seating) == 10:
        print("**You can type 'E' to be directed to the Economy Class**")
    else:
        print("**You can type 'B' to be directed to the Business Class**")
    choice = str(input("Choose your seat (For example:B2): ")).upper()
    if choice in seating:
        print("\nThis seat is available;")
        conf = input("Confirm? (Y/N) ").upper()
        if conf == "Y":
            seating[seating.index(choice)] = 0
            print(choice, 'is yours!')
            print("""\nThank you for using our service;
Safe travel, enjoy!""")
            input("\nPress Enter to preview your ticket...\n")
            TicketingModule()
            input("\n\nPress Enter to go back to Main Menu...")
            MainMenu()
        elif conf == "N":
            print("You are being directed back to the Purchase Menu\n")
            PurchaseMenu()
        else:
            print("Invalid Entry!")
            PurchaseMenu()
    #This transfers the user from Business to Economy or vice versa
    elif len(seating) == 10 and choice == 'E':
        seating = alternate
        print()
        seatf()
    elif len(seating) == 40 and choice == 'B':
        seating = alternate
        print()
        seatf()
    else:
        print("Invalid Entry!\nTry again!\n")
        seatf()
    return

#This initiates the program
MainMenu()
