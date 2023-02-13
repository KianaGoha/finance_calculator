# include import math at the top of file
import math

# create variables to provide guidance for the user about what they have to do and the options they can choose from using the calculate, then print them on separate lines
rules = "Choose either 'investment' or 'bond' from the menu below to proceed: "
option1 = "Investment - to calculate the amount of interest you'll earn on your investment."
option2 = "Bond - to calculate the amount you'll have to pay on a home loan."
print(f"{rules} \n\n{option1} \n{option2} \n")

# ask the user which calculation they would like to carry out
calculation = input("Which calculation would you like to carry out? (investment or bond) ")
# create a variable to convert their input to lowercase letters to ensure how the user capitalises their answer does not affect the program and how it proceeds
answer = calculation.lower() 

# if the user chooses the investment option then do the following:
    # ask the user to input the amount of money they are depositing and store it as a float
    # ask the user to enter the interest rate making sure that the user inputs a number only and not the percentage sign and store it as a float
    # divide the interest rate the user has input by 100 it is used as a percentage in the calculation later
    # ask the user to input the number of years that they plan on investing and store it as an integer
    # create a variable called interest and ask the user whether they would like to calculate simple or compound interest
    # make sure to convert the input for the interest variable to lowercase so that the way the user capitalises the input does not affect how the program proceeds
if answer == "investment":
    deposit = float(input("How much money are you depositing? £"))
    interest_rate = float(input("What is the interest rate (only input the number without % sign)? "))
    interest_percentage = interest_rate / 100
    years = int(input("How many years do you plan on investing? "))
    interest = input("Would you like simple or compound interest? ")
    interest = interest.lower()

    # if the user inputs simple then calculate the simple interest by applying the formula A = P(1 + r * t)
    if interest == "simple":
        return_investment = deposit * (1 + interest_percentage * years)
    # if the user inputs compound then calculate the compound interest by applying the formula A = P(1 + r) ^ t
    else:
        return_investment = deposit * math.pow((1 + interest_percentage), years)
    print(f"You will get back £{return_investment} after {years} years at {interest_rate}% interest rate for the specified deposit amount of £{deposit}")

# if the user chooses the bond option at the beginning then do the following:
    # ask the user for the present value of their house and store as a float 
    # ask the user to input the interest rate per annum making sure they only input a number and not the percentage sign then store as a float
    # divide the interest rate the user has input by 100 it is used as a percentage 
    # divide this interest rate by 12 to find the monthly interest to use in the calculation later
    # ask the user to input the number of months that they plan to take to repay the bond and store as an integer
    # calculate the amount the user has to pay each month to repay the loan, round the answer to 2 decimal places, and print the answer
elif answer == "bond":
    present_value = float(input("What is the present value of your house? £ "))
    rate = float(input("What is the interest rate per annum (only input the number without % sign)? "))
    rate = rate / 100
    monthly_interest = rate / 12
    months = int(input("Over how many months are you planning to take to repay the bond? "))
    monthly_payback = (monthly_interest * present_value) / (1 - (1 + monthly_interest) ** (-months))
    monthly_payback = round(monthly_payback, 2)
    print(f"You will have to pay back £{monthly_payback} each month")