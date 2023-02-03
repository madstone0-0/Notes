# Limit of a Function

Reporting about the behavior of a function within the range of its dangerous values.

$$
f(x) = x^2 + {1\over x}
$$

Input variable - $x$

Output - $f(x)$

Name of function - $f$

"Acceptable"/Permissible input values of x - All real numbers except zero

$$
\begin{align*}
(x, f(x)), (x+h, f(x+h)) \\
{f(x+h) - f(x)} \over {x+h-x} \\
f(x+h) - f(x) \over h \\
\end{align*}
$$

Left
| $x$ | $y$|
|---|---|
|1.1||
|1.2||
|1.3 | |
|1.4 | |
|1.5 | |
|1.6 | |
|1.7 | |
|1.8 | |
|1.9 | |
|1.99 | |

Right
| $x$ | $y$|
|---|---|
|2.9||
|2.8||
|2.7 | |
|2.6 | |
|2.5 | |
|2.4 | |
|2.3 | |
|2.2 | |
|2.1 | |
|2.11 | |

##### Proof

$$
y= -16t^2+100t+6
$$

Points used:
$(0,6),(1, 90),(3, 162)$

When $t=0$ and $y=6$

$$
\begin{align*}
y = at^2 + bt+c \\
6 = a(0)^2 + b(0) +c\\
&c = 6
\end{align*}
$$

When $t=1$ and $y=90$

$$
\begin{align*}
90 = a(1)^2 +b +6\\
90 = a + b + 6 \\
84 = a + b \\
84 - b = a
\end{align*}
$$

When $t=3$ and $y=162$

$$
\begin{align*}
162 = a(3)^2 +3b + 6 \\
162 = 9a + 3b + 6 \\
162 = 9(84 - b) + 3b + 6 \\
162 = 756 - 9b +3b +6\\
-594 = -6b +6 \\
-600 = -6b\\
&b = 100
\end{align*}
$$

$\therefore$ $b = 100$

$$
\begin{align*}
84 - 100 = a \\
& a = -16
\end{align*}
$$

Therefore $a=-16$, $b=100$, and $c=6$

##### Given $f(x) = x^2$, find the Limit of $f(x)$ at $x=3$

$$
\begin{align*}
\text{As x} \rightarrow 3^-, \text{ } f(x) \text{->} 9 \\
\text{As x} \rightarrow 3^+, \text{ } f(x) \text{->} 9
\end{align*}
$$

Or

$$
\begin{align*}
\lim_{x\rightarrow3^-} f(x) =9 \\
\lim_{x\rightarrow3^+} f(x) = 9
\end{align*}
$$

The first $9$ is known as the left limit of $f(x)$ and the other $9$ is known as the right limit of $f(x)$

The Limit of $f(x)$ at $x=3$

$$
\begin{align*}
\lim_{x\rightarrow3} f(x) = 9
\end{align*}
$$

This is because the left limit and right limit converge.

###### In the case where:

$$
\begin{align*}
\lim_{x\rightarrow1^-} f(x) = 5 \\
\lim_{x\rightarrow1^+} f(x) = 4
\end{align*}
$$

The left and right limits do not converge so there is no limit of $f(x)$ for $x = 1$

$$
\begin{align*}
\lim_{x\rightarrow1} f(x) = \text{No such unique number} \\
\therefore \text{The limit of } f(x) \text{ at } x= 1 \text{ does not exist}
\end{align*}
$$

###### In the case where the one limit does not exist (increasing without bounds):

$$
\begin{align*}
\lim_{x\rightarrow1^-} f(x) \rightarrow \infin \\
\lim_{x\rightarrow1^+} f(x) \rightarrow 4
\end{align*}
$$

The limit does not exist because the left limit does not exist.

$$
\begin{align*}
\lim_{x\rightarrow1} f(x) = \text{does not exist} \\
\because \text{ the left limit does not exist}
\end{align*}
$$

### Graphical

2023-01-27

Given $f(x) = x^2$, evaluate the Limit of $f(x)$ at $x=3$ using the graphical approach.
