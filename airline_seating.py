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

def select_seats():
    selSeat = input("Input seat number (row seat): ")
    des = []
    for word in selSeat:
        selSeat.split()
        des.append(word)
    des.remove(des[1])
    return des

def printout(big_list, seats):
    
    '''Prints everything'''
    
    print(big_list, seats)

def main():
    row, seats = inputs()
    
    big_list = make_rows(row, seats)
    
    printout(big_list, seats)
main()