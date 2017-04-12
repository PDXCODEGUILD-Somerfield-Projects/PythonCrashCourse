change_float = float(input("How much change? >"))

dollar_int = int(change_float//1)
print("Return " + str(dollar_int) + " dollars.")

change_decimal = change_float - dollar_int

if change_decimal >= .25:
    quarters = change_decimal // .25
    print("Return " + str(int(quarters)) + " quarters.")
    change_decimal -= quarters * .25

if change_decimal >= .10:
    dimes = change_decimal // .10
    print("Return " + str(int(dimes)) + " dimes.")
    change_decimal -= dimes * .10

if change_decimal >= .05:
    nickels = change_decimal // .05
    print("Return " + str(int(nickels)) + " nickels.")
    change_decimal -= nickels * .05
    # change_decimal rounded up or python won't recognize
    # a 1 penny solution
    change_decimal = round(change_decimal, 2)

if change_decimal >= .01:
    pennies = (round(change_decimal, 2)) * 100
    print("Return " + str(int(pennies)) + " pennies.")




