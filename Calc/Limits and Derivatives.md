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
\begin{align}
f(x) =\begin{cases}
x^2, & \text{if } \leq 2  \\
&&& \text{at }x=2  \\
 1+2x& \text{if } > 2
\end{cases} \\


g(x) = |x| = \begin{cases}
-x, & \text{if } x<0  \\
&&& \text{at } x= 0 \\
x, & \text{if } x \geq 0
\end{cases}
\end{align}
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

##### Questions

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
