/* Beginner's way */
i = 1
even_numbers = []
while i <= 10:
	if i % 2 == 0
		even_numbers.append(i)
	i+= 1
	
/* Intermediate's way */
numbers = range(1, 11)
even_numbers = [x for x in numbers if x % 2 == 0]

/* Professional's way */
even_numbers = list(range(2, 11, 2))
