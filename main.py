def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    # Case: numberOfCoffees <= 8
    if numberOfCoffees // 9 == 0:
        return numberOfCoffees * pricePerCoffee
    # Case: numberOfCoffees >= 9
    return (numberOfCoffees - (numberOfCoffees // 9)) * pricePerCoffee


"""
def getCostOfCoffee(numberOfCoffees, pricePerCoffee):
    i = 1
    total = 0

    while numberOfCoffees > 0:
        if i == 9:
            # I want to reset the count to know if there are bought other 9 coffees
            i = 1
            # The ninth coffe count as 1 but I don't have to add the price
            numberOfCoffees -= 1
            continue
        # i contain the value of the next coffe that should be counted
        i += 1
        # total is the total price
        total += pricePerCoffee
        # I counted a coffe so numberOfCoffees represent the coffees that I still have to count
        numberOfCoffees -= 1
    return total
"""

assert getCostOfCoffee(7, 2.50) == 17.50
assert getCostOfCoffee(8, 2.50) == 20
assert getCostOfCoffee(9, 2.50) == 20
assert getCostOfCoffee(10, 2.50) == 22.50

for i in range(1, 4):
    assert getCostOfCoffee(0, i) == 0
    assert getCostOfCoffee(8, i) == 8 * i
    assert getCostOfCoffee(9, i) == 8 * i
    assert getCostOfCoffee(18, i) == 16 * i
    assert getCostOfCoffee(19, i) == 17 * i
    assert getCostOfCoffee(30, i) == 27 * i