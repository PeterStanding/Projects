# https://inventwithpython.com/bigbookpython/project53.html

import csv, sys, re

# Read all data from the CSV File
elementsFile = open(r'Periodic_Table\periodic_table.csv', encoding='utf-8')
elementsCSVReader = csv.reader(elementsFile)
elements = list(elementsCSVReader)
elementsFile.close()

columns = [ 'Atomic Number', 'Symbol', 'Element', 'Origin of name',
            'Group', 'Period', 'Atomic weight', 'Density',
            'Melting point', 'Boiling point',
            'Specific heat capacity', 'Electronegativity',
            'Abundance in earth\'s crust']

# Need to find the longest string in the Columns List
longest_column = 0
for key in columns:
    if len(key) > longest_column:
        longest_column = len(key)

# Put all the elements data into a data structure
ELEMENTS = {}
for line in elements:
    element = {
        'Atomic Number':  line[0],
        'Symbol':         line[1],
        'Element':        line[2],
        'Origin of name': line[3],
        'Group':          line[4],
        'Period':         line[5],
        'Atomic weight':  line[6] + ' u', # atomic mass unit
        'Density':        line[7] + ' g/cm^3', # grams/cubic cm
        'Melting point':  line[8] + ' K', # kelvin
        'Boiling point':  line[9] + ' K', # kelvin
        'Specific heat capacity':      line[10] + ' J/(g*K)',
        'Electronegativity':           line[11],
        'Abundance in earth\'s crust': line[12] + ' mg/kg'}
    
    for key, value in element.items():
        # Remove the [roman numeral] text
        element[key] = re.sub(r'\[(I|V|X)+\]', '', value)
    
    ELEMENTS[line[0]] = element # Map the Atomic Number to the element
    ELEMENTS[line[1]] = element # Map the Symbol to the element

print('Periodic Table of Elements')
print('By Al Sweigart al@inventwithpython.com')
print()

while True:
    # Shows the Table and lets User Select an Element
    print('''            Periodic Table of Elements
      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og
        
            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
    
    print('Enter a Symbol or Atomic Number to examine, or QUIT to exit')
    response = input('> ').title()

    if response == 'Quit':
        print('QUITTING')
        sys.exit()
    
    # Display the selected Data
    if response in ELEMENTS:
        for key in columns:
            keyJust = key.rjust(longest_column)
            print(keyJust+": " + ELEMENTS[response][key])
        input('Press Enter to continue...')