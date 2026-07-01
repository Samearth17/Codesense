import numpy as np
 
def cannyEdgeDetector(img, sigma):
    
    # Step 1: Filter the image with a Gaussian filter to remove noise
    blurred = gaussianFilter(img, sigma)
    
    # Step 2: Obtain the gradients (Gx, Gy) of the blurred image
    Gx, Gy = sobelFilter(blurred)
    
    # Step 3: Calculate the magnitude and angle of the gradient
    magnitude, angle = calculateGradient(Gx, Gy)
    
    # Step 4: Non-maximum suppression to thin the edges while retaining 
    # strong edge points
    thin_image = nonMaximumSuppression(magnitude, angle)
    
    # Step 5: Double threshold to classify pixels as weak or strong edge
    strong_px, weak_px = doubleThreshold(thin_image)
    
    # Step 6: Trace through the edge map and obtain the final edges
    edges = followEdge(strong_px, weak_px)
    
    return edges