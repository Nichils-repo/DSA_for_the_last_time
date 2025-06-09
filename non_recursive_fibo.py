def fib(n):

    if n == 0:
        return 0
    if n == 1:
        return 1 
    
    answer = 0
    first = 0
    second = 1

    #0,1,2,3,4,5,6 index 
    #1,2,3,4,5,6,7 nth fib
    #0,1,1,2,3,5,8 nth fib answer
    for i in range(0,n-1):
        answer = first + second
        first = answer
        second = first

    return answer
