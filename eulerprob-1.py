# declare the list called “multiples”
multiples = []

# start a for() loop to iterate thru 1000 values 
for x in range(1000):
# check if a multiple of 5, add to list if true
  if x % 5 == 0:
    multiples.append(x)
# check if a multiple of 3, add to list if true
  elif x % 3 == 0:
   multiples.append(x)

# output the sum of the list of multiples of 3 and 5
print(sum(multiples))
