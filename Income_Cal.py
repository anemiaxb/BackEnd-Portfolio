"""
Date: 3/18/2020
Version: 3.7
Owner: anemiaxb
Author:
Rationale:
"""

"""

Cal's intro.

The user will answer questions pertaining to pay type including pay schedule,hourly rate,gross salary,pay frequency,and tax rate.

"""

welcome = "Welcome! My name is Cal and I will be helping you today. To get started, I need some information about your income."

print(welcome)

# While loop until user inputs "Hourly" or "Salary"

pay_type = ['H', 'S']

user_schedule = None

while user_schedule not in pay_type:
    user_schedule = input('What is your pay type? (H)ourly or (S)alary: ').title().strip()

# Asking user hourly rate or gross salary and pay frequency

if user_schedule == 'S':

    user_salary = float(input('Gross Annual Salary: $ ').strip().replace(',', ''))  # float

    user_salary_pay_frequency = input('Are you paid (W)eekly, (B)i-weekly, or (M)onthly?: ').strip().title()

else:

    user_hourly_rate = float(input('What is your hourly rate?: $ ').strip())  # float

# Asking user for tax rate, if not known, then will calculate using previous paycheck info

user_tax = input('Do you know what your tax rate is? Y or N: ').strip().upper()

if user_tax == 'Y':

    user_tax_rate_float = float(input('Tax rate: ').strip())
    user_tax_rate_converted = (user_tax_rate_float / 100)

else:

    print('For me to figure out your tax rate, I will need information from your LAST paycheck.')

# Calculate weekly,bi-weekly,or monthly gross pay IF user_schedule == salary and user_tax_rate == Y

print("The results are based on information you have provided to me.")

if user_salary_pay_frequency == 'W':

    weekly_gross = (user_salary / 52).__round__(2)
    weekly_net = (weekly_gross - (weekly_gross * user_tax_rate_converted)).__round__(2)

    print('Weekly Gross: ${}'.format(weekly_gross))
    print('Weekly Net: ${}'.format(weekly_net))

elif user_salary_pay_frequency == 'B':

    biWeekly_gross = (user_salary / 26).__round__(2)
    biWeekly_net = (biWeekly_gross - (biWeekly_gross * user_tax_rate_converted)).__round__(2)

    print('Bi-Weekly Gross: ${}'.format(biWeekly_gross))
    print('Bi-Weekly Net: ${}'.format(biWeekly_net))

# Calculate gross pay IF user_schedule == hourly and user_tax_rate == Y


# Calculate weekly,bi-weekly,or monthly gross pay IF user_schedule == salary and user_tax_rate == N

# Calculate gross pay IF user_schedule == hourly and user_tax_rate == N
