# mortgage.py
#
# Exercise 1.7

principal = 100000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_payments = 0
rate_multiplier = 1 + rate/12
extra_payment = 1000
extra_payment_start = 13
extra_payment_end = 24

while principal > 0:
    num_payments += 1
    if (num_payments >= extra_payment_start) and (num_payments <= extra_payment_end):
        this_payment = payment + extra_payment
    else:
        this_payment = payment

    if (principal < this_payment):
        principal = 0
    else:
        principal = principal * rate_multiplier - this_payment

    total_paid = total_paid + this_payment
    print(num_payments, round(this_payment, 2), round(total_paid, 2), round(principal, 2))

print()
print ('Total paid = ', round(total_paid, 2))
print ('Number of payments = ', num_payments)


