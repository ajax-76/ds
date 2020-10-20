def digital_root(n):
    summ = 0
    while n>0:
        summ =summ + n % 10
        n =n // 10
    #check sum is single digit
    if summ//10 == 0:
        return summ
    else:
       return  digital_root(summ)

print(digital_root(941))           