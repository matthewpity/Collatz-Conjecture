seed = 2**68

while True:
	t = seed
	while t >= seed:
		if t%2 == 0: t = t/2
		else: t = (t*3)+1
		
	print(f"Seed {seed} failed.")
	seed = seed+1
