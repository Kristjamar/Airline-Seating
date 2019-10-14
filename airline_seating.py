import string
def inputs():
    
    ''' These are the inputs for the number of rows and seats '''
    
    row = int(input("Enter number of rows: "))
    seats = int(input("Enter number of seats in each row: "))
    #sel_seat = input("Input seat number (row seat): ")
    return row, seats  


def make_rows(row, seats):
    
    ''' A function that creates the list of seats and rows '''
    
    big_list = []
    seat_list = [] 
    char = list(string.ascii_uppercase) # The ascii characters that tell us what character should be assigned next. 
    
    for _ in range(0, row):
        for i in range(0, seats):
            seat_list.append(char[i])
        big_list.append(seat_list)
        seat_list = [] 
    return big_list


def select_seats(big_list):
    
    ''' 
        This function allows the user to select seats and handles
        any errors that might occur.
    '''

    while True:
        selSeat = input("Input seat number (row seat): ")
        selSeatList = []
        digit = ""
        alpha = ""
        for word in selSeat:
            #Creating a list of the choices for the user
            selSeat.strip()
            if word.isdigit():
                digit += word
            if word == " ":
                continue
            else:
                alpha = word
        selSeatList.append(digit)
        selSeatList.append(alpha)
        
        try: # Error handling so if the user enters anything other than integer or string, it displays a message
            row = int(selSeatList[0])
            seat = str(selSeatList[1])
        except:
            print("Seat number is invalid!")
            continue

        errcheck = False
        for rowl in range(len(big_list)): # This replaces a given seat with "X"
            for i, iteml in enumerate(big_list[rowl]):
                if (row-1 == rowl) and ((seat == iteml) or (iteml == "X")):
                    if big_list[rowl][i] == seat:
                        big_list[rowl][i] = "X"
                        return big_list
                    else:
                        errcheck = True
        if errcheck:
            print("That seat is taken!")

        if errcheck == False:
            print("Seat number is invalid!")


def again(big_list):

    ''' Checks if the user wants to book another seat '''

    notfull = True # A checker for if all the seats on the plane are taken
    for sublist in big_list:
        for ele in sublist:
            if ele != "X":
                notfull = False
                break

    if notfull == True:
        return False

    ans = input("More seats (y/n)? ")
    if ans == "y":
        return True
    else:
        return False

            
def printout(big_list):
    
    '''Prints all seats and rows'''
    
    for i in range(1,len(big_list)+1):
        print("{:>2}{:>3}".format(i," "),end="")
        for j in range(0,len(big_list[i-1])):
            if j == (len(big_list[i-1])/2):
                print("  ",end="")
            print("{}".format(str(big_list[i-1][j])),end=" ")
        print("")
        

def main():
    moreseats = True

    row, seats = inputs()
    
    big_list = make_rows(row, seats)
    
    printout(big_list)
    
    while moreseats:
        select_seats(big_list)
        printout(big_list)
        moreseats = again(big_list)

    
main()
