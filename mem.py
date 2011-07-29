










a={0:0,1:1}
def fib(n):
  if not n in a:
    a[n]=fib(n-1)+fib(n-2)
  return a[n]


fib(50)


    


    



    
