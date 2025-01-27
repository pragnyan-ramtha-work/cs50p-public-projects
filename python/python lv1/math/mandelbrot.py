import numpy as np
import matplotlib.pyplot as plt

# Function to compute the Mandelbrot set
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

# Generate the Mandelbrot set for a given region and resolution
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    mandelbrot_image = np.empty((height, width))
    for i in range(width):
        for j in range(height):
            c = complex(r1[i], r2[j])
            mandelbrot_image[j, i] = mandelbrot(c, max_iter)
    return mandelbrot_image

# Set the parameters for the plot
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 800, 800
max_iter = 10000

# Generate and plot the Mandelbrot set
mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
plt.imshow(mandelbrot_image, extent=(xmin, xmax, ymin, ymax), cmap="hot")
plt.colorbar(label="Number of iterations")
plt.title("Mandelbrot Set")
plt.xlabel("Real part of c")
plt.ylabel("Imaginary part of c")
plt.show()
