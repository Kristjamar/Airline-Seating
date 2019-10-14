const_list = []

def make_rows(row, seats):
    for i in range(0, row):
        row_list = ["A"]*seats
        const_list.append(row_list)
    return row_list

def printout(const_list, seats):
    print(const_list)

def main():
    row = int(input("Enter number of rows: "))
    seats = int(input("Enter numbers of seats in each row: "))
    
    row_list = make_rows(row, seats)
    
    printout(const_list,seats)
main()