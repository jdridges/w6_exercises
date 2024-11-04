#created social security tax, medicare tax and federal tax functions given the parameters listed for each
#asked to return tax amount for each given the following 3 people:
#person 1: gross pay $750, witholding code 0
#person 2: gross pay $1550, witholding code 2
#person 3: gross pay $1100, witholding code 5


def get_soc_sec_tax(gross_pay):
    tax_rate = .062
    soc_sec_tax = gross_pay * tax_rate
    return f' The total social security taxes payed with a gross pay of ${gross_pay} is ${round(soc_sec_tax, 2)}'

print(get_soc_sec_tax(750.00))
print(get_soc_sec_tax(1550.00))
print(get_soc_sec_tax(1100))

def get_medicare_tax(gross_pay):
    tax_rate = .0145
    medicare_tax = gross_pay * tax_rate
    return f' The total medicare taxes payed with a gross pay of ${gross_pay} is: ${round(medicare_tax, 2)}'
print(get_medicare_tax(750.00))
print(get_medicare_tax(1550.00))
print(get_medicare_tax(1100.00))

def get_federal_tax(gross_pay, witholding_code):
    if witholding_code == 0:
        tax_rate = .23
    elif witholding_code == 1:
        tax_rate = .21
    elif witholding_code == 2:
        tax_rate = .195
    elif witholding_code == 3:
        tax_rate = .185
    else:
        tax_rate = .18 - ((witholding_code - 4) * .005)

    federal_tax = gross_pay *tax_rate
    return f' The total federal taxes payed with a gross pay of ${gross_pay} and a witholding code of {witholding_code} is: ${round(federal_tax, 2)}'
print(get_federal_tax(750.00, 0))
print(get_federal_tax(1550.00, 2))
print(get_federal_tax(1100.00, 5))