import numpy as np
import matplotlib.pyplot as plt
import estimators

# Parameters
n_pixels = 1000
axis_limit = 1
tol = 1e-15
max_iter = 100

f = lambda z : z**(4+3j)-1
df = lambda z : (4+3j)*z**(3+3j)
ddf = lambda z : (4+3j)*(3+3j)*z**(2+3j)

# Calculations
vals = np.linspace(-axis_limit, axis_limit, n_pixels)
n_iterations = np.zeros((n_pixels, n_pixels))

def get_n_iter(x, y):
    z = complex(x, y)
    for i in range(max_iter):
        new_z = estimators.newton(z, f, df)
        #new_z = estimators.halley(z, f, df, ddf)
        if abs(z-new_z) < tol:
            return i
        z = new_z
    return max_iter

for i in range(n_pixels):
    for j in range(n_pixels):
        x = vals[i]
        y = vals[j]
        n_iterations[i,j] = get_n_iter(x, y)


# Plot setup
fig = plt.figure(figsize=(10,10))
plt.imshow(n_iterations, cmap="Greys_r", extent=[-axis_limit, axis_limit, -axis_limit, axis_limit])

# Save figure
fig.savefig("images/out.png")
plt.show()