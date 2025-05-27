#make a set of Fibonacci numbers seeded with 1 and 2
fib_nums=[1, 2]

#define indices using negative indexing so we can do sums with values at the end of the list
indices=[-2,-1]

#go thru numbers up to 4,000,000 to fill out the rest of the sequence for the problem requirements
for x in range(4000000):
    if x == sum(fib_nums[i] for i in indices):
      fib_nums.append(x) 

#define the set of even numbers only
fib_even=[]
      
#use mod to identify the even Fibonacci numbers 
for x in fib_nums:
    if x % 2 == 0:
     fib_even.append(x)
     
     
#output the sum of our even Fibonacci numbers    
print(sum(fib_even))
