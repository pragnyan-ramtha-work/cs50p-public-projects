import numpy as np
import matplotlib.pyplot as plt

# Function to iterate over 1/z^2 + c
def iterate_inverse_square_plus_c(c, max_iter):
    z = 0
    n = 0
    while n < max_iter:
        # Avoid division by zero by setting a small threshold
        if abs(z) < 1e-10:
            return max_iter  # Treat as if it hasn't escaped
        z = z * z + c
        n += 1
        # Escape condition if z becomes too large
        if abs(z) > 1e10:
            return n
    return max_iter

# Generate the fractal set for 1/z^2 + c
def inverse_square_plus_c_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    result = np.zeros((height, width))
    for i in range(width):
        for j in range(height):
            c = complex(x[i], y[j])
            result[j, i] = iterate_inverse_square_plus_c(c, max_iter)
    return result

# Set parameters for the plot
xmin, xmax, ymin, ymax = -100.0, 100.0, -100.0,100.0
width, height = 800, 800
max_iter = 100

# Generate and plot the fractal
inverse_square_plus_c_image = inverse_square_plus_c_fractal(xmin, xmax, ymin, ymax, width, height, max_iter)
plt.imshow(inverse_square_plus_c_image, extent=(xmin, xmax, ymin, ymax), cmap="hot")
plt.colorbar()
plt.title("Fractal of f(z) = 1/z^2 + c")
plt.xlabel("Real part of c")
plt.ylabel("Imaginary part of c")
plt.show()
