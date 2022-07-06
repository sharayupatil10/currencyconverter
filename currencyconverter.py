from requests import get
from pprint import PrettyPrinter

# URL of the website = "https://free.currencyconverterapi.com"

BASE_URL = "https://free.currconv.com/"
#This is the URL to which the request to fetch the data is being sent

API_KEY = "562ddaf40c95f5d58108"
#API key identifies the application or program making the call to an API.

printer = PrettyPrinter()
#This function allows us to format the data in a more readable way

#Function to get currencies from the URL
def get_currencies():
    
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    #endpoint is the location of the data of list of currencies from where it can be retrieved
    
    url = BASE_URL + endpoint
    
    data = get(url).json()['results']
    # sends a get request to the URL in order to retreive the results
    # data is returned by the URL in the form of JSON which in python is of the data type - dictionary
    
    data = list(data.items())
    # dictionary is converted into list data type
    
    data.sort()
    # the list of currencies is sorted
    
    return data
    # the sorted list of currencies will be returned
    
#Function to print the list of currencies    
def print_currencies(currencies):
    
    for name, currency in currencies:
        name = currency['currencyName']
        # storing name of the currency in variable 'name'
        
        _id = currency['id']
        # storing the currency code in variable '_id'
        
        symbol = currency.get("currencySymbol", "")
        # storing the symbol of currency in variable 'symbol'
        # if no symbol exists, then assign value of symbol = ""
        
        print(f"{name} -- {_id} -- {symbol}")
        # printing the data
        
#Function which returns the exchange rate of two currencies
def exchange_rate(currency1, currency2):
    
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    # location of the data of exchange rate of two currencies in the URL
    
    url = BASE_URL + endpoint
    
    data = get(url).json()
    # sends a get request to the URL in order to retreive the exchange rates
    # data is returned by the URL in the form of JSON which in python is of the data type - dictionary

    if len(data) == 0:
        print('No match found for the entered currencies.')
        return None

    rate = list(data.values())[0]
    # the dictionary is first converted to list
    # the 0th indexed data stores the exchange rate values of a currency pair
    # that value is accessed and being assigned to variable 'rate'
    
    print(f"1 {currency1} ---> {rate} {currency2}\n")

    return rate
    # returning the exchange rate of a currency pair
    
#Function which converts the entered amount from one currency to another
def convert(currency1, currency2, amount):
    
    rate = exchange_rate(currency1, currency2)
    # calling the exchange rate function and assigning its return value to variable 'rate'
    
    if rate is None:
        print("Please check the currency codes and enter again. ")
        return None
    
    amount = float(amount)
    # explicitly type casting amount to float data type
    
    converted_amount = (rate * amount)
    # calculating the equivalent amount in one currency to another
    
    print(f"{amount} {currency1} is equivalent to {converted_amount} {currency2}\n")
    
    return converted_amount
    # returns the equivalent converted amount
    
#Defining the main function which calls the above functions
def main():
    
    currencies = get_currencies()
    # calling the get_currencies function and storing its values in variable 'currencies'

    print("------------- WELCOME TO THE CURRENCY CONVERTER --------------")
    print("This currency converter tool calculates foreign exchange rates for all the major currencies worldwide to enable cross-border purchases.")
    print("\nIn order to list out the different currencies available, type in - List")
    print("\nIn order to get the exchange rate of two currencies, type in - Rate")
    print("\nIn order to convert the amount from one currency type to another, type in - Convert")
    print()

    while True:
        command = input("\nEnter the function to be performed ( Press q to quit): \n").lower()
       
        if command == "q":
            print("\nThankyou for using our services !!! ")
            break
            # coming out of the control structure
        
        elif command == "list":
            print_currencies(currencies)
            # calling the print currencies function 
            
        elif command == "rate":
            currency1 = input("\nEnter the code of the currency you wish to convert FROM : ").upper()
            currency2 = input("Enter the code of the currency you wish to convert TO : ").upper()
            exchange_rate(currency1, currency2)
            # calling the exchange rate function
            
        elif command == "convert":
            currency1 = input("\nEnter the code of the currency you wish to convert FROM : ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter the code of the currency you wish to convert TO : ").upper()
            convert(currency1, currency2, amount)
            # calling the convert function
        else:
            print("Invalid Command !!!")

main()
# calling the main functions