from methods import sirap as s

# Loop so the program dosen't close after every input
while True:  
    s.print_menu()
    answer = input()
    print("--------------------")
    print()
    match answer:
        case "0": # Convert csv to txt
            s.cnvrt_csv_to_txt()
            print()
            input("Press any key to continue..")
        case "1": # Prints all data in to a text table
            s.print_table(False)
            print()
            input("Press any key to continue..")
        case "2": # Function for adding a new bil
            s.add_bill()
            print()
            input("Press any key to continue..")
        case "3": # Prints the table with 'Order by date'
            s.print_table(True)
            print()
            input("Press any key to continue..")
        case "4": # Prints all the years where the total credited and total debited is listed
            s.printStatics()
            print()
            input("Press any key to continue..")
        case "5": # Print the heighst amount of bills in credit and debit
            s.highest_amount()
            print()
            input("Press any key to continue..")
        case "6": # Print the most common compnay
            s.most_common_company()
            print()
            input("Press any key to continue..")
        case "7": # Prints the average time between bills.
            s.avg_time()
            print()
            input("Press any key to continue..")
        case "8": # Prints the total number of bills.
            s.total_bills()
            print()
            input("Press any key to continue..")
        case "9": # Prints the average spent beetween two time periods
            s.avg_spent_date()
            print()
            input("Press any key to continue..")
        case "10": # Exit
            print("See you later!")
            break      
        case _:
            # The user has provieded an invalid input
            print("Could not recgonize '", answer, "', Please try again.")
    print()
    print("--------------------")
    print()