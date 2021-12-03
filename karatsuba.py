def karatsuba(x,y):

    if len(str(x)) == 1 or len(str(y)) == 1:
        return int(x)*int(y)
    
    # suppoose number of digits in x and y are different
    # x = 12345
    # y = 12
    # but we consider both the number of same length by assuming 0's in small number
    # x = 12345
    # y = 00012
    # Now, length of both the numbers is same, So we can find universal cut
    # cut = 5//2 = 2
    # then we approach like this    
    # a = 123
    # b = 45
    # c = 000 #Which is actually c = 0 in memory. Hance, len(str(c)) = 0 and algorithom will directly return 0 in next step
    # d = 12 
    
    n = max(len(str(x)), len(str(y)))
    cut = n//2

    a = x//10**cut
    b = x%10**cut

    c = y//10**cut
    d = y%10**cut

    ac = karatsuba(a,c)
    bd = karatsuba (b,d)
    ad_plus_bc = karatsuba(a+b,c+d) - ac -bd 

    return (10**(2*cut)) * ac + (10**cut) * ad_plus_bc + bd
 
ans = karatsuba(234224342423423424234242334234,5672323442424234234234242438)
print(ans)
