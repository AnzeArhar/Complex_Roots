# Complex roots

Python scripts to generate visualizations of iterative root finding algorithms
in the complex plane using [matplotlib](https://matplotlib.org/) and
[numpy](https://numpy.org/).

## Samples

![Newton's method for $z^{4+3i}-1$](images/newton_6.png)

![Halley's method for $z^{13}-z-1$](images/halley_3.png)

![Newton's method for $z^7-z-1$](images/newton_2.png)

## PDF document generation

Requires installation of [pandoc universal document converter](https://pandoc.org/).

```
pandoc output.md -o output.pdf
```

## About

See [output.pdf](output.pdf) document for more information about the algorithms.