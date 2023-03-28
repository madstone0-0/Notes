---
title: Implicit Differentiation
author: Madiba Hudson-Quansah
creator: Madiba Hudson-Quansah
subject: Calculus 1
tags:
    - Calculus
    - Derivatives
---

##### Explicit Function

$y = x^2+x=1$

The dependent variable $y$ is separate from the independent variable $x$, making this function explicitly written.

##### Implicit Function

$x^2+y^2 = 1$

The dependent variable $y$ is not separate from the independent variable $x$, making this function implicitly written.

#### Implicit Differentiation

Given an implicitly written function, $2x^3+2y^3 = 9xy$. We can find the derivative by doing the following

$$
\begin{aligned}
        2x^3+2y^3 = 9xy \\
        \frac{d}{dx}(2x^3+2^3) = \frac{d}{dx}(9xy)\\
        6x^2 + 6y^2\frac{dy}{dx} = (9)(y) + (9x)\frac{dy}{dx}\\
        6x^2=9y = 9x\frac{dy}{dx} - 6y^2\frac{dy}{dx}\\
        6x^2=9y= (9x-6y^2)\frac{dy}{dx}\\
        &=  \frac{6x^2-9y}{9x-6y^2} = \frac{dy}{dx}
\end{aligned}
$$
