import string
def inputs():
    
    '''These are the inputs for the program'''
    
    row = int(input("Enter number of rows: "))
    seats = int(input("Enter numbers of seats in each row: "))
    #sel_seat = input("Input seat number (row seat): ")
    return row, seats  

def make_rows(row, seats):
    
    '''This makes the big list with the seats'''
    
    big_list = []
    seat_list = [] 
    counter = 0
    char = list(string.ascii_uppercase)
    for i in range(0, seats):
        seat_list.append(char[counter])
        counter += 1
    for i in range(0, row):
        big_list.append(seat_list)
    return big_list

def select_seats(big_list):
    while True:
        selSeat = input("Input seat number (row seat): ")
        selSeatList = []
        for word in selSeat:
            selSeat.strip()
            if word == " ":
                continue
            selSeatList.append(word)
        
        row = int(selSeatList[0])
        seat = str(selSeatList[1])
        errcheck = False
        for rowl in range(len(big_list)):
            for i, iteml in enumerate(big_list[rowl]):
                if (row-1 == rowl) and (seat == iteml):
                    if big_list[rowl][i] == "X":
                        errcheck = True
                        print("That seat is taken!")
                    else:    
                        big_list[rowl][i] = "X"
                        return big_list
        if errcheck == False:
            print("Seat number is invalid!")
            
def printout(big_list):
    
    '''Prints everything'''
    
    print(big_list)

def main():
    row, seats = inputs()
    
    big_list = make_rows(row, seats)
    
    printout(big_list)
    
    select_seats(big_list)
    
    printout(big_list)
    
main()
