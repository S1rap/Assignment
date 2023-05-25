import csv
from os import read
import click
from csv import writer
from datetime import date, datetime
from tabulate import tabulate



def get_table():
         # Opens the file and loop through the values seperated by coma
        with open("customerdata.csv",'r') as f:
            rowReader = csv.reader(f, delimiter=',')
            table = [] # Table for 'tabulate' to make better design
            for values in rowReader:
                column = (
                    values[0],
                    values[1],
                    values[2] 
                    + '-'
                    + values[3] 
                    + '-'
                    + values[4],
                    values[5],
                    values[6])
                table.append(column)
            return table


class sirap:

    def print_table(Sort):
            table = get_table()
            # Sorting by date   
            if Sort == True:
                table = sorted(table, key=lambda x: x[2])
            
            print(tabulate(table, headers=[
                'Company',
                'Name',
                'Date',
                'Amount',
                'Card'],
                tablefmt='github'))
    
    def avg_time():
        table = get_table()
        dates = [] 
        for item in table:
            split = item[2].split("-")
            dt = datetime(int(split[0]),int(split[1]),int(split[2]))
            dates.append(dt)
       
        avgTime=datetime.strftime(datetime.fromtimestamp(sum(map(datetime.timestamp,dates))/len(dates)),"%d")
        print("The average time between bills is", avgTime, "days")

    def avg_spent_date():
        table = get_table()
        dates = [] 
        for item in table:
            dates.append(item[2])

        print("Format [YYYY-MM-DD]")
        start_date = ""
        end_date = ""
        
        # Cheking the datetime is correct format
        try:
            start_date =datetime.strptime(input("From: "), '%Y-%m-%d')
            end_date = datetime.strptime(input("To: "), '%Y-%m-%d')
        except ValueError:
            # Failed
            print("Please use date format [YYYY-MM-DD]")
            return

        
        dt_dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]
        in_between_dates = []
        for d in dt_dates:
            if d >= start_date and d <= end_date:
                in_between_dates.append(d)

        beetween_dt = [d.strftime('%Y-%m-%d') for d in in_between_dates]
        total_amount = []
        for item in table:
            if item[2] in beetween_dt:
                total_amount.append(float(item[3]))
        if len(total_amount) != 0:
            value = sum(total_amount) / len(total_amount) 
        else:
            value = 0       
        print("The average spent from", start_date.date(), "to", end_date.date(), "is", value)


    def total_bills():
        file = open("customerdata.csv")
        reader = csv.reader(file)
        lines= len(list(reader))
        print("The total number of bills is:", lines)
        
    def cnvrt_csv_to_txt():
        
        print("[1] CSV To Text file [2] Text to CSV file" )
        answer = input(":")
        if answer == "1":

            read_file = r'customerdata.csv'
            write_file  =  input("Filename (wihtout .txt) :") + ".txt"
        elif answer == "2":
             read_file = input("Filename (wihtout .txt) :") + ".txt"
             write_file  =  r'customerdata.csv'
        else:
            print("Invalid input")
            return

        try:
            with open(read_file, 'r') as inp, open(write_file, 'w') as out:
                for line in inp:
                    out.write(line)
            print("Converted", read_file, "to", write_file)         
        except IOError:
            print("File does not exist")   
    def add_bill():
        print("Please provide following information")
        
        Colums = ['Company','Name', 'Date[YYYY-MM-DD]', 'Amount', 'Card']
        Data = []
        for colum in Colums:
            Data.append(input((colum + ": ")))

        # Cheking that date is correct format
        date_string = Data[2]
        y = date_string.split("-")[0]
        m = date_string.split("-")[1]
        d = date_string.split("-")[2]
        try:
            datetime(int(y), int(m), int(d))
        except ValueError:
            # Failed
            print("Please use date format [YYYY-MM-DD]")
            return
        
        # Converting Date format to seperat colums
        DateItem = Data[2].split("-")
        Data.pop(2)
        # Will loop through 3 values(year,month,day) and 
        # insert them the same order as the table colum
        for item in DateItem:
            Data.insert(len(Data) - 2, item)

        # Cheking that 'name' not contains
        # more than 1 Spaces
        name = Data[1]
        count = 0
        for n in name:
            if n.isspace() == True:
                count+=1
        if count > 1: 
            print("Please do only use one surname and lastname")
            return
        
        print(Data)
        if click.confirm('Add new to file?', default=True):
             with open('customerdata.csv', 'a+', newline='') as write_obj:
                # Create a writer object from csv module
                csv_writer = writer(write_obj)
                # Add contents of list as last row in the csv file
                #csv_writer.writerow("")
                csv_writer.writerow(Data)
                print("Successfully added your data")

    def print_menu():
        print("Billing manager v1.0")   
        print("""
[0] Convert 
[1] Print table
[2] Add bill
[3] Sort table by Date
[4] Stastics
[5] Highest amount
[6] Most common company
[7] Average time between bills
[8] Total number of bills
[9] The average spent beetween two time periods
[10] Exit
Please, select a function
        """)
    
    def highest_amount():
        table = get_table()
        Credit = []
        Debit = []

        for item in table:
            if item[4] == "credit":
                Credit.append(float(item[3]))
            elif item[4] == "debit":
                Debit.append(float(item[3])) 
        print("Your heighest credit bil was:", max(Credit), "and the heighest debit was:", max(Debit))    
        

    def most_common_company():
        
        table = get_table()
        Companys = []
        
        for item in table:
            Companys.append(item[0])

        print('The most common company is:', max(Companys))        

    def printStatics():
        
        table = get_table()
        years = [] # Getting the total amount of distinct year

        for item in table:
            years.append(item[2].split("-")[0])
        
        # Removeing all non-unique years
        distinct_years = set(years)
        # Creating a list with the relevent date
        st = []
        
        for item in distinct_years:
            arg = {'Year' : item, 'Credit': 0, 'Debit': 0}
            st.append(arg)

        for item in table:
            year = item[2].split("-")[0]
            Amount = float(item[3])
            if item[4] == "credit":
                index = st.index(next(filter(lambda n: n.get('Year') == year, st)))
                newAmout = float(st[index]['Credit']) + Amount
                st[index]['Credit'] = newAmout

            elif item[4] == "debit":
                index = st.index(next(filter(lambda n: n.get('Year') == year, st)))
                newAmout = float(st[index]['Debit']) + Amount
                st[index]['Debit'] = newAmout
        
        # Order by date
        st = sorted(st, key = lambda i: i['Year'])
        
        # Printing a table
        header = st[0].keys()
        rows =  [x.values() for x in st]
        print (tabulate(rows, header, tablefmt='github'))