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
    char = list(string.ascii_uppercase)
    
    for _ in range(0, row):
        for i in range(0, seats):
            seat_list.append(char[i])
        big_list.append(seat_list)
        seat_list = [] 
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
                if (row-1 == rowl) and ((seat == iteml) or (iteml == "X")):
                    if big_list[rowl][i] == "X":
                        errcheck = True
                        print("That seat is taken!")
                    else:
                        big_list[rowl][i] = "X"
                        return big_list

        if errcheck == False:
            print("Seat number is invalid!")


def again():
    ans = input("More seats (y/n)? ")
    if ans == "y":
        return True
    else:
        return False

            
def printout(big_list):
    
    '''Prints everything'''
    
    for i in range(1,len(big_list)+1):
        print("{:>2}{:>3}".format(i," "),end="")
        for j in range(0,len(big_list[i-1])):
            if j == (len(big_list[i-1])/2):
                print(" ",end="")
            print("{:>2}".format(str(big_list[i-1][j])),end="")
        print("")
        

def main():
    moreseats = True

    row, seats = inputs()
    
    big_list = make_rows(row, seats)
    
    printout(big_list)
    
    while moreseats:
        select_seats(big_list)
        printout(big_list)
        moreseats = again()

    
main()
