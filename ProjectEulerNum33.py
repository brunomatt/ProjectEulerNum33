# The fraction 49/98 is a curious fraction,
# as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct,
# is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
from fractions import Fraction

four_nums = []
four_denoms = []
final_num = 1
final_denom = 1
numerator = [i for i in range(10, 99)]
denominator = [k for k in range(10,100)]

def incorrect_cancel(num, denom):
    num_digits = [i for i in str(num)]
    denom_digits = [k for k in str(denom)]
    for digit in num_digits:
        if digit in denom_digits:
            num_digits.remove(digit)
            denom_digits.remove(digit)
        if len(num_digits) == 1:
            fraction = num_digits + denom_digits
        else:
            fraction = [1,1]
    if int(fraction[1]) != 0:
        value = int(fraction[0]) / int(fraction[1])
        if value == (num / denom) and denom % 10 != 0:
            four_nums.append(int(fraction[0]))
            four_denoms.append(int(fraction[1]))

for i in numerator:
    for k in denominator:
        if i / k < 1:
            incorrect_cancel(i,k)

for j in four_nums:
    final_num = final_num * j

for j in four_denoms:
    final_denom = final_denom * j

print(Fraction(final_num / final_denom).limit_denominator(10000))
