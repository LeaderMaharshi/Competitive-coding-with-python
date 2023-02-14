
def decimal_to_octal(num):
    if num == 0:
        return '0'
    octal = ''
    while n>0:
        octal = str(n % 8)+octal
        n // 8
    return octal