import matplotlib
matplotlib.use('TkAgg')
import math
import numpy as np
from matplotlib import pyplot as plt

origin = [0, 0]
refvec = [0, 1]

def clockwiseangle_and_distance(point):
    # Vector between point and the origin: v = p - o
    vector = [point[0]-origin[0], point[1]-origin[1]]
    # Length of vector: ||v||
    lenvector = math.hypot(vector[0], vector[1])
    # If length is zero there is no angle
    if lenvector == 0:
        return -math.pi, 0
    # Normalize vector: v/||v||
    normalized = [vector[0]/lenvector, vector[1]/lenvector]
    dotprod  = normalized[0]*refvec[0] + normalized[1]*refvec[1]     # x1*x2 + y1*y2
    diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]     # x1*y2 - y1*x2
    angle = math.atan2(diffprod, dotprod)
    # Negative angles represent counter-clockwise angles so we need to subtract them 
    # from 2*pi (360 degrees)
    if angle < 0:
        return 2*math.pi+angle, lenvector
    # I return first the angle because that's the primary sorting criterium
    # but if two vectors have the same angle then the shorter distance should come first.
    return angle, lenvector

#define the vertical filter
vertical_filter = [[-1,-2,-1], [0,0,0], [1,2,1]]

#define the horizontal filter
horizontal_filter = [[-1,0,1], [-2,0,2], [-1,0,1]]

#read in the pinwheel image
img = plt.imread('Elephant.png')

#get the dimensions of the image
n,m,d = img.shape

#initialize the edges image
edges_img = img.copy()
filtered_img = edges_img.copy()

#loop over all pixels in the image
for row in range(3, n-2):
    for col in range(3, m-2):
        
        #create little local 3x3 box
        local_pixels = img[row-1:row+2, col-1:col+2, 0]
        
        #apply the vertical filter
        vertical_transformed_pixels = vertical_filter*local_pixels
        #remap the vertical score
        vertical_score = vertical_transformed_pixels.sum()/4
        
        #apply the horizontal filter
        horizontal_transformed_pixels = horizontal_filter*local_pixels
        #remap the horizontal score
        horizontal_score = horizontal_transformed_pixels.sum()/4
        
        #combine the horizontal and vertical scores into a total edge score
        edge_score = (vertical_score**2 + horizontal_score**2)**.5
        
        #insert this edge score into the edges image
        edges_img[row, col] = [edge_score]*3

        if(edge_score > 0.4):
            filtered_img[row, col] = [1]*3
        else:
            filtered_img[row, col] = [0]*3

for row in range(n):
    for col in range(m):
        if(row < 3 or row > n-3):
            filtered_img[row, col] = [0]*3
        elif(col < 3 or col > m-3):
            filtered_img[row, col] = [0]*3

edgesList = []
for row in range(n):
    for col in range(m):
        if(np.all(filtered_img[row][col] == 1)):
            edgesList.append([row, col])

edgesList2 = sorted(edgesList, key=clockwiseangle_and_distance)

with open("ListEdges.txt", "w") as f:
    for coord in edgesList2:
        f.write("{},{}\n".format(coord[0], coord[1]))

# plt.subplot(121)
# plt.imshow(img)
# plt.subplot(122)
# plt.imshow(filtered_img)
# plt.show()