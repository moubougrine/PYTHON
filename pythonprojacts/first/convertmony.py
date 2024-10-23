from pystyle import Box, Write, Colors
from forex_python.converter import CurrencyRates, RatesNotAvailableError

def main():
    print(Box.Lines('[+] Learn Python with Rakwan [+]'))
    Write.Print('This program converts money between currencies\n', Colors.blue_to_cyan, interval=0.1)
    print(Box.DoubleCube('Example [11]'))

    # Get user input
    while True:
        try:
            money = float(input("Please enter the amount you want to convert: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    cv_from = input("Source currency code (e.g., USD): ").upper()
    cv_to = input("Target currency code (e.g., EUR): ").upper()

    # Initialize the CurrencyRates object
    cr = CurrencyRates()

    # Convert the amount
    try:
        # Display the result
        print(f"\nConverting {money} {cv_from} to {cv_to}")
        output = cr.convert(cv_from, cv_to, money)
        print(f"The converted amount is: {output:.2f} {cv_to}")
    except RatesNotAvailableError:
        print(f"Error: Unable to fetch exchange rates for {cv_from} or {cv_to}.")
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

    # Wait for user input before exiting
    input("\nPress Enter to exit ...")

if __name__ == "__main__":
    main()