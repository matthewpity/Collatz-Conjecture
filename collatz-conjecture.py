seed = 295147905179430533351
while True:
	t = seed
	path = []
	while t >= seed:
		if t%2 == 0:
			t = t/2
		else:
			t = (t*3)+1
		print(f"{seed} position: {t}")
		path.append(t)
	print(f"{seed} failed. Path: {path}")
	seed = seed+1
