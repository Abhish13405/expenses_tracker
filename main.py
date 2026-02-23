import os
import datetime


def initialize_file():
    if not os.path.exists('expenses.txt'):
        with open('expenses.txt','w') as file:
            file.write('Date,Amount,Category,Description\n')




def add_expense(date, amount, category, description):
    with open('expenses.txt','a') as file:
        file.write(f'{date},{amount},{category},{description}\n')
    print('Expense added.')




# def add_expense(date, amount, category, description):
#     with open('expenses.txt','a') as file:
#         file.write(f'{date},{amount},{category},{description}')
        
#     print('Expense added.')

def view_expenses():
    with open('expenses.txt','r') as file:
        lines = file.readlines()
        print(lines[0].strip())
        for line in lines[1:]:
            print(line.strip())

def filter_expenses(filter_by, filter_value):
    with open('expenses.txt','r') as file:
        lines = file.readlines()
        print(lines[0].strip())
        for line in lines[1:]:
            data = line.strip().split(',')
            if filter_by == 'date' and filter_value == data[0]:
                print(line.strip())
            elif filter_by == 'category' and filter_value == data[2]:
                print(line.strip())

def delete_expense(date, amount, category, description):
    with open('expenses.txt','r') as file:
        lines = file.readlines()
    with open('expenses.txt','w') as file:
        for line in lines:
            if line.strip() != f'{date},{amount},{category},{description}':
                file.write(line)
    print('Expense deleted.')

def monthly_summary():
    
    # def add_expense(date, amount, category, description):
    # with open('expenses.txt','a') as file:
    #     file.write(f'{date},{amount},{category},{description}\n')
    # print('Expense added.')

    current_month = datetime.datetime.now().strftime('%Y-%m')
    total_expense = 0.0
    category_expense = {}
    with open('expenses.txt','r') as file:
        lines = file.readlines()
    for line in lines[1:]:
        data = line.strip().split(',')
        if data[0].startswith(current_month):
            amount = float(data[1])
            category = data[2]
            total_expense += amount
            if category in category_expense:
                category_expense[category] += amount
            else:
                category_expense[category] = amount
    print(f'Total expense for {current_month}: {total_expense}')
    for cat, amt in category_expense.items():
        print(f'{cat}: {amt}')

def main():
    initialize_file()
    while True:
        print("--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses (by date/category)")
        print("4. Delete Expense")
        print("5. Monthly Summary")
        print("6. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            date = input("Enter date (yyyy-mm-dd): ")
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(date, amount, category, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_by = input("Filter by (date/category): ")
            filter_val = input(f"Enter {filter_by}: ")
            filter_expenses(filter_by, filter_val)
        elif choice == '4':
            date = input("Enter date (yyyy-mm-dd): ")
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            delete_expense(date, amount, category, description)
        elif choice == '5':
            monthly_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

# if __name__ == '_main_':
#     main()
if __name__ == '__main__':
    main()
