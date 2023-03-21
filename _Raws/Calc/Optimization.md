---
title: Optimization
author: Madiba Hudson-Quansah
creator: Madiba Hudson-Quansah
subject: Calculus 1
tags:
    - Calculus
---

> Local - Subsection of range
>
> Global - Whole range

###### Maximize

-   Local Maximum - Maximum in specified range
-   Global Maximum - Overall maximum

    $$
    \begin{aligned}
        R(x) = 45 - \frac{x^2}{3}, \; 0 \leq x \leq 1 \\
        \text{Find all local maximum \underline{values} } \\
        \text{Find the global maximum \underline{value} }
    \end{aligned}
    $$

###### Minimize

-   Local Minimum - Minimum in specified range
-   Global Minimum - Overall minimum

### Local/Relative Maximum/Minimum (Optimum)

-   Find the critical values of the function:
    -   Stationary points, i.e. $f^{\prime}(?) = 0$
    -   Undefined points, i.e. $f^{\prime}(?) = \emptyset$
-   Assess them for potential local maximum/minimum:
    -   Find the first derivative, input values from the left and right of the critical points and check the change in signs:
        -   $+$ to $-$: Maximum
        -   $-$ to $+$: Minimum
    -   Find second derivative, input the critical values and check the sign:
        -   $+$: Minimum
        -   $-$: Maximum

### Global/Absolute Maximum/Minimum (Optima)

To find the Absolute Optima of a function whose domain is unrestricted:

$$
\begin{aligned}
    \begin{array}{c c}
        \lim_{x \to \infty} f(x) & \lim_{x \to -\infty} f(x)
   \end{array}
\end{aligned}
$$

#### Conditions for finding Absolute Optima easily

1. Closed Domain, i.e. $[x_1,x_2]$
2. Function is continuous for the duration of the closed domain

##### Extreme Value Theorem (EVT)

If a real valued function $f$ is continuous on the closed interval $[a,b]$, the $f$ must attain a maximum and minimum at least once.

$$
\begin{gathered}
    f(c) \geq f(x) \geq F(d) \\
    \forall x \in [a,b]
\end{gathered}
$$

Where $f(c)$ is the function's minimum value and $F(d)$ is the function's maximum value.

###### Example

$$
f(x)=x^3 \; \text{on } \; [-1,10]
$$

-   $f(x)$ is continuous due to it being a polynomial
-   The function's domain is closed due to the end values being included in the domain

By EVT $f(x)$ must attain absolute maximum and minimum at least once on the interval. Possibly at:

1. End points of the domain
2. Critical values of $f(x)$

$$
\begin{aligned}
    f(x) = x^3\\
    f^{\prime}(x) = 3x^2\\
    0 = 3x^2\\
    \frac{0}{3} = x^2\\
    0 = x \\[10pt]
    f(-1) = -1\\
    f(10) = 1000 \\[20pt]
    \therefore \text{Absolute Maximum is } 1000 \\
    \text{Absolute Minimum is } -1
\end{aligned}
$$

### Concavity

Let $f$ be a function that is differentiable over an open interval $I$

-   If $f^{\prime}$ is increasing over $I$, we say $f$ is concave up over $I$, i.e. $f^{\prime\prime} > 0$
-   If $f^{\prime}$ is decreasing over $I$, we say $f$ is concave down over $I$, i.e $f^{\prime\prime} < 0$

#### Inflection

A point where a function switches concavity, i.e

$$
\begin{gathered}
    f^{\prime\prime}(x^{-}) = +\text{ve } \; \text{to } \; f^{\prime\prime}(x^{+}) = -\text{ve }\\
    \text{or } \\
    f^{\prime\prime}(x^{-}) = -\text{ve } \; \text{to } \; f^{\prime\prime}(x^{+}) = +\text{ve }
\end{gathered}
$$

#### Curvature

###### Concave Up

The cave is facing up

###### Concave down

The cave is facing down
