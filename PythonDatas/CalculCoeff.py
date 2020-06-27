from cmath import *

PRECISION = 1000

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

with open("ListEdges.txt", "r") as f:
	data = f.read()

points = data.split("\n")
pointsList = []
for index, line in enumerate(points):
	if(index < len(points) - 1):
		point = line.split(",")
		pointsList.append([int(point[0]), int(point[1])])

# Calculation of the coefficients, complex
frequencies = []
complexCoefficients = []
for i in range(PRECISION):
	frequencies.append(i)
	complexCoefficients.append(integral(i, pointsList))
	if(i != 0):
		frequencies.append(-i)
		complexCoefficients.append(integral(-i, pointsList))

# Translation into the needed format
sizes = []
angles = []
for coeff in complexCoefficients:
	sizes.append(abs(coeff))
	angles.append(phase(coeff))

with open("..//MainScript/ListCoeffs.txt", "w") as f:
	for frequency, size, angle in zip(frequencies, sizes, angles):
		f.write("{},{},{}\n".format(frequency, size, angle))