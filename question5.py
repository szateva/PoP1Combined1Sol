
def balance(init_sum, int_rate, tfl, tax_rate, M):
    bal = init_sum
    for i in range(0, M):
        interest = (int_rate / 100) * bal
        if bal > tfl:
            tax = (tax_rate / 100) * (bal - tfl)
        else:
            tax = 0
        bal += interest - tax
    return bal


print(balance(10000, 1, 20000, 1, 2))
print(balance(25000, 2, 20000, 1, 2))
print(balance(19800, 2, 20000, 1, 2))