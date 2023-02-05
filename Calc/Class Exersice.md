$$
\begin{align}
    \lim_{t \to 4} t^2+5t+1 \\
    \lim_{t \to 2} \frac{t^2-2}{t^2+t-6} \\
    \lim_{x \to 5} \frac{x^2-x}{x^2+2x-3} \\
    \lim_{h \to 0} \frac{(1+h)^2-1}{h} \\
    \lim_{t \to 0} \frac{(t+4)^2-16}{t} \\
    \lim_{x \to 0} \frac{\sqrt{x+2} - \sqrt{2}}{x} \\
    \lim_{x \to 1} \frac{x-1}{\sqrt{x^2 +3} -2} \\
    \lim_{x \to -1} \frac{x}{(x+1)^2} \\
    \lim_{x \to -\infin} \frac{x^3-2x^2+1}{x^{4}-2} \\
    \lim_{x \to -\infin} \frac{-x^5-x^3+x-3}{2x^3+3x -2} \\
    \lim_{x \to \infin} \frac{x^4-5x^2+x-1}{3x^4+x-1} \\
    \lim_{x \to -\infin} \frac{x^3+\sqrt{4x^6+4}}{5x^3+2x} \\
    \text{For the function} f(x) =
    \begin{cases}
    x^3-2, & \text{if } x \geq 2\\
    1+x^2, & \text{if } x < 2
    \end{cases} && \text{find the } \lim_{x \to 1} f(x)
\end{align}
$$

###### Q1.

$$
\begin{align*}
    \lim_{t \to 4} t^2+5t+1 \\
    &= (4)^2 +5(4)+1 \\
    &= 16 +20 +1 \\
    &\lim_{t \to 4} t^2+5t+1 = 37
\end{align*}
$$

###### Q2.

$$
\begin{align*}

    \lim_{t \to 2} \frac{t^2-2}{t^2+t-6} \\
    &= \frac{t^2-2}{(t-2)(t+3)} \\
    &\therefore \lim_{t \to 2} \frac{t^2-2}{t^2+t-6} = \text{Does not exist} \\


\end{align*}
$$

###### Q3.

$$
\begin{align*}
    \lim_{x \to 5} \frac{x^2-x}{x^2+2x-3} \\
    & = \frac{5^2-5}{5^2+2(5)-3} \\
    &= \frac{25-5}{25+10-3} \\
    &= \frac{20}{32}\\
    &\lim_{x \to 5} \frac{x^2-x}{x^2+2x-3}  = \frac{5}{8} \\
\end{align*}
$$

###### Q4.

$$
\begin{align*}
    \lim_{h \to 0} \frac{(1+h)^2-1}{h} \\
    &= \frac{h^2+2h}{h} \\
    &= h+2 \\
    & \lim_{h \to 0} \frac{(1+h)^2-1}{h} = 2 \\
\end{align*}
$$

###### Q5.

$$
\begin{align*}
    \lim_{t \to 0} \frac{(t+4)^2-16}{t} \\
    &= \lim_{t \to 0} \frac{t^2+8t}{t} \\
    &= \lim_{t \to 0} (t+8) \\
    &= (0+8) \\
    & \lim_{t \to 0} \frac{(t+4)^2-16}{t} =8 \\
\end{align*}
$$

###### Q6.

$$
\begin{align*}

    \lim_{x \to 0} \frac{\sqrt{x+2} - \sqrt{2}}{x} \\
    &= \frac{\sqrt{x+2} -\sqrt{2}}{x} \times \frac{\sqrt{x+2} + \sqrt{2}}{\sqrt{x+2} + \sqrt{2}} \\
&=  \frac{(\sqrt{x+2} -\sqrt{2})(\sqrt{x+2} + \sqrt{2})}{x(\sqrt{x+2}+\sqrt{2})}\\
&= \frac{x+2-2}{x(\sqrt{x+2}+ \sqrt{2})} \\
&= \frac{1}{\sqrt{x+2}+ \sqrt{2}}\\
&= \frac{1}{\sqrt{0+2}+ \sqrt{2}} \\
& \lim_{x \to 0} \frac{\sqrt{x+2} - \sqrt{2}}{x} = \frac{\sqrt{2}}{4}\\
\end{align*}
$$

###### Q7.

$$
\begin{align*}

    \lim_{x \to 1} \frac{x-1}{\sqrt{x^2 +3} -2} \\
    &= \frac{x-1}{\sqrt{x^2+3}  -3} \times \frac{\sqrt{x^2+3}+2}{\sqrt{x^2+3}+2} \\
    &= \frac{(x-1)(\sqrt{x^2+3}+2)}{(\sqrt{x^2+3}-2)(\sqrt{x^2+3}+2)} \\
    &= \frac{(x-1)(\sqrt{x^2+3}+2)}{x^2+3-4} \\
    &= \frac{(x-1)(\sqrt{x^2+3}+2)}{x^2-1} \\
    &= \frac{(x-1)(\sqrt{x^2+3}+2)}{(x-1)(x+1)} \\
    &= \frac{\sqrt{x^2+3}+2}{x+1} \\
    &= \frac{\sqrt{1^2+3}+2}{1+1} \\
    &= \frac{4}{2} \\
    & \lim_{x \to 1} \frac{x-1}{\sqrt{x^2 +3} -2}= 2 \\
\end{align*}
$$

###### Q8.

$$
\begin{align*}
    \lim_{x \to -1} \frac{x}{(x+1)^2} \\
    &= \frac{x}{x^2+2x+1} \\
    &= \frac{x}{x(x+2+\frac{1}{x})} \\
    &= \frac{-1}{-1(-1+2-1)} \\
    &= \frac{-1}{0} \\
    &\lim_{x \to -1} \frac{x}{(x+1)^2} = -\infin  \\
\end{align*}
$$

###### Q9.

$$
\begin{align*}

    \lim_{x \to -\infin} \frac{x^3-2x^2+1}{x^{4}-2} \\
    &= \frac{\frac{1}{x}-\frac{2}{x^2}+\frac{1}{x^4}}{1-\frac{2}{x^4}} \\
    &=  \frac{-\frac{1}{\infin}-\frac{2}{\infin}+\frac{1}{\infin}}{1-\frac{2}{\infin}}\\
    &= \frac{0-0+0}{1-0} \\
    &\lim_{x \to -\infin} \frac{x^3-2x^2+1}{x^{4}-2} = 0  \\
\end{align*}
$$

###### Q10.

$$
\begin{align*}
    \lim_{x \to -\infin} \frac{-x^5-x^3+x-3}{2x^3+3x -2} \\
    &= \frac{x^3(-x^2-1+\frac{x}{x^3} -\frac{3}{x^3})}{x^3(2+\frac{3x}{x^3}-\frac{2}{x^3})} \\
    &= \frac{x^2-1+\frac{1}{x^2}-\frac{3}{x^3}}{2+\frac{3}{x^2}-\frac{2}{x^2}} \\
    &= \frac{-\infin-1+0+0}{2+0+0} \\
    &= \frac{-\infin-1}{2} \\
    &\lim_{x \to -\infin} \frac{-x^5-x^3+x-3}{2x^3+3x -2} = -\infin  \\
\end{align*}
$$

###### Q11.

$$
\begin{align*}

    \lim_{x \to \infin} \frac{x^4-5x^2+x-1}{3x^4+x-1} \\
    &= \frac{x^4(1-\frac{5x^2}{x^4}+\frac{x}{x^4}-\frac{1}{x^4})}{x^4(3+\frac{x}{x^2}-\frac{1}{x^4})} \\
    &= \frac{1-\frac{5}{x^2}+\frac{1}{x^3}-\frac{1}{x^4}}{3+\frac{1}{x^2}-\frac{1}{x^4}} \\
    &= \frac{1-\frac{5}{\infin}+\frac{1}{\infin}-\frac{1}{\infin}}{3+\frac{1}{\infin}-\frac{1}{\infin}} \\
    &= \frac{1-0+0-0}{3+0-0} \\
    & \lim_{x \to \infin} \frac{x^4-5x^2+x-1}{3x^4+x-1} = \frac{1}{3}\\
\end{align*}
$$

###### Q12.

$$
\begin{align*}

    \lim_{x \to -\infin} \frac{x^3+\sqrt{4x^6+4}}{5x^3+2x} \\
    &=  \\
    &= \frac{x^3+2\sqrt{x^6+1}}{5x^3+2x} \\
    &= \frac{x^3(1-2\sqrt{1+\frac{1}{x^6}})}{x^3(5+\frac{2}{x^2})} \\
    &= \frac{1-2\sqrt{1+\frac{1}{x^6}}}{5+\frac{2}{x^2}} \\
    &= \frac{1-2\sqrt{1+0}}{5+0} \\
    & \lim_{x \to -\infin} \frac{x^3+\sqrt{4x^6+4}}{5x^3+2x} = -\frac{1}{5} \\
\end{align*}
$$

###### Q13.

$$
\begin{align*}
    \lim_{x \to 1} f(x) \\
    &=  \\


\end{align*}
$$
