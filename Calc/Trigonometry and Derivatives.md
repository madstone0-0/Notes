#Trigonometry and Derivatives

## Sine

$$
\begin{align*}
f(x) = \sin(x)\\
-1 \leq \sin(x) \leq 1\\
\sin(0) = 0
\end{align*}
$$

For all integer multiples of $\pi$, $\sin$ attains 0

$$
\sin(k\pi) = 0,  \text{ Where k is an integer}
$$

The graph of sine is periodic with a period of $2\pi$, meaning it repeats itself every interval of $2\pi$

### Derivatives of $\sin(x)$

If $y=\sin(x)$

$$
y^{\prime} = \cos(x)
$$

###### Proof

$$
\begin{align*}
    y^{\prime} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} \\
 \frac{\sin(x+h) -\sin(x)}{h} \\
    \therefore \frac{\sin(x+h) -\sin(x)}{h} \\
    \frac{\sin(x)\cos\left(h\right) + \cos\left(x\right)\sin\left(h\right) - \sin\left(x\right)}{h} \\
    \frac{\sin(\cos(h)-1) + \cos(x)\sin(h)}{h} \\
    y^{\prime} = \lim_{h \to 0} \frac{\sin(\cos(h)-1) + \cos(x)\sin(h)}{h} \\
    y^{\prime} = \lim_{h \to 0} \frac{\sin(\cos(h) -1 )}{h} + \frac{\cos(x)\sin(h)}{h}\\
 = \lim_{h \to 0} \frac{\sin(\cos(h) -1 )}{h} + \lim_{h \to 0} \frac{\cos(x)\sin(h)}{h}\\
\because \lim_{x \to a} f(x) + \lim_{x \to a} g(x) = \lim_{x \to a}(f(x) + g(x))    \\
 = \sin(x)\lim_{h \to 0}  \frac{\cos(h -1 )}{h} \\
 \because \lim_{x \to a} (kf(x)) = k \lim_{x \to a} f(x)
\end{align*}
$$

## Cosine

$$
\begin{align*}
f(x) = \cos(x)\\
-1 \leq \cos(x) \leq 1 \\
\cos(0) = 1
\end{align*}
$$

## Relationships

$$
\begin{align*}
\cos(x-\frac{\pi}{2}) = \sin(x) \\
\sin(x + \frac{\pi}{2}) = \cos(x)
\end{align*}
$$
