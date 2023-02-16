# Trigonometry and Derivatives

## Sine

$$
\begin{aligned}
f(x) = \sin(x)\\
-1 \leq \sin(x) \leq 1\\
\sin(0) = 0
\end{aligned}
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
\begin{aligned}
    y^{\prime} = \lim_{h \to 0} \frac{f(x+h) -f(x)}{h} \\
 \frac{\sin(x+h) -\sin(x)}{h} \\
    \therefore \frac{\sin(x+h) -\sin(x)}{h} \\
    \frac{\sin(x)\cos\left(h\right) + \cos\left(x\right)\sin\left(h\right) - \sin\left(x\right)}{h} \\
    \frac{\sin(\cos(h)-1) + \cos(x)\sin(h)}{h} \\
    y^{\prime} = \lim_{h \to 0} \frac{\sin(\cos(h)-1) + \cos(x)\sin(h)}{h} \\
    y^{\prime} = \lim_{h \to 0} \frac{\sin(\cos(h) -1 )}{h} + \frac{\cos(x)\sin(h)}{h}\\
 = \lim_{h \to 0} \frac{\sin(\cos(h) -1 )}{h} + \lim_{h \to 0} \frac{\cos(x)\sin(h)}{h}\\
\because \lim_{x \to a} f(x) + \lim_{x \to a} g(x) = \lim_{x \to a}(f(x) + g(x))    \\
 = \sin(x)\lim_{h \to 0}  \frac{\cos(h) -1 }{h} + \cos(x)\lim_{h \to 0} \frac{\sin(h)}{h} \\
 \because \lim_{x \to a} (kf(x)) = k \lim_{x \to a} f(x) \\

 \lim_{h \to 0^{-}}\frac{\cos(h) -1 }{h} = 0 \\
 \lim_{h \to 0^{+}} \frac{\cos(h) -1 }{h} = 0 \\
 \therefore  \lim_{h \to 0} \frac{\cos(h) -1 }{h} =  0\\
 = \sin(x) \times 0 +\cos(x)\lim_{h \to 0} \frac{\sin(h)}{h}\\
= \cos(x)\lim_{h \to 0} \frac{\sin(h)}{h}\\
\lim_{h \to 0^{-}} \frac{\sin(h)}{h} = 1 \\
\lim_{h \to 0^{+}} \frac{\sin(h)}{h} = 1 \\
\therefore \lim_{h \to 0} \frac{\sin(h)}{h} = 1 \\
\therefore \cos(x)\lim_{h \to 0} \frac{\sin(h)}{h} = \cos(x) \times 1\\
&= \cos(x) \\




\end{aligned}
$$

## Cosine

$$
\begin{aligned}
f(x) = \cos(x)\\
-1 \leq \cos(x) \leq 1 \\
\cos(0) = 1
\end{aligned}
$$

## Relationships

$$
\begin{aligned}
\cos(x-\frac{\pi}{2}) = \sin(x) \\
\sin(x + \frac{\pi}{2}) = \cos(x)
\end{aligned}
$$
