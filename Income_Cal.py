# """
# Date: 3/21/2020
# Version: 3.7
# Owner: anemiaxb
# Author:
# Rationale:
# """
# """
#
# Cal's intro.
#
# The user will answer questions pertaining to pay type including pay type,frequency, and if they know their tax rate.
#
# """
#
# print("Welcome! My name is Cal and I will be helping you today. To get started, I need some information about your income.")
#
# pay_type = ['H', 'S']
# frequency = ['W', 'B', 'M']
# tax_rate = ['Y', 'N']
#
# user_pay_type = None
# user_pay_frequency = None
# user_tax_rate = None
#
# while user_pay_type not in pay_type or user_pay_frequency not in frequency or user_tax_rate not in tax_rate:
#     user_pay_type = input('What is your pay type? (H)ourly or (S)alary: ').strip().title()
#     if user_pay_type == 'H':
#         hourly_rate = float(input('Hourly Rate: $ ').strip())
#     elif user_pay_type == 'S':
#         user_salary = float(input('Gross Annual Salary: $ ').strip().replace(',', ''))
#         user_pay_frequency = input('Are you paid (W)eekly, (B)i-weekly, or (M)onthly?: ').strip().title()
#     else:
#         print("Sorry,I don't recognize that! Please restart program.")
#     while True:
#         try:
#             user_ot_rate = float(input('What is your OT rate?: ').strip())
#             break
#         except ValueError:
#             print('Oops! That was not a valid number. Try again...')
#     user_tax_rate = input('Do you know what your tax rate is? Y or N: ').strip().title()
#     if user_tax_rate == 'Y':
#         while True:
#             try:
#                 user_tax_rate_float = float(input('Tax rate(as whole number): ').strip())
#                 user_tax_rate_converted = (user_tax_rate_float / 100)
#                 break
#             except ValueError:
#                 print('Enter your tax rate as a whole number...')
#     break
#
#
# def h_w_y():
#     hourly_rate = float(input('Hourly rate: $'))
#     hours_worked =
#
#
# # user_tax_rate_float = float(input('Tax rate: ').strip())
# # user_tax_rate_converted = (user_tax_rate_float / 100)
#
# # print('For me to figure out your tax rate, I will need information from your LAST paycheck.')
#
# # Calculate weekly,bi-weekly,or monthly gross pay IF user_schedule == salary and user_tax_rate == Y
#
#
# if user_salary_pay_frequency == 'W' and user_tax == 'Y':
#
#     weekly_gross = (user_salary / 52).__round__(2)
#     weekly_net = (weekly_gross - (weekly_gross * user_tax_rate_converted)).__round__(2)
#
#     print("The results are based on information you have provided to me.")
#     print('Weekly Gross: ${}'.format(weekly_gross))
#     print('Weekly Net: ${}'.format(weekly_net))
#
# elif user_salary_pay_frequency == 'B' and user_tax == 'Y':
#
#     biWeekly_gross = (user_salary / 26).__round__(2)
#     biWeekly_net = (biWeekly_gross - (biWeekly_gross * user_tax_rate_converted)).__round__(2)
#
#     print("The results are based on information you have provided to me.")
#     print('Bi-Weekly Gross: ${}'.format(biWeekly_gross))
#     print('Bi-Weekly Net: ${}'.format(biWeekly_net))
#
# elif user_salary_pay_frequency == 'M' and user_tax == 'Y':
#     monthly_gross = (user_salary / 12).__round__(2)
#     monthly_net = (monthly_gross - (monthly_gross * user_tax_rate_converted)).__round__(2)
#
#     print("The results are based on information you have provided to me.")
#     print('Monthly Gross: ${}'.format(monthly_gross))
#     print('Monthly Net: ${}'.format(monthly_net))
#
# else:
# print('Error! Please restart program.')
# Calculate gross pay IF user_schedule == hourly and user_tax_rate == Y


# Calculate weekly,bi-weekly,or monthly gross pay IF user_schedule == salary and user_tax_rate == N

# Calculate gross pay IF user_schedule == hourly and user_tax_rate == N
