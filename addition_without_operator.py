

# def add(*args):
#     print(sum(args))
#
# add(1,2,3,4,5)

def add_without_arithmetic_operator(a, b):
    while b != 0:
        # carry contains common set bits of a and b
        carry = a & b

        # Sum of bits of a and b where at least one of the bits is not set
        a = a ^ b
        # Carry is shifted by one so that adding it to a gives the required sum
        b = carry << 1

    return a

print(add_without_arithmetic_operator(2,3))