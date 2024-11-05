class RewardsProgram:
    '''Stores customer information surrounding the Rewards program'''
    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email 

    def profile(self):
        print(f'Name: {self.cust_name}')
        print(f'Phone: {self.phone}')
        print(f'Email: {self.email}')

    def thank_you(self):
        print(f'Thank you, {self.cust_name}, for visiting our restaurant!')

    def add_to_cust_list(self):
        global cust_list
        cust_list.append((self.cust_name, self.phone, self.email))