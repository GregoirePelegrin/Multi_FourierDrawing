from cmath import *

def function1(t, List):
	x = List[round(t * len(List))][0]
	y = List[round(t * len(List))][1]
	return complex(x, y)

def function2(n, t):
	return exp(complex(0, -n * 2 * pi * t))

def integral(n, List):
	integr = 0
	h = 1/len(List)
	for i in range(len(List)):
		integr += function1(i*h, List)*function2(n, i*h)
	integr *= h
	return integr

def calculCoeff(prec):
	print("[Coefficients calculation]: Data recuperation")
	with open("./MainScript/ListEdgesSorted.txt", "r") as f:
		data = f.read()
	points = data.split("\n")
	pointsList = []
	for index, line in enumerate(points):
		if(index < len(points) - 1):
			point = line.split(",")
			pointsList.append([int(point[0]), int(point[1])])

	print("[Coefficients calculation]: Complex coefficients start")
	# Calculation of the coefficients, complex
	frequencies = []
	complexCoefficients = []
	for i in range(prec):
		if(i == int(prec/2)):
			print("[Coefficients calculation]: 50% done")
		frequencies.append(i)
		complexCoefficients.append(integral(i, pointsList))
		if(i != 0):
			frequencies.append(-i)
			complexCoefficients.append(integral(-i, pointsList))
	print("[Coefficients calculation]: Complex coefficients done")

	print("[Coefficients calculation]: Coefficients translation start")
	# Translation into the needed format
	sizes = []
	angles = []
	for index, coeff in enumerate(complexCoefficients):
		if(index == int(prec/2)):
			print("[Coefficients calculation]: 50% done")
		sizes.append(abs(coeff))
		angles.append(phase(coeff))
	print("[Coefficients calculation]: Coefficients translation done")

	print("[Coefficients calculation]: Writing in progress")
	with open("./MainScript/ListCoeffs.txt", "w") as f:
		for frequency, size, angle in zip(frequencies, sizes, angles):
			f.write("{},{},{}\n".format(frequency, size, angle))
	print("[Coefficients calculation]: Finished")

nbrVectors = 750 # In fact ther is 2x this nbr, positive and negative frequencies
calculCoeff(nbrVectors)