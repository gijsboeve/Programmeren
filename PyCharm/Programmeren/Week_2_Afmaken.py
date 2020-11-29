principal_amount = float(input("How many money you want to use"))

interest_rate = int(input("how much interest do you get?"))
interest_times_a_year = 4
amount_of_years = 3

final_amount = principal_amount * (1 + (interest_rate/interest_times_a_year)) ** (interest_times_a_year*amount_of_years)

print(final_amount)
