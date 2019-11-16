def interests(p, n):
    '''
    :param p: interest rate a bank is offered.
    :param n: years
    :return:  the total amount of money when the deposit is drawn.
    '''
    import math
    sum=(1+p/100)**n
    return sum
A=1000
A*=interests(5, 5)
print('If you save 1000 in the bank, after 5 years you may get %.2f back.'%A )
