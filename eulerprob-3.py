#problem: What is the largest prime factor of the number 600851475143?

#let the user input a number of their choice, the target number
target=int(input("Type your number here: \n"))

#create an empty list to store factors
factors=[]

#use for loop to find factors of target number starting with 1 to avoid division by 0
def find_factor(target):
    for x in range(1, target+1):
        if target % x == 0:
            factors.append(x) #add found factors to the list
#find_factor(target)
#show output of prime and non-prime factors
#print("Factors of " + str(target) + ":" + str(factors))

#make an empty list for prime factors 
#prime_factors=[]
#index=factors[1]

#def is_prime(factors):
    #for y in range(2,factors[-1]):
        #for i in range(len(factors)):
            #if i % y == 0:
                #sub_factors.append(y)
            #if len(sub_factors) > 2:
                #return "not prime"
            #else:
                #return "prime"
#print(is_prime(factors))

#print(len(sub_factors))

#######
# I kept getting stuck trying to make the logic for finding prime numbers based on the len() of the list of factors for each known factor
# I ended up looking up some solutions to learn where I was going wrong; a solution from ChatGPT is below with my notes in the comments for my understanding

#look for prime factors of n (the target number)

p_factors = []

def prime_factors(n):
    
    #declare the empty list
    
    #start at the smallest prime number for iterations
    i = 2
    
    #limit the search to numbers which are equal to or less than the sqrt of n, there will not be new factors greater than the sqrt of n
    while i * i <= n:
        
        #same logic I've been using to look at factors
        if n % i != 0:
            i += 1
            
        #if n is divisible by i is True..add it to the list
        else:
            n //= i
            p_factors.append(i)
            
    #prime factors are always 1 and n (itself)
    if n > 1:
        p_factors.append(n)
    return p_factors
        

#call function 
prime_factors(target)

#find largest prime factor
biggest=p_factors[-1]

print("The largest prime factor of "+str(target)+" is "+str(biggest)+".")
    
