class Home:
    def __init__(self):
        self.data = {}
        self.login = []

    def home(self):
        print("press 1:customer login\npress 2:manager login\npress 3:exit")
        user_input = int(input("enter your suggestion:"))
        if user_input == 1:
            self.customer_page()

        elif user_input == 2:
            self.manager_home_page()
        elif user_input == 3:
            self.exit()

    def transaction(self, transaction_type):
        if transaction_type == "credit":
            amount = int(input(f"enter your {transaction_type} amount:"))
            if not self.data.get(self.login).get("transaction"):
                self.data.get(self.login).update({'transaction': [amount]})
            else:
                self.data.get(self.login).get('transaction').append(amount)
            print(self.data)


        elif transaction_type == "debit":

            amount = int(input(f"enter your {transaction_type} amount:"))
            if not self.data.get(self.login).get('transaction'):
                self.data.get(self.login).update({'transaction': [-(amount)]})
            else:
                self.data.get(self.login).get('transaction').append(-amount)
            print(self.data)
        elif transaction_type== "transction":
            print(f"Transcation list for {self.data.get(self.login).get('name')}")
            print("---------------------------------------------------------------")
            for trans in self.data.get(self.login).get("transaction"):
                if trans > 0:
                    print(f" creadit         {trans}")
                else:
                    print(f" debit           {abs(trans)}")
            print("---------------------------------------------------------------")
            print(f" TOTAL           {sum(self.data.get(self.login).get('transaction'))}")
            print("---------------------------------------------------------------")


    def customer_page(self):
        if not self.login:
            user_pin = int(input("Enter Your PIN:"))
            if user_pin in self.data:
                self.login = user_pin
                print(f"WELCOME {self.data.get(self.login).get('name')}YOU ARE LOGIN")
            else:
                print("wrong pin")
                self.customer_page()
        print("press-1:credit\npress-2:debit\npress-3:transction\npress 4: HOME\npress-5:exit")
        a = int(input("Enter your suggestion:"))
        if a == 1:
            self.transaction("credit")
            self.customer_page()
        elif a == 2:
            self.transaction("debit")
            self.customer_page()
        elif a == 3:
            self.transaction("transction")
            self.customer_page()
        elif a == 4:
            self.home()
        elif a == 5:
            self.exit()
        else:
            print("wrong input")

    def manager_home_page(self):
        print("press-1: create Customer\npress-2:show Customer data\npress 3: HOME\npress 4: exit")
        user_input_1 = int(input("Enter your suggesion:"))
        if user_input_1 == 1:
            self.create_customer()
            self.manager_home_page()
        elif user_input_1 == 2:
            self.show_Customer_data()
            self.manager_home_page()
        elif user_input_1 == 3:
            self.home()
            self.manager_home_page()
        elif user_input_1 == 4:
            self.exit()

    def create_customer(self):
        user_pin = int(input("Enter Your PIN:"))
        user_name = input("Enter your Name:")
        user_bls = int(input("Enter your Balance:"))

        self.data.update({user_pin: {"name": user_name, "balance": user_bls}})
        print(self.data)

    def show_Customer_data(self):
        print(f" Name        pin              balance")
        print("--------------------------------------------------")
        for pin, data in self.data.items():

            print(f"{data.get('name')}           {pin}        {data.get('balance')}")

    def exit(self):
        print("Thank you for visiting!")


obj = Home()
user_input = obj.home()
