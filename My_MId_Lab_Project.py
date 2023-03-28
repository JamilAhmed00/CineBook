


"""Maker: Jamil Ahmed"""


class Star_Cinema:
    #hall_list = []
    #show_list = []

    def entry_hall(self,Hall):
        self.hall_list.append(Hall)


class Hall(Star_Cinema):

    
    def __init__(self, rows, cols,hall_no):

        self.__seat = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        

        

    def entry_show(self,id, movie_name, time):

        self.id = id
        self.movie_name = movie_name
        self.time = time
        show = []
        
        show.append(id)
        show.append(movie_name)
        show.append(time)
        
        self.__show_list.append(show)
        self.show_seat = [['A' for j in range(self.__cols)] for i in range(self.__rows)]
        self.__seat[id] = self.show_seat


    


    def book_seat(self,name,phone_number,id,row,col):
        

        for i in self.__seat:
            if i == id:
                if self.__seat[id][row][col] == 'A':
                    self.__seat[id][row][col] = 'x'
                    return f'Ticket Booked Ticket No: {row} {col}\n'
                
                else:
                    return 'Already Booked. Pleaee Try Another One.\n'

        
        if row > self.__rows or col > self.__cols: 
            return 'Invalid Row or Colom.\n'
        else:
            return 'Invalid Movie ID'

        
    

    def view_show_list(self):
        for i in self.__show_list:
            print(f'{i}\n')


    def view_available_seat(self, id):
        if id in self.__seat:
            for i in self.__seat[id]:
                #print(self.seat[id])
                print(f'{i}\n')
        else:
            print("Invalid Show ID.\n")





hall1 = Hall(5,5,1)
hall1.entry_show('1234','Nishaartho Valobasha','Time: 23/04/2023')
hall1.entry_show('23456','Sakib Khan Number 1','Time: 22/04/2023')



while True:

    print('Please Choice Your Option:\n1. View All Shows.\n2. View Availabe Seats.\n3. Book Ticket.\n4. Quit\n\n')

    x = int(input())
    if x==4:
        break
    
    elif x==1:
        hall1.view_show_list()

    elif x==2:
        print('Please Give the Movie ID: \n\n')
        y = input()
        hall1.view_available_seat(y)
        
    
    elif x==3:
        print('Please Give Your Name, Mobile Number, Movie ID, Row No, Col No: \n\n')
        name = input()
        mobile = input()
        ID = input()
        row = int(input())
        col = int(input())
        print(hall1.book_seat(name,mobile,ID,row,col))








