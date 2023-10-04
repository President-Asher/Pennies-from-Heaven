import math

num_of_pennies = input("Please enter the number of pennies: ")
num_of_pennies = int(num_of_pennies)

p_in_dollar = 100
p_in_quarter = 25
p_in_dime = 10
p_in_nickel = 5

num_of_dollars = num_of_pennies // p_in_dollar
print(num_of_dollars)

the_change = num_of_pennies % p_in_dollar
print(the_change)

num_of_quarters = the_change // p_in_quarter
print(num_of_quarters)

num_of_dimes = the_change // p_in_dime
print(num_of_dimes)

num_of_nickels = the_change // p_in_nickel
print(num_of_nickels)