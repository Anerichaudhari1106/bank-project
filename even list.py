# Bank programme
class CreatAccount:
    def __init__(self):
        self.data = {}
        self.login = ''
        self.transactions = {}

    def creat_account(self):
        user_pin = int(input("Enter Your PIN:"))
        user_name = input("Enter your Name:")
        user_bls = int(input("Enter your Balance:"))
        self.data.update({user_pin: {"name": user_name, "balance": user_bls}})


    def show_Customer_data(self):
        print(f" Name               Pin             Balance")
        print("------------------------------------------------------")

        for pin, info in self.data.items():
            self.data.get(pin)['balance'] = sum(self.transactions.get(pin) if self.transactions.get(pin) else [0, 0])

            print(f" {info.get('name')}               {pin}             {info.get('balance')}")

        print("------------------------------------------------------------------")

    def exit(self):
        print("Thank you for Visting")

    def customer_login(self):
        customer_pin = int(input("ENTER YOUR PIN:"))
        if customer_pin in self.data:
            print("Welcome! You are logged in.")
            print("WELCOME", self.data.get(customer_pin).get("name"))
            self.login = customer_pin
            return True
        else:
            return False

    def transaction(self, transaction_type):
        if transaction_type != "transction":
            amount = int(input(f"enter your {transaction_type} amount:"))
        if transaction_type == "credit":
            self.transactions.setdefault(self.login, []).append(amount)


        elif transaction_type == "debit":
            self.transactions.setdefault(self.login, []).append(-amount)


        elif transaction_type == "transction":
            print(f"Transaction list for {self.data.get(self.login).get('name')}")
            print("---------------------------------------------------------------")

            for trans in self.transactions.get(self.login):
                if trans > 0:
                    print(f" creadit         {trans}")
                else:
                    print(f" debit            {(abs(trans))}")
            print("Total Balance:", sum(self.transactions[self.login]))


obj = CreatAccount()
print("=======WELCOME TO SBI=======")
print("-----------------------------")

while True:
    print("press 1:customer login\npress 2:manager login\npress 3:exit")
    user_input = int(input("enter your suggestion:"))

    if user_input == 1:
        c = obj.customer_login()
        if not c:
            print("WRONG PIN Number")
            continue

        while True:
            print("press-1:credit\npress-2:debit\npress-3:transction\npress 4: HOME\npress-5:exit")
            a = int(input("Enter your suggestion:"))
            if a == 1:
                obj.transaction("credit")
            elif a == 2:
                obj.transaction("debit")
            elif a == 3:
                obj.transaction("transction")
            elif a == 5:
                obj.exit()
                break
            elif a == 4:
                break

            else:
                print("wrong suggation")

    elif user_input == 2:

        while True:
            print("press-1: create Customer\npress-2:show Customer data\npress 4: HOME\npress 3: exit")
            user_input_1 = int(input("Enter your suggesion:"))
            if user_input_1 == 1:
                obj.creat_account()
            elif user_input_1 == 2:
                """ show customer data"""
                obj.show_Customer_data()

            elif user_input_1 == 3:
                obj.exit()
            elif user_input_1 == 4:
                break



    elif user_input == 3:
        obj.exit()
        break

    else:
        print("You are enter wrong input")
