---
title: Trigonometry and Derivatives
author: Madiba Hudson-Quansah
creator: Madiba Hudson-Quansah
subject: Calculus 1
tags:
    - Calculus
    - Derivatives
    - Trigonometry
---

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

### Derivative of $\sin(x)$

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
 = \lim_{h \to 0} \frac{\sin(\cos(h) -1 )}{h} + \lim_{h \to 0} \frac{\cos(x)\sin(h)}{h}\\[20pt]
\because \lim_{x \to a} f(x) + \lim_{x \to a} g(x) = \lim_{x \to a}(f(x) + g(x))    \\[20pt]
 = \sin(x)\lim_{h \to 0}  \frac{\cos(h) -1 }{h} + \cos(x)\lim_{h \to 0} \frac{\sin(h)}{h} \\[20pt]
 \because \lim_{x \to a} (kf(x)) = k \lim_{x \to a} f(x) \\[20pt]
 \lim_{h \to 0^{-}}\frac{\cos(h) -1 }{h} = 0 \\
 \lim_{h \to 0^{+}} \frac{\cos(h) -1 }{h} = 0 \\
 \therefore  \lim_{h \to 0} \frac{\cos(h) -1 }{h} =  0\\
 = \sin(x) \times 0 +\cos(x)\lim_{h \to 0} \frac{\sin(h)}{h}\\
= \cos(x)\lim_{h \to 0} \frac{\sin(h)}{h}\\
\lim_{h \to 0^{-}} \frac{\sin(h)}{h} = 1 \\
\lim_{h \to 0^{+}} \frac{\sin(h)}{h} = 1 \\[20pt]
\therefore \lim_{h \to 0} \frac{\sin(h)}{h} = 1 \\
\therefore \cos(x)\lim_{h \to 0} \frac{\sin(h)}{h} = \cos(x) \times 1\\[20pt]
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

## Tangent

$$
\begin{aligned}
   f(x) = &\tan(x) \\
   y = &\tan(x) = 0\\
   & \sin(x) = 0
\end{aligned}
$$

###### Vertical Asymptote

> A vertical line $(x,0)$ where the values of a function rise or fall infinitely.

The line $x=a$ is a vertical asymptote of $f(x)$ if

$$
\begin{aligned}
   \lim_{x \to a} f(x) = \pm \infty
\end{aligned}
$$

The zero points of $\cos(x)$ create a vertical asymptote in relation to $\tan(x)$

### Derivative of $tan(x)$

If $y=\tan(x)$

$$
y^{\prime} = \sec^2(x)
$$

###### Proof

$$
\begin{aligned}
    y = \tan(x) = \frac{\sin(x)}{\cos(x)} \\[20pt]
y^{\prime} = \frac{\cos(x)(\cos(x))- \sin(x)(-\sin(x))}{(\cos(x))^2} \\[20pt]
\because y^{\prime} = \frac{v \times u^{\prime} - u \times v^{\prime}}{v^2} \\
y^{\prime} = \frac{\cos^2(x) + \sin^2(x)}{\cos^2(x)} \\
y^{\prime} = \frac{\cos^2(x)}{\cos^2(x)} + \frac{\sin^2(x)}{\cos^2(x)}\\
y^{\prime} = 1 + (\frac{\sin(x)}{\cos(x)})^2\\
y^{\prime} = 1 + \tan^2(x)\\
&= \sec^2(x)
\end{aligned}
$$

## Secant

$$
\begin{aligned}
f(x) = \sec(x) \\
\sec(0) = 1
\end{aligned}
$$

### Derivative of $\sec(x)$

If $y=\sec(x)$

$$
y^{\prime} = \tan(x)\sec(x)
$$

## Relationships

$$
\begin{aligned}
\cos(x-\frac{\pi}{2}) = \sin(x) \\
\sin(x + \frac{\pi}{2}) = \cos(x)
\end{aligned}
$$

## Identities

###### Reciprocal Identities

$$
\begin{aligned}
   \sin(\theta) = \frac{1}{\csc(\theta)} \text{ or } \csc(\theta) = \frac{1}{\sin(\theta)} \\[20pt]
\cos(\theta) = \frac{1}{\sec(\theta)} \text{ or } \sec(\theta) = \frac{1}{\cos(\theta)} \\[20pt]
\tan(\theta) = \frac{1}{\cot(\theta)} \text{ or } \cot(\theta) = \frac{1}{\tan(\theta)}
\end{aligned}
$$

###### Pythagorean Identities

$$
\begin{aligned}
   \sin^2(\theta) + \cos^2(\theta) = 1\\
   1 + \tan^2(\theta) = \sec^2(\theta) \\
   \csc^2(\theta) = 1 + \cot^2(\theta)
\end{aligned}
$$

###### Ratio Identities

$$
\begin{aligned}
   \tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)} \\
   \cot(\theta) = \frac{\cos(\theta)}{\sin(\theta)}
\end{aligned}
$$

###### Sum and Difference of Angles

$$
\begin{aligned}
   \sin(\alpha + \beta) = \sin(\alpha) \times \cos(\beta) + \cos(\alpha) \times \cos(\beta) \\
   \sin(\alpha-\beta) = \sin(\alpha)  \times \cos(\beta) - \cos(\alpha)  \times \sin(\beta) \\
   \cos(\alpha+\beta) = \cos(\alpha)  \times \cos(\beta) - \sin(\alpha)  \times  \sin(\beta) \\
   \cos(\alpha - \beta) = \cos(\alpha)  \times \cos(\beta) + \sin(\alpha)  \times  \sin(\beta) \\
   \tan(\alpha + \beta) = \frac{\tan(\alpha) + \tan(\beta)}{1- \tan(\alpha)  \times  \tan(\beta)} \\
   \tan(\alpha - \beta) = \frac{\tan(\alpha) - \tan(\beta)}{1+ \tan(\alpha)  \times  \tan(\beta)}
\end{aligned}
$$

###### Double Angles

$$
\begin{aligned}
   \sin(2\theta) = 2\sin(\theta) \cos(\theta) \\
   \cos(2\theta) = \cos^2(\theta) - \sin^2(\theta) \\
   = 2\cos^2(\theta) - 1 \\
   = 1- 2 \sin^2(\theta) \\
   \tan(2\theta)= \frac{2\tan(\theta)}{1 - \tan^2(\theta)}
\end{aligned}
$$

## Questions

$y = (\sin x)^{2}$

$$
\begin{aligned}
   y^{\prime} = 2\cos(\sin x)
\end{aligned}
$$

$y = \cos(5x+4)$

$$
\begin{aligned}
   y^{\prime} = -5\sin (5x+4)
\end{aligned}
$$

<br/>

$$
\begin{aligned}
   g(x) = 3 \sec(x) - 10 \tan(x) \\[20pt]
   h(x) = 3w^{-4} - w^2 \tan(w) \\[20pt]
   y = 5 \sin(x) \cos(x) + 9 \sec(x) \\[20pt]
   y = \frac{\sin(t)}{3-2 \cos(t)}\\[20pt]
   y = \sin(10x) \\[20pt]
   f(w) = \tan(w) \sec(w) \\[20pt]
   y = 2 \sin(3x+ \tan(x))\\[20pt]
   h(z) = \sin(z^{6}) + \sin^{6}(2) \\[20pt]
   f(t) = \sin(2t) + \cos(4t) \\[20pt]
   f(x) = [\sqrt[3]{2x} + \sin^2(3x)]^{-\frac{1}{2}} \\[20pt]
   y = \frac{4 \sin(x^2)}{\cos(x^2)} \\[20pt]
   h(x) = x^2 \cos(x^3) \\[20pt]
   y = \sqrt{5z+ \tan(4z)}
\end{aligned}
$$

Q1. $g(x) = 3 \sec(x) -10 \tan(x)$

$$
\begin{aligned}
   g^{\prime}(x) = 3(\tan(x) \sec(x)) - 10 \sec(x) \\
   = 3 \tan(x) \sec(x) - 10 \sec^2(x) \\
   = \sec(x) (3 \tan(x) - 10 \sec(x)) \\
&   g^{\prime}(x) = \sec(x) (3 \tan(x) - 10 \sec(x))
\end{aligned}
$$

Q2. $h(w) = 3w^{-4} -w^2 \tan(w)$

$$
\begin{aligned}
   h^{\prime}(w) = -12w^{-5} - (2w)(\tan(w)) + (w^2)(\sec^2(w)) \\
&   h^{\prime}(w) = -12w^{-5} - 2w \tan(w) - w^2 \sec^2(w)
\end{aligned}
$$

Q3. $y=5 \sin(x) \cos(x) + 4 \sec(x)$

$$
\begin{aligned}
   y^{\prime} = 5[\cos(x) \times \cos(x) - \sin(x)  \times  \sin(x)]  + 4 \tan(x) \sec(x)\\
   y^{\prime} = 5(\cos^2(x) - \sin^2(x)) + 4 \tan(x) \sec(x) \\
   &y^{\prime} = 5 \cos(2x) + 4 \tan(x) \sec(x)
\end{aligned}
$$

Q4. $y= \frac{\sin(t)}{3-2 \cos(t)}$

$$
\begin{aligned}
   y^{\prime}  =\frac{(\cos(t) (3-2 \cos(t))) - (2 \sin(t))(\sin(t))}{(3-2 \cos(t))^2} \\
   y^{\prime} = \frac{3 \cos(t) - 2 \cos^2(t) - 2 \sin^2(t)}{(3-2 \cos(t))^2} \\
   y^{\prime} = \frac{3 \cos(t) - 2(\cos^2(t) + \sin^2(t))}{(3-2 \cos(t))^2} \\
 & y^{\prime} = \frac{3 \cos(t) - 2}{(3-2 \cos(t))^2}
\end{aligned}
$$

Q5. $y = \frac{\sin(10z)}{z}$

$$
\begin{aligned}
   y^{\prime} = \frac{(10 \cos(10z))(z) - (1)(\sin(10z))}{z^2} \\
   &y^{\prime} = \frac{10z \cos(10z) - \sin(10z)}{z^2}
\end{aligned}
$$

Q6. $f(w) = \tan(w) \sec(w)$

$$
\begin{aligned}
   f^{\prime}(w) = (\sec^2(w))(\sec(w)) + (\sec(w) \tan(w))(\tan(w)) \\
   = \sec^3(w) + \sec(w) \tan^2(w)\\
   & f^{\prime}(w) = \sec(w) (\sec^2(w) + \tan^2(w))
\end{aligned}
$$

Q14. $y = \sqrt{5z +\tan(4z)}$

$$
\begin{aligned}
   y = (5z + \tan(4z))^{\frac{1}{2}} \\
   y^{\prime} = (\frac{1}{2})(5+4 \sec^2(4z))(5z+ \tan(4z))^{-\frac{1}{2}} \\
&   y^{\prime} = \frac{\frac{5}{2} + 2 \sec^2(4z)}{\sqrt{5z+\tan(4z)}}
\end{aligned}
$$
