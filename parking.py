class ParkingGarage ():

    def __init__(self, tickets, parkingSpaces,currentTickets):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTickets = currentTickets

    def takeTicket(self):
    
        """
            taketicket() checks if ticket list is empty then removes objects from both the 
            ticket and parkingSpaces list. 
            Says bye to the user
            Informs the user that they aren't parked there if there are no tickets
        """
    
        if len(self.tickets) != 0:
            self.tickets.pop()
            self.parkingSpaces.pop()
            print('Have a nice day. Come back soon!')
        else:
            print("You're not parked here!")


    def payForParking(self):

        """
            payForParking() checks if payment is entered and then adds to tickets and 
            parkingSpaces list.
            Adds to both tickets and parkingSpaces list
            updates currentTickets key 'paid' to value True
        """
    
        payment= input('\nPlease enter your payment of 0.50: ')
        if payment != '':
            print('\nPayment made. You have 15 minutes to leave')
            self.currentTickets.update({'paid':True})
            self.tickets.append(payment)
            self.parkingSpaces.append(payment)

    def leaveGarage(self):
            """
            leaveGarage() checks if currentTickets key 'paid' value is True changes
            it back to False if True and thanks the user. Adds to the tickets and
            parkingSpaces lists.Thanks the  user for payment. continues to ask user for 
            payment if currentTickets key 'paid' value is False
    
            """
            if self.currentTickets:
                self.currentTickets.update({'paid':False})
                print('\nThank You, have a nice day!')
            else:
                payment=input('\nPlease enter your payment of 0.50: ')
                if payment != '':
                    print('\nPayment made. You have 15 minutes to leave')
                    self.currentTickets.update({'paid':True})
                    self.tickets.append(payment)
                    self.parkingSpaces.append(payment)

    def showSpaces(self):
            print('Current occupied spaces: ', len(self.parkingSpaces))

    def showTickets(self):
            print('Current tickets: ', len(self.tickets))

    def run(self):

            while not my_garage.currentTickets or my_garage.currentTickets:
    
                print('\nWelcome to Gotham Downtown Parking Garage!')
                guest = input("\nAre you parking or leaving? Type 'parking','leaving' or 'quit' to quit: ")
                if guest.lower() == 'parking':
                    my_garage.payForParking()
                    my_garage.leaveGarage()
                elif guest.lower() =='leaving':
                    my_garage.takeTicket()
                elif guest.lower() == 'showt':
                    my_garage.showTickets()
                elif guest.lower() == 'shows':
                    my_garage.showSpaces()
                elif guest.lower() =='quit':
                    break
                else:
                     print('Please choose from the menu!')
                continue  

my_garage = ParkingGarage([],[],{})
my_garage.run()


    