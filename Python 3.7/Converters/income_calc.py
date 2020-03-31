"""
Date: 3/31/2020
Version: Py 3.7
Owner: anemiaxb
Author:anemiaxb
Rationale: Simple income calculator for hourly workers. Adam has pre and post tax deductions whereas Sarah does not, but has shift differential
rate and pay. Both users have an OT rate and it is usually your hourly_rate * 1.5 or 2.0.

Switch out names,variable ,and variableNames with your own information.
"""

users = ['A', 'S']  # Place user names' first initials in  users list
user = None

while user not in users:
    user = input('(A)dam or (S)ara?: ').title().strip() # Replace names here with sa(m)e format

    if user == 'A':
        hours_Adam = float(input('Total hours: '))
        otHours = float(input('OT Hours: '))

        rate = # Your rate
        taxRateAdam = # Your tax rate
        otRate = # Your OT rate(hourly,NOT multiplier)
        preTax = # Your pre-tax amount
        postTax = # Your post-tax amount

        gross_Adam = ((rate * hours_Adam) + (otRate * otHours)).__round__(2)
        preTax_total = (gross_Adam - preTax).__round__(2)
        taxTotal = (preTax_total * taxRateAdam).__round__(2)
        beforePostTax = (preTax_total - taxTotal).__round__(2)
        postTax_total = (beforePostTax - postTax).__round__(2)
        print()

        print('____________________________________________________')
        print('| Hours |    Gross    |    Taxes   |     Net       |')
        print('|-------|-------------|------------|---------------|')
        print(f"| {hours_Adam}  |   ${gross_Adam}   |   ${taxTotal}  |   ${postTax_total}    |")
        print('|__________________________________________________|')



    elif user == 'S':
        rate = # Your rate
        taxRateSara = # Your tax rate
        shiftDiffRate = # Your differential rate
        otRate = # Your OT rate(hourly,NOT multiplier)


        hours_Sara = float(input('Total hours: '))
        shiftDiff = float(input('Shift diff: '))
        otHours = float(input('OT Hours: '))

        gross_Sara = ((rate * hours_Sara) + (otRate * otHours) + (shiftDiffRate * shiftDiff)).__round__(2)
        taxes_Sara = (gross_Sara * taxRateSara).__round__(2)
        net_Sara = (gross_Sara - taxes_Sara).__round__(2)

        print('____________________________________________________')
        print('| Hours |    Gross    |    Taxes   |     Net       |')
        print('|-------|-------------|------------|---------------|')
        print(f"| {hours_Sara}  |   ${gross_Sara}   |   ${taxes_Sara}  |   ${net_Sara}    |")
        print('|__________________________________________________|')
