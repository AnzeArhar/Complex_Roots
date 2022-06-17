---
title: "Visualizations of iterative root finding algorithms in the complex plane"
author: "Anže Arhar"
date: "2022-06-17"
numbersections: true
geometry: "a4paper"
---

Showcase of a selection of visualizations of iterative root finding algorithms
in the complex plane.

\tableofcontents

\listoffigures

\newpage

# Explanation

The images are colored by the number of iterations it takes the algorithm to
converge on the root of the equation within some tolerance (for the following
images we used a value of $10^{-15}$) for a given starting point. If the
algorithm exceeds 100 iterations, the pixel is colored white. Less iterations
means that the pixel is darker.

# Algorithms

## Newton's method

$$z_{n+1}=z_n-\frac{f(z_n)}{f'(z_n)}$$

## Halley's method

$$z_{n+1}=z_n-\frac{2f(z_n)f'(z_n)}{2(f'(z_n))^2-f(z_n)f''(z_n)}$$

## Stefenssen's method

$$z_{n+1}=z_n-\frac{f(z_n)}{\frac{f(z_n+f(z_n))}{f(z_n)}-1}$$

# References

- https://en.wikipedia.org/wiki/Root-finding_algorithms
- https://blbadger.github.io

\newpage

![Newton's method for $z^3-1$](images/newton_1.png)

![Halley's method for $z^3-1$](images/halley_1.png)

![Newton's method for $z^7-z-1$](images/newton_2.png)

![Halley's method for $z^7-z-1$](images/halley_2.png)

![Newton's method for $z^{13}-z-1$](images/newton_3.png)

![Halley's method for $z^{13}-z-1$](images/halley_3.png)

![Newton's method for $z^3-2z+2$](images/newton_4.png)

![Halley's method for $z^3-2z+2$](images/halley_4.png)

![Newton's method for $z^8+15z^4-16$](images/newton_5.png)

![Halley's method for $z^8+15z^4-16$](images/halley_5.png)

![Newton's method for $z^{4+3i}-1$](images/newton_6.png)

![Halley's method for $z^{4+3i}-1$](images/halley_6.png)