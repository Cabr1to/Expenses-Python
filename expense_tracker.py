def main():
    print("Running Expense Tracker")

    # Input for expense
    get_user_expense()

    # Write expense to a file 
    save_expense_to_file()

    # Read file and summarize expenses
    summarize_expenses()



def get_user_expense():
    print("ok")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"{expense_name} R${expense_amount}")

    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc"
    ]

    while True:
        print("Select a category ")
        for i, category_name in enumerate(expense_categories):
            print(f"    {i+1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            break
        else:
            print("Invalid category. Please try again.")



def save_expense_to_file():
    print("ok")


def summarize_expenses():
    print("ok")


if __name__ == "__main__":
    main()