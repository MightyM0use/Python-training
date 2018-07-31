i = 0
n = 0
s = 0
sum_sqr = 0 
sum_s = 0
r = 0

# n is a natural number between 1 and 100
# sqr_n is for the variable we need to stock (the square of n)
# sum_sqr_n is to stock the sum of the square of each number
while n <= 100 : 
	sqr_n = n*n
	sum_sqr= sum_sqr + sqr_n
	n = n + 1

# s is a natural number between 1 and 100
#sum_s is for the variable we need to stock (the sum of sum_s + s until s reaches 100)

while s <= 100 : 
	sum_s = sum_s + s
	s = s + 1

sum_s = sum_s * sum_s
r = sum_s - sum_sqr
print r
