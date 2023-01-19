import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('client_database')

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)

def get_sales_data():
  """
  Get sales figures input the user
  """
  print("Please enter sales data from the last market.")
  print("Data should de six numbers, separated by commas.")
  print("Example: 10,20,30,40,50,60\n")

  data_str = input("Enter your data here: ")
  print(f"The data provided is {data_str}")

get_sales_data()




print("ATM Banking\n\nInsert your card")


password=1234
balance=50000
choice=0
chances = 3

is_on = True
while is_on:

  logo = (
        """
        WW            WW EEEEEE   LL      CCCC      OOOO    MM    MM EEEEEE
         WW     W    WW  EE       LL     CC  CC   OO    OO  MMM  MMM EE
          WW  W  W  WW   EEEE     LL    CC       OO      OO MM MM MM EEEE  
           WW      WW    EE       LL     CC  CC   OO    OO  MM    MM EE
            W      W     EEEEEEE  LLLLLL  CCCC      OOOO    MM    MM EEEEEEE
        """      
  )
  print(logo)
  
  pin = int(input("\nPlease enter the Four digit pin : "))
  if pin != password :
    chances -=1
    print("Wrong pin number!!\nPlease enter your Four digit pin number.")
    print(f"You have {chances} chances left")
    if chances == 0:
      print("Wrong pin number!!\nPlease insert your card again and enter your Four digit pin number.")
      is_on = False
  else:
    while choice != 4:
      print("\n\n**** Menu ****")
      print("1 == balance")
      print("2 == deposit")
      print("3 == withdtraw")
      print("4 == cancel\n")
  
      choice=int(input("\nEnter your option:\n"))
  
      if choice==1:
        print("Balance = $", balance)
  
      elif choice==2:
        deposit=int(input("Enter your deposit: $"))
        balance += deposit
        print("\ndeposit amount: $", deposit)
        print("balance = $", balance)
  
      elif choice==3:
        withdraw=int(input("Enter the amount to withdraw: $"))
        balance -= withdraw
        print("\nwithdrawn amount: $", withdraw)
        print("balance = $", balance)
  
      elif choice==4:
        print("\nSession Ended!! Do not forget your card! Goodbye!")
        is_on = False
        
      else:
        print("\nInvalid Entry!!!")



    
