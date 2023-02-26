---
title: Limit of a Function
author: Madiba Hudson-Quansah
creator: Madiba Hudson-Kansai
subject: Calculus 1
tags:
    - Calculus
    - Limit
---

Reporting about the behaviour of a function within the range of its dangerous values.

$$
f(x) = x^2 + {1\over x}
$$

Input variable - $x$

Output - $f(x)$

Name of function - $f$

"Acceptable"/Permissible input values of x - All real numbers except zero

$$
\begin{aligned}
(x, f(x)), (x+h, f(x+h)) \\
{f(x+h) - f(x)} \over {x+h-x} \\
f(x+h) - f(x) \over h \\
\end{aligned}
$$

##### Proof

$$
y= -16t^2+100t+6
$$

Points used:
$(0,6),(1, 90),(3, 162)$

When $t=0$ and $y=6$

$$
\begin{aligned}
y = at^2 + bt+c \\
6 = a(0)^2 + b(0) +c\\
&c = 6
\end{aligned}
$$

When $t=1$ and $y=90$

$$
\begin{aligned}
90 = a(1)^2 +b +6\\
90 = a + b + 6 \\
84 = a + b \\
84 - b = a
\end{aligned}
$$

When $t=3$ and $y=162$

$$
\begin{aligned}
162 = a(3)^2 +3b + 6 \\
162 = 9a + 3b + 6 \\
162 = 9(84 - b) + 3b + 6 \\
162 = 756 - 9b +3b +6\\
-594 = -6b +6 \\
-600 = -6b\\
&b = 100
\end{aligned}
$$

$\therefore$ $b = 100$

$$
\begin{aligned}
84 - 100 = a \\
& a = -16
\end{aligned}
$$

Therefore $a=-16$, $b=100$, and $c=6$

##### Given $f(x) = x^2$, find the Limit of $f(x)$ at $x=3$

$$
\begin{aligned}
\text{As x} \to 3^-, \text{ } f(x) \text{->} 9 \\
\text{As x} \to 3^+, \text{ } f(x) \text{->} 9
\end{aligned}
$$

Or

$$
\begin{aligned}
\lim_{x\to3^-} f(x) =9 \\
\lim_{x\to3^+} f(x) = 9
\end{aligned}
$$

The first $9$ is known as the left limit of $f(x)$ and the other $9$ is known as the right limit of $f(x)$

The Limit of $f(x)$ at $x=3$

$$
\begin{aligned}
\lim_{x\to3} f(x) = 9
\end{aligned}
$$

This is because the left limit and right limit converge.

###### In the case where:

$$
\begin{aligned}
\lim_{x\to1^-} f(x) = 5 \\
\lim_{x\to1^+} f(x) = 4
\end{aligned}
$$

The left and right limits do not converge so there is no limit of $f(x)$ for $x = 1$

$$
\begin{aligned}
\lim_{x\to1} f(x) = \text{No such unique number} \\
\therefore \text{The limit of } f(x) \text{ at } x= 1 \text{ does not exist}
\end{aligned}
$$

###### In the case where the one limit does not exist (increasing without bounds):

$$
\begin{aligned}
\lim_{x \to 1^-} f(x) \to \infty \\
\lim_{x \to 1^+} f(x) \to 4
\end{aligned}
$$

The limit does not exist because the left limit does not exist.

$$
\begin{aligned}
\lim_{x\to1} f(x) = \text{does not exist} \\
\because \text{ the left limit does not exist}
\end{aligned}
$$

### Graphical

Given $f(x) = x^2$, evaluate the Limit of $f(x)$ at $x=3$ using the graphical approach.
