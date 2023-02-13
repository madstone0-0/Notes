# Limits and Derivatives

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
\begin{align*}

{\frac{d}{dx}f(x)}_{x\to 1^-}  = 2 \\
{\frac{d}{dx}f(x)}_{x\to 1^+}  = 2 \\
& \frac{d}{dx} x^2 = 2  \\
\end{align*}
$$

2. Investigate the existence or otherwise the derivatives if the following functions:

$$

\begin{align*}
f(x) =\begin{cases}
x^2, & \text{if } \leq 2  \\
 1+2x& \text{if } > 2
\end{cases}
\text{at }x=2  \\
\end{align*}
$$

$$
\begin{align*}
g(x) = |x| = \begin{cases}
-x, & \text{if } x<0  \\
 x, & \text{if } x \geq 0
\end{cases}
\text{at } x= 0 \\
\end{align*}
$$

Q1.

$$
\begin{align*}

\frac{d}{dx}f(x)_{x\to 2^{-}}  = 4 \\
\frac{d}{dx}f(x)_{x\to 2^{+}}  = \text{is not constant}
\end{align*}
$$

Q2.

$$
\begin{align*}

\frac{d}{dx}g(x)_{x\to 0^-} = 1 \\
\frac{d}{dx}g(x)_{x \to 0^+} = 1 \\
&= \frac{d}{dx}g(x) = 1
\end{align*}
$$

## Derivatives

-   Slope or Gradient of a non-linear function
-   Derivative = $dy\over dx$ = Instantaneous rate of change of a function
-   Slope of a line = $\Delta y\over\Delta x$ = Average rate of change
-   Leverage average rate of change to obtain the instantaneous rate of change = **First Principle**
    $$
    \begin{align*}
        \frac{dy}{dx} = \lim_{h \to 0} \frac{f(x+h)- f(x)}{h}
    \end{align*}
    $$
-   The derivative is a function at a point and a number at another point

###### Secant

> A line going though two points on a curve

#### Questions

Q1. Find the derivative of $f(x) = x^2$ using first principle

$$
\begin{align*}
    \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} \\
 \frac{(x+h)^2-x^2}{h} \\
 \frac{2hx+h^2}{h} \\
 2x + (0)\\
& \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} = 2x
\end{align*}
$$

Q2. Find the derivative of $f(x) = \frac{1}{x}$ using first principle

$$
\begin{align*}

    \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} \\
    \frac{df}{dx} = \lim_{h \to 0} (\frac{1}{(x+h)} - \frac{1}{x}) \div h \\
  \frac{-h}{x^2+hx} \div h \\
  \frac{-h}{x^2+hx} \times \frac{1}{h} \\
  -\frac{1}{x^2+hx} \\
  -\frac{1}{x^2+0x} \\
& \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} =   -\frac{1}{x^2} \\


\end{align*}
$$

<br>

Q3. Find the derivative of $f(x)=\sqrt{x}$

$$
\begin{align*}

    \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} \\
\frac{df}{dx} = \lim_{h \to 0}  = \frac{\sqrt{x+h} -\sqrt{x}}{h} \times \frac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}} \\
\frac{df}{dx} = \lim_{h \to 0} = \frac{(\sqrt{x+h}- \sqrt{x}) - (\sqrt{x+h}+ \sqrt{x})}{h(\sqrt{x+h}+ \sqrt{x})} \\
\frac{df}{dx} = \lim_{h \to 0} = \frac{x+h-x}{h(\sqrt{x+h}+ \sqrt{x})} \\
 \frac{df}{dx} = \lim_{h \to 0} = \frac{h}{h(\sqrt{x+h}+ \sqrt{x})} \\
 \frac{df}{dx} = \lim_{h \to 0} = \frac{1}{\sqrt{x+h} +\sqrt{x}} \\
 \frac{1}{\sqrt{x+0} +\sqrt{x}} \\
 \frac{1}{2\sqrt{x}} \\

    & \frac{df}{dx} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} = \frac{1}{2\sqrt{x}} \\
\end{align*}
$$

### Techniques of Differentiation

#### Power Rule

$$
\begin{align*}
    y = x^n, \text{ n is a real number}\\
    \frac{dy}{dx} = nx^{n-1} \\

\end{align*}
$$

#### Questions

$$
\begin{align}
    y = x^2 \\
    y = \frac{1}{x^2} \\
    y = \frac{1}{\sqrt{x}} +x^3-1 \\
    y = x^{-8} + 3x^2 \\
\end{align}
$$

Q1.

$$
\begin{align*}
    y = x^2, \text{ n = 2}\\
    \frac{dy}{dx} =2x^{2-1}\\
&= 2x^1 \\
&= 2x \\
\end{align*}
$$

Q2.

$$
\begin{align*}
    y = \frac{1}{x^2} \\
    y = x^{-2}, \text{ n = -2} \\
    & y^{\prime} = -2x
\end{align*}
$$

Q3.

$$
\begin{align*}
    y = \sqrt{x} \\
    y = x^{\frac{1}{2}} \\
    y^{\prime} = \frac{x^{-\frac{1}{2}}}{2} \\
    y^{\prime} = \frac{1}{2\sqrt{x}}
\end{align*}
$$

Q4.

$$
\begin{align*}
    y = \frac{1}{\sqrt{x}} + x^3 -1 \\
    y^{\prime} = x^{-\frac{1}{2}} +x^3 -1 \\
    y^{\prime} = -\frac{1}{2}x^{-\frac{3}{2}} + 3x^2 \\

\end{align*}
$$

Qi.

$$
\begin{align*}
y = -x^{-8} + 3x^2 \\
y^{\prime} = -8x^{-9} + 6x

\end{align*}
$$

<br>

#### Chain Rule

###### Chain Function

> A composite function i.e. $f[g]$

$$
\begin{align*}

\end{align*}
$$

$$
\begin{align*}
    y = (2x+1)^2 \\
    y^{\prime} = 4(2x+1) \\
\end{align*}
$$

$$
\begin{align*}
    y = (3x^2+2x)^5 \\
    y = (5)(6x+2)(3x^2+2x)^4 \\
    y= (30x+10)(3x^2+2x)
\end{align*}


$$

#### Questions

$$
\begin{align*}
     y = 15x^9 - 3x^{12} +5x - 46 \\
    y = 2t^6+7t^{-6}\\
    y = 8x^3-\frac{1}{3x^5} + x- 23 \\
    y = \sqrt{x} + 9\sqrt[3]{x^4} - \frac{2}{\sqrt[5]{x^2}} \\
    y = \sqrt[3]{x^2}(2x-x^2) \\
    y = \frac{2t^5+t^2-5}{t^2} \\
    y = 2x^3 + \frac{300}{x^3} + 4
\end{align*}
$$

#### Product Rule

Given $y=u\times v$

$$
\begin{align*}
\frac{dy}{dx} = u\prime \times v + v\prime \times u
\end{align*}
$$

Q1. $y=(x^2+1)(x^3-x)$

$$
\begin{align*}
    y = (x^2+1)(x^3-x)\\
    y^{\prime} = (2x)(x^3-x) + (x^2+1)(3x^2-1) \\
    y^{\prime} = 2x^4 - 2x^2 + 3x^4 +2x^2-1 \\
    & y^{\prime} = 5x^4 -1
\end{align*}
$$

Q2. $y=(6x^3-x)(10-20x)$

$$
\begin{align*}
    y^{\prime} = (18x^2-1)(10-20x) + (-20)(6x^3-x) \\
    y^{\prime} = 180x^2 -10 -360x^3 + 20x  - 120x^3+20x \\
y^{\prime}  &= -480x^3+ 180x^2+ 40x - 10
\end{align*}
$$

#### Questions

$$
\begin{align*}
    y = (4t^2-t)(t^3-8t^2+12)\\
    y = (1+\sqrt{x^3})(x^{-3}-2\sqrt[3]{x})\\
    y = (4-t^2)(1+5t^2)\\
    y = (x-\frac{2}{x^2})(7-2x^3) \\
    y = (3-x)(1-2x+x^2)
\end{align*}
$$

#### Quotient Rule

Where $\large{y=\frac{f(x)}{g(x)}}$

$$
\begin{align*}
    \frac{dy}{dx} = \frac{g(x) \times f^{^{\prime}}(x) - f(x) \times g^{^{\prime}}(x)}{(g(x))^2}
\end{align*}
$$

Where $\large {y=\frac{u}{v}}$

$$
\begin{align*}
y^{\prime} = \frac{v \times u^{\prime} - u \times v^{\prime}}{v^2}
\end{align*}
$$

#### Questions
