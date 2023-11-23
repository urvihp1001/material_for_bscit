def fn(n):
        if n==0:
            return 0
        else:
            
            return n%10+fn(n//10)
print(fn(1728))
