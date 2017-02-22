"""Calculates and prints total Oregon income tax"""

tax_burden = 0

tier_1_bracket = 3350
tier_2_bracket = 5050
tier_3_bracket = 116000

tier_1_limit = 3350
tier_2_limit = 8400
tier_3_limit = 124400

tier_1_tax = .05
tier_2_tax = .07
tier_3_tax = .09
tier_4_tax = .099


def calculate_ore_tax(user_gross_income):
    """Determines the OR taxes based on gross income"""
    taxable_running_total = user_gross_income
    ore_tax_running_total = 0

    if user_gross_income >= tier_1_limit:
        ore_tax_running_total += tier_1_bracket * tier_1_tax
        taxable_running_total -= tier_1_bracket

        if user_gross_income >= tier_2_limit:
            ore_tax_running_total += tier_2_bracket * tier_2_tax
            taxable_running_total -= tier_2_bracket

            if user_gross_income >= tier_3_limit:
                ore_tax_running_total += tier_3_bracket * tier_3_tax
                taxable_running_total -= tier_3_bracket

                if user_gross_income  > tier_3_limit:
                    ore_tax_running_total += taxable_running_total * tier_4_tax

            else:
                ore_tax_running_total += taxable_running_total * tier_3_tax

        else:
            ore_tax_running_total += taxable_running_total * tier_2_tax

    else:
        ore_tax_running_total = user_gross_income * tier_1_tax


    return ore_tax_running_total



# Get user's full income
user_gross_income = float(input("What is your gross income? -->"))

tax_burden = calculate_ore_tax(user_gross_income)

print('Your tax burden is: $' + str(tax_burden) + ".")

