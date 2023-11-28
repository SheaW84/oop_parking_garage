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
            my_ticket = self.tickets.pop()
            self.currentTickets.update({my_ticket:False})
            self.parkingSpaces.pop()
            print(f'You have ticket number{my_ticket}')
        else:
            print("You're not parked here!")


    def payForParking(self):

        """
            payForParking() checks if payment is entered and then adds to tickets and 
            parkingSpaces list.
            Adds to both tickets and parkingSpaces list
            updates currentTickets key 'paid' to value True
        """
        ticket_no = input('\nPlease enter your ticket number: ')
        payment= input('\nPlease enter your payment of 0.50: ')
        if payment != '':
            print('\nPayment made. You have 15 minutes to leave')
            self.currentTickets.update({ticket_no:True})
       

    def leaveGarage(self):
            """
            leaveGarage() checks if currentTickets key 'paid' value is True changes
            it back to False if True and thanks the user. Adds to the tickets and
            parkingSpaces lists.Thanks the  user for payment. continues to ask user for 
            payment if currentTickets key 'paid' value is False
    
            """

            if self.currentTickets:
                ticket_no = input('Turn in your ticket: ')
                if self.currentTickets[ticket_no]:
                    print('\nThank You, have a nice day!')
                    self.tickets.append(ticket_no)
                    self.parkingSpaces.append(ticket_no)
                    del self.currentTickets[ticket_no]
                else:
                    self.payForParking()
                    

    def showSpaces(self):
            print('Current occupied spaces: ', len(self.parkingSpaces))

    def showTickets(self):
            print('Current tickets: ', len(self.tickets))

    def run(self):

            while not my_garage.currentTickets or my_garage.currentTickets:
    
                print('\nWelcome to Gotham Downtown Parking Garage!')
                guest = input("\nAre you parking or leaving? Type 'parking','paying','leaving' or 'quit' to quit: ")
                if guest.lower() == 'parking':
                    my_garage.takeTicket()
                elif guest.lower() == 'paying':
                    my_garage.payForParking()                
                elif guest.lower() =='leaving':
                    my_garage.leaveGarage()
                elif guest.lower() == 'showt':
                    my_garage.showTickets()
                elif guest.lower() == 'shows':
                    my_garage.showSpaces()
                elif guest.lower() =='quit':
                    break
                else:
                     print('Please choose from the menu!')
                continue  

my_garage = ParkingGarage(['1','2','3','4'],['1','2','3','4'],{})
my_garage.run()


    