#LAB2 Q2
def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f'{city}, {state}, {zip}')

display_mailing_label('Jacob Ridges', '1999 fvknfv court', 'Greenburg', 'California', '61129' )
display_mailing_label('Bob Ross', '1999 painting lane', 'London', 'England', '61192')

#LAB2 Q3
def add_numbers(*args):
    total = sum(args)
    addition_symbol = " + ".join(str(num) for num in args)
    print(f'{addition_symbol} = {total}')

add_numbers(1,3,5)         #there may be a way to do this differently
add_numbers(30,50,40,90)    
add_numbers(1)
add_numbers(1,2)

#LAB2 Q4
def display_receipt(total_due, amount_paid):
    change_due = amount_paid - total_due
    amount_short = total_due - amount_paid
    if total_due > amount_paid:
        print(f'Uh oh! Not enough!')
        return f'It seems you are ${round(amount_short,2)} short'
    print (f'Total due: ${round(total_due,2)}')
    print(f' Amount paid: ${round(amount_paid,2)}')
    print(f'Change due: ${round(change_due, 2)}')

display_receipt(30.37, 45.11)
display_receipt(49.99, 49.99)
print(display_receipt(42.32, 39.99))


