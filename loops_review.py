# Your code below:
#list containing vales 0 - 9
single_digits = list(range(10))
squares = []
for i in single_digits:
  #create a new list containing the squared values of each value from the prev. list
  squares.append(i*i)
  print(i)

print(squares)

#list comprehension - get cubed values of the original list
cubes = [sd * sd * sd for sd in single_digits]
print(cubes)
