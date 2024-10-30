class Tea:
    '''varieties of tea for my tea shop'''

    def __init__(self, name, type, allergen = 'none'):
        self.name = name
        self.type = type 
        self.allergen = allergen
        self.instock = 'y'
        self.looseleaf = 'y'
        
    def brew(self):
        print(f'How about a nice cup of {self.name}?')
        print(f'Please collect your tea from the counter.')

class BlackTea(Tea):
    '''varieties of black tea'''
    def __init__(self, name, allergen, strength, caffeinated = 'y'):
        super().__init__(name, allergen)
        self.strength = strength
        self.caffeinated = caffeinated
    
bl_asm = BlackTea('Assam', 'none', 'full-bodied')

print(f'''
{bl_asm.name}
{bl_asm.allergen}
{bl_asm.strength}
{bl_asm.caffeinated}      
''')

# gr_jas = Tea('jasmine green tea', 'green')
# oo_peo = Tea('white peony oolong', 'oolong')
# bl_alm = Tea('almond darjeeling', 'black', 'tree nut')

# print(gr_jas.name, gr_jas.looseleaf)
# print(oo_peo.name, oo_peo.looseleaf)
# print(bl_alm.name, bl_alm.looseleaf)

# print(f'Can I have a cup of {gr_jas.name}?')
# oo_peo.brew()
