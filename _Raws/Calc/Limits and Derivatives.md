---
title: Limits and Derivatives
author: Madiba Hudson-Quansah
creator: Madiba Hudson-Quansah
subject: Calculus 1
tags:
    - Calculus
    - Limits
    - Derivatives
---

###### Case 1

Changing input values, output values remain the same $\therefore$ The change in $y$ with respect to changes $x$ values is $0$.

This function is called a constant function

$$
f(x) = k, \text{ for all input } x
$$

###### Case 2

Changing input values result in changing output values/ different output values.

$$
f(x) = \text{ not a constant function}
$$

###### Case 3

Changing input values result in a constant change in output values.

$$
\Delta f(x) = \text{ constant}
$$

This function is called a linear function.

###### Case 4

Changing input values result in a non constant change in output values

$$
\Delta f(x) = \text{ not constant}
$$

#### Questions

1. Find the derivative of $f(x) = x^2$ at $x=1$

$$
\begin{aligned}
{\frac{d}{dx}f(x)}_{x\to 1^-}  = 2 \\
{\frac{d}{dx}f(x)}_{x\to 1^+}  = 2 \\
& \frac{d}{dx} x^2 = 2  \\
\end{aligned}
$$

2. Investigate the existence or otherwise the derivatives if the following functions:

$$
\begin{aligned}
f(x) =\begin{cases}
x^2, & \text{if } \leq 2  \\
 1+2x& \text{if } > 2
\end{cases}
\text{at }x=2  \\
\end{aligned}
$$

$$
\begin{aligned}
g(x) = |x| = \begin{cases}
-x, & \text{if } x<0  \\
 x, & \text{if } x \geq 0
\end{cases}
\text{at } x= 0 \\
\end{aligned}
$$

Q1.

$$
\begin{aligned}
\frac{d}{dx}f(x)_{x\to 2^{-}}  = 4 \\
\frac{d}{dx}f(x)_{x\to 2^{+}}  = \text{is not constant}
\end{aligned}
$$

Q2.

$$
\begin{aligned}
\frac{d}{dx}g(x)_{x\to 0^-} = 1 \\
\frac{d}{dx}g(x)_{x \to 0^+} = 1 \\
&= \frac{d}{dx}g(x) = 1
\end{aligned}
$$

## Derivatives

-   Slope or Gradient of a non-linear function
-   Derivative = $dy\over dx$ = Instantaneous rate of change of a function
-   Slope of a line = $\Delta y\over \Delta x$ = Average rate of change
-   Leverage average rate of change to obtain the instantaneous rate of change = **First Principle**
    $$
    \begin{aligned}
        \frac{dy}{dx} = \lim_{h \to 0} \frac{f(x+h)- f(x)}{h}
    \end{aligned}
    $$
-   The derivative is a function at a point and a number at another point

###### Secant

> A line going though two points on a curve

#### Questions

Q1. Find the derivative of $f(x) = x^2$ using first principle

$$
\begin{aligned}
    \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} \\
 \frac{(x+h)^2-x^2}{h} \\
 \frac{2hx+h^2}{h} \\
 2x + (0)\\
& \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} = 2x
\end{aligned}
$$

Q2. Find the derivative of $f(x) = \frac{1}{x}$ using first principle

$$
\begin{aligned}
    \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} \\
    \frac{df}{dx} = \lim_{h \to 0} (\frac{1}{(x+h)} - \frac{1}{x}) \div h \\
  \frac{-h}{x^2+hx} \div h \\
  \frac{-h}{x^2+hx} \times \frac{1}{h} \\
  -\frac{1}{x^2+hx} \\
  -\frac{1}{x^2+0x} \\
& \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} =   -\frac{1}{x^2} \\
\end{aligned}
$$

Q3. Find the derivative of $f(x)=\sqrt{x}$

$$
\begin{aligned}
    \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} \\
\frac{df}{dx} = \lim_{h \to 0}  = \frac{\sqrt{x+h} -\sqrt{x}}{h} \times \frac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}} \\
\frac{df}{dx} = \lim_{h \to 0} = \frac{(\sqrt{x+h}- \sqrt{x}) - (\sqrt{x+h}+ \sqrt{x})}{h(\sqrt{x+h}+ \sqrt{x})} \\
\frac{df}{dx} = \lim_{h \to 0} = \frac{x+h-x}{h(\sqrt{x+h}+ \sqrt{x})} \\
 \frac{df}{dx} = \lim_{h \to 0} = \frac{h}{h(\sqrt{x+h}+ \sqrt{x})} \\
 \frac{df}{dx} = \lim_{h \to 0} = \frac{1}{\sqrt{x+h} +\sqrt{x}} \\
 \frac{1}{\sqrt{x+0} +\sqrt{x}} \\
 \frac{1}{2\sqrt{x}} \\
    & \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} = \frac{1}{2\sqrt{x}} \\
\end{aligned}
$$

### Techniques of Differentiation

#### Power Rule

$$
\begin{aligned}
    y = x^n, \text{ n is a real number}\\
    \frac{dy}{dx} = nx^{n-1} \\
\end{aligned}
$$

#### Questions

$$
\begin{aligned}
    y = x^2 \\
    y = \frac{1}{x^2} \\
    y = \frac{1}{\sqrt{x}} +x^3-1 \\
    y = x^{-8} + 3x^2 \\
\end{aligned}
$$

Q1.

$$
\begin{aligned}
    y = x^2, \text{ n = 2}\\
    \frac{dy}{dx} =2x^{2-1}\\
&= 2x^1 \\
&= 2x \\
\end{aligned}
$$

Q2.

$$
\begin{aligned}
    y = \frac{1}{x^2} \\
    y = x^{-2}, \text{ n = -2} \\
    & y^{\prime} = -2x
\end{aligned}
$$

Q3.

$$
\begin{aligned}
    y = \sqrt{x} \\
    y = x^{\frac{1}{2}} \\
    y^{\prime} = \frac{x^{-\frac{1}{2}}}{2} \\
    y^{\prime} = \frac{1}{2\sqrt{x}}
\end{aligned}
$$

Q4.

$$
\begin{aligned}
    y = \frac{1}{\sqrt{x}} + x^3 -1 \\
    y^{\prime} = x^{-\frac{1}{2}} +x^3 -1 \\
    y^{\prime} = -\frac{1}{2}x^{-\frac{3}{2}} + 3x^2 \\
\end{aligned}
$$

Qi.

$$
\begin{aligned}
y = -x^{-8} + 3x^2 \\
y^{\prime} = -8x^{-9} + 6x
\end{aligned}
$$

#### Chain Rule

###### Chain Function

> A composite function i.e. $f[g]$

$$
\begin{aligned}
    y = (2x+1)^2 \\
    y^{\prime} = 4(2x+1) \\
\end{aligned}
$$

$$
\begin{aligned}
    y = (3x^2+2x)^5 \\
    y = (5)(6x+2)(3x^2+2x)^4 \\
    y= (30x+10)(3x^2+2x)
\end{aligned}
$$

#### Questions

$$
\begin{aligned}
    y = 15x^9 - 3x^{12} +5x - 46 \\
    y = 2t^6+7t^{-6}\\
    y = 8x^3-\frac{1}{3x^5} + x- 23 \\
    y = \sqrt{x} + 9\sqrt[3]{x^4} - \frac{2}{\sqrt[5]{x^2}} \\
    y = \sqrt[3]{x^2}(2x-x^2) \\
    y = \frac{2t^5+t^2-5}{t^2} \\
    y = 2x^3 + \frac{300}{x^3} + 4
\end{aligned}
$$

Q1. $y = 15x^9 - 3x^{12} +5x - 46$

$$
    y^{\prime} = 185x^{8} - 36x^{11} +5
$$

Q2. $y = 2t^6+7t^{-6}$

$$
    y^{\prime} = 12t^{5} = 42t^{-7}
$$

Q3. $y = 8x^3-\frac{1}{3x^5} + x- 23$

$$
\begin{aligned}
    y = 8x^3 - \frac{1}{3x^{5}} + x -23 \\
    y = 8x^3 - \frac{1}{3}x^{-5} + x -23 \\
    y^{\prime} = 24x^2 + \frac{5}{3}x^{-6} + 1
\end{aligned}
$$

Q4. $y = \sqrt{x} + 9\sqrt[3]{x^4} - \frac{2}{\sqrt[5]{x^2}}$

$$
\begin{aligned}
    y = \sqrt{x} + 9\sqrt[3]{7} - \frac{2}{\sqrt[5]{x^2}} \\
    y = x^{\frac{1}{2}} + 9(x^{7})^{\frac{1}{3}} - 2(x^2)^{-\frac{1}{5}} \\
    y = x^{\frac{1}{2}} + 9x^{\frac{7}{3}} - 2x^{-\frac{2}{5}} \\
    y^{\prime} = \frac{1}{2}x^{-\frac{1}{2}} +21x^{\frac{4}{3}} + \frac{4}{5}x^{-\frac{7}{5}} \\
    y^{\prime} = \frac{1}{2\sqrt{x}} + 21x^{\frac{4}{3}} + \frac{4}{5}x^{-\frac{7}{5}}
\end{aligned}
$$

Q5. $y = \sqrt[3]{x^2}(2x-x^2)$

$$
\begin{aligned}
    y = (x^2)^{\frac{1}{3}}(2x-x^2) \\
    y = x^{\frac{2}{3}}(2x-x^2) \\
    y = 2x^{\frac{5}{3}} - x^{\frac{2}{3}}\\
    y^{\prime} = \frac{10}{3}x^{\large\frac{2}{3}} - \frac{8}{3}x^{\large\frac{5}{3}}
\end{aligned}
$$

Q6. $\large{y = \frac{2t^5+t^2-5}{t^2}}$

$$
\begin{aligned}
y = 2t^3 + 1 -\frac{5}{t^2} \\
y = 2t^3 + 1 - 5t^{-2} \\
y^{\prime} = 6t^2 + 10t^{-3}
\end{aligned}
$$

Q7. $y = 2x^3 + \large{\frac{300}{x^3}} + 4$

$$
\begin{aligned}
    y = 2x^3 + 300x^{-3} + 4\\
    y^{\prime} = 6x^2 - 900x^{-4}
\end{aligned}
$$

#### Product Rule

Given $y=u\times v$

$$
\begin{aligned}
\frac{dy}{dx} = u^{\prime} \times v + v^{\prime} \times u
\end{aligned}
$$

Q1. $y=(x^2+1)(x^3-x)$

$$
\begin{aligned}
    y = (x^2+1)(x^3-x)\\
    y^{\prime} = (2x)(x^3-x) + (x^2+1)(3x^2-1) \\
    y^{\prime} = 2x^4 - 2x^2 + 3x^4 +2x^2-1 \\
    & y^{\prime} = 5x^4 -1
\end{aligned}
$$

Q2. $y=(6x^3-x)(10-20x)$

$$
\begin{aligned}
    y^{\prime} = (18x^2-1)(10-20x) + (-20)(6x^3-x) \\
    y^{\prime} = 180x^2 -10 -360x^3 + 20x  - 120x^3+20x \\
y^{\prime}  &= -480x^3+ 180x^2+ 40x - 10
\end{aligned}
$$

#### Questions

$$
\begin{aligned}
    y = (4t^2-t)(t^3-8t^2+12)\\
    y = (1+\sqrt{x^3})(x^{-3}-2\sqrt[3]{x})\\
    y = (4-t^2)(1+5t^2)\\
    y = (x-\frac{2}{x^2})(7-2x^3) \\
    y = (3-x)(1-2x+x^2)
\end{aligned}
$$

Q1. $y = (4t^2-t)(t^3-8t^2+12)$

$$
\begin{aligned}
    y^{\prime} = (8t- 1)(t^3-8t^2+12) + (3t^2-16t)(4t^2-t) \\
    y^{\prime} = 8t^{4} - 64t^3 + 96t - t^3 + 8t^2 -12 + 12t^{4} - 3t^3 - 64t^3 + 16t^2\\
    y^{\prime} = 20t^{4} -132t^3 + 24t^2 +96t -12 \\
\end{aligned}
$$

Q2. $y = (1+\sqrt{x^3})(x^{-3}-2\sqrt[3]{x})$

$$
\begin{aligned}
y = (1+(x^3)^{\frac{1}{2}})(x^{-3}-2\sqrt[3]{x}) \\
y = (1+x^{\frac{1}{2}})(x^{-3}-2(x^{\frac{1}{3}})) \\
y^{\prime} = (\frac{3}{2}x^{\frac{1}{2}})(x^{-3}-2x^{\frac{1}{3}}) + (-3x^{4} - \frac{2}{3}x^{-\frac{2}{3}}-\frac{2}{3}x^{\frac{5}{6}}) \\y^{\prime} = \frac{3}{2}x^{-\frac{5}{2}}-3x^{\frac{5}{6}} - 3x^{-4}-3x^{-\frac{5}{2}} - \frac{2}{3}x^{-\frac{2}{3}} - \frac{2}{3}x^{\frac{5}{6}} \\
y^{\prime} = -\frac{11}{3}x^{\frac{5}{6}} - \frac{3}{2}x^{-\frac{5}{2}} - \frac{2}{3}x^{-\frac{2}{3}} - 3x^{-4}
\end{aligned}
$$

Q3. $y = (4-t^2)(1+5t^2)$

$$
\begin{aligned}
    y^{\prime} = (-2t)(1+5t^2) + (10t)(4-t^2) \\
    y^{\prime} = -2t - 10t^3 + 40t - 10t^3\\
    y^{\prime} = 20t^3 + 38t
\end{aligned}
$$

Q4. $y = (x-\frac{2}{x^2})(7-2x^3)$

$$
\begin{aligned}
    y = (x-2x^{-2})(7-2x^3)\\
    y^{\prime} = (1+4x^{-3})(7-2x^3) + (-6x^2)(x-2x^{-2})\\
    y^{\prime} = 7 - 2x^3 + 28x^{-3} - 8x^{0} - 6x^3 + 12x^0\\
y^{\prime} = 7 - 2x^3 + 28x^{-3} - 8 - 6x^3 + 12\\
&y^{\prime} = -8x^3+\frac{28}{x^3}+11
\end{aligned}
$$

Q5. $y = (3-x)(1-2x+x^2)$

$$
\begin{aligned}
    y^{\prime} = (-1)(1-2x+x^2) + (2x-2)(3-x) \\
    y^{\prime} = -1 + 2x -x^2 + 6x-2x^2 - 6 +2x\\
y^{\prime} &= -7 + 10x - 3x^2
\end{aligned}
$$

#### Quotient Rule

Where $\large{y=\frac{f(x)}{g(x)}}$

$$
\begin{aligned}
    \frac{dy}{dx} = \frac{g(x) \times f^{^{\prime}}(x) - f(x) \times g^{^{\prime}}(x)}{(g(x))^2}
\end{aligned}
$$

Where $\large {y=\frac{u}{v}}$

$$
\begin{aligned}
y^{\prime} = \frac{v \times u^{\prime} - u \times v^{\prime}}{v^2}
\end{aligned}
$$

#### Questions
