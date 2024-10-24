import pandas as pd
import csv
from datetime import datetime
from main import get_amount, get_category, get_date,get_description
import matplotlib.pyplot as plt


class CSV:
    CSV_file = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"] 
    Format = '%d-%m-%Y'

    @classmethod
    def m_csv(cls):
        try:
            pd.read_csv(cls.CSV_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_file, index=False)
            print(f"{cls.CSV_file} created with default columns.")

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully.")

    @classmethod
    def get_transaction(cls,start_date,end_date):
        df = pd.read_csv(cls.CSV_file)
        df["date"] = pd.to_datetime(df["date"],format=CSV.Format)
        start_date= datetime.strptime(start_date,CSV.Format)
        end_date= datetime.strptime(end_date,CSV.Format)
        mask = (df["date"]>=start_date) & (df["date"]<=end_date)
        filter_de = df.loc[mask]
        """  if filter_de.empty:
                print("No transactions found in the given date range ")
            else :
                print(f"Transaction from {start_date.strftime.CSV.Format} to {end_date.strftime(CSV.Format)}")
                print(filter_de.to_string(index=False, formatters={"date" : lambda x: x.strftime(CSV.Format)}))
                total_income = filter_de[filter_de["category" ]== "Income"].sum()
                total_expense =  filter_de[filter_de["category" ]== "Expense"].sum()
                print("\n Summary")
                print(f"Total Income :${total_income:.2f}")
                print(f"Total Expense :${total_expense:.2f}")
                print(f"Net Savings :${total_income - total_expense:.2f}")

            return filter_de
            """
        if filter_de.empty:
            print("No transactions found in the given date range.")
        else:
            print(f"Transactions from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
            print(filter_de.to_string(index=False, formatters={"date": lambda x: x.strftime('%Y-%m-%d')}))

            total_income = filter_de[filter_de["category"] == "Income"]["amount"].sum()  # Specify the column for summation
            total_expense = filter_de[filter_de["category"] == "Expense"]["amount"].sum()  # Specify the column for summation

            print("\nSummary")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${total_income - total_expense:.2f}")

        return filter_de

def N_plot(df):
    # Set the date as the index
    df.set_index("date", inplace=True)
    
    # Create a DataFrame for Income, resampled by day
    income_df = (
        df[df["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    
    # Create a DataFrame for Expense, resampled by day
    expense_df = (
        df[df["category"] == "Expense"]  # Corrected here
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expenses Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()



def add():    
    CSV.m_csv()
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter for today date :",
        allow_default=True)
    amount = get_amount()
    category = get_category()
    description =get_description()
    CSV.add_entry(date,amount,category,description)

    
def main():
    while True:
        print("\n1. Add a new transaction ")
        print("2. View transaction and summary within a date range")
        print("3.Exit")
        choice = input("Enter your choice (1-3) : ")
        if choice == "1":
            add()
        elif choice == "2" :
            start_date = get_date("Enter the start date (dd-mm-yyyy) : ")
            end_date = get_date("Enter the end date (dd-mm-yyyy) : ")
            df=CSV.get_transaction(start_date,end_date)
            if input("Do you want plot ? [Yes/Not] : ").strip().lower() == "Yes":
                N_plot(df)
        elif choice == "3" :
            print ("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1. 2 or 3.")

if __name__ == "__main__":
    main()
