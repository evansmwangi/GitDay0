from  math import sqrt
def PrimeChecker(integer)
intended_value=eval(input('list prime numbers upto this value:')
    integer = 2
    if intended_value is not int:
    return('enter integer value')
    while integer<=intended_value:
        is_Prime=True
        try_factor=2
        root=sqrt(integer)
        while try_factor<=root:
            if integer%try_factor==0:
                is_Prime=False;
                break
                try_factor+=1
                if is_Prime:
        return (integer, end=' ')
    integer +=1
 print ()
    
