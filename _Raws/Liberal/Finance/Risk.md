# Risk and Return

## Return

The reward for investing money. Return comprises two components:  
- Income received on the investment  
- Changes in market price of the investment

## Risk

The variable of returns from those that are expected. The concept of risk captures the uncertainty about receiving the expected return on an investment.
- Risk free asset - Actual returns on such assets are not different from what is expected, e.g. Government securities 
- Risky asset - Actual returns on such assets are not guaranteed and so may differ from what is expected, e.e. Equity stocks

## Risk and Return Trade-off

In principle, a security with higher risk should pay a higher return to its investors, and a security with lower risk should pay a lower return to its investors.

## Measuring Return and Risk

The rate of return on an investment is calculated as:
$$
\text{Rate of Return} = \frac{\text{Investment Income} + \text{Change in Price}}{\text{Value of Asset Invested}}
$$

Risk is measured from a distribution of returns. The variance and standard deviation of returns are the most common measures of risk, and the higher the standard deviation the higher the variable in returns.

First, estimate the expected or average return in the distribution of returns: 
$$
E(R) = \sum_{i=1}^{n} R_i * P(R_i)
$$
Where:
- $E(R)$ - Expected return
- $R_i$ - Return in state i
- $P(R_i)$ - Probability of return in state i

Then estimate the variance in the distribution of returns:
$$
Var(R) = \sum_{i=1}^{n} P(R_i) * (R_i - E(R))^2
$$
Where:
- $Var(R)$ - Variance of returns
- $P(R_i)$ - Probability of return in state i
- $R_i$ - Return in state i
- $E(R)$ - Expected return

$$
Var(r) = \frac{1}{n-1} \sum_{s=1}^{n} (R_s - \bar{R})^2
$$

Where:
- $Var(r)$ - Variance of returns
- $n$ - Number of observations
- $R_s$ - Return in state s
- $\bar{R}$ - Average return

Finally the standard deviation is the square root of the variance:
$$
SD(R) = \sqrt{Var(R)}
$$

The probability that the stock return falls below the average return is a rough measure of downside risk. The probability that the stock return goes above the average return is an indicator of upside risk.

> Downside Risk - The risk of returns falling below some minimum acceptable level.

> Upside Risk - The chance of returns exceeding expectations.

### Comparing Risk on Different Securities

Standard deviation is an absolute measure of risk, so it is difficult to compare the risk of two securities using this. The coefficient of variation (CV) is a relative measure of risk that allows comparison of the risk of two securities. It is calculated as:
$$
CV = \frac{SD(R)}{E(R)}
$$
The greater the CV, the higher the risk per unit of return.

## Attitudes towards Risk

### Certainty Equivalent 

The amount of cash someone would require with certainty at a point in time to make the individual indifferent between that certain amount and an amount expected to be received with risk at the same point in time.

### Risk Aversion

Demand for higher expected return from an investment when its risk is higher. A risk adverse investor downgrades the utility from an investment higher below its expected return when risk is higher, thus they demand higher expected return to invest in high-risk securities. A risk neutral person is not sensitive to risk they only care about expected return. A risk loving person raises the utility from an investment higher over the expected returns when the risk is higher, thus they are willing to accept lower expected return to invest in high-risk securities.

### Certainty Equivalent and Risk Attitudes

The relationship between certainty equivalent and the risky expected return can be used to define investors attitude toward risk, i.e:
- Risk Averse: $CE < EV$
- Risk Neutral: $CE = EV$
- Risk Loving: $CE > EV$

Where, $CE$ is the certainty equivalent and $EV$ is the expected value of the risky return.

## Diversification

The processor of holding a portfolio of different investments to reduce risk. The covariance and correlation between the returns on the component assets is critical to the effectiveness of diversification in reducing risk.

> Correlation - A statistical measure that indicates the extent to which two or more variables fluctuate together. A positive correlation indicates the extent to which those variables increase or decrease in parallel; a negative correlation indicates the extent to which one variable increases as the other decreases.

For effective diversification the correlation between the component assets must be negative or low positive.

To obtain a portfolio with less than perfectly positive correlation:
- Invest in different asset classes, e.g. equities, bonds, real estate
- Invest in different companies 
- Invest in different industries
- Invest in different geographical locations

### Investment Portfolio

A combination of two or more securities or assets held by an investor. Investors usually invest in a portfolio by spreading their money over two or more assets, with the objective of reducing risk.

### Portfolio Return

The rate of return on a portfolio is the weighted average of the rate of returns on the component assets. It is calculated as:
$$
E(R_p) = \sum_{i=1}^{n} w_i * E(R_i)
$$

Where:
- $E(R_p)$ - Expected return on the portfolio
- $w_i$ - Proportion of the portfolio invested in asset i
- $E(R_i)$ - Expected return on asset i


In principle return on a portfolio lies between the minimum and maximum component asset returns. 

### Portfolio Risk

The risk on a portfolio is measured by the portfolio standard deviation and is calculated as:
$$
SD(R_p) = \sqrt{\sum_{i=1}^{n} \sum_{j=1}^{n} w_i * w_j * Cov(R_i, R_j)}
$$

Where:
- $SD(R_p)$ - Standard deviation of portfolio returns
- $w_i$ - Proportion of the portfolio invested in asset i
- $w_j$ - Proportion of the portfolio invested in asset j
- $Cov(R_i, R_j)$ - Covariance between returns on asset i and asset

The covariance between two assets is calculated as:
$$
Cov(R_i, R_j) = \rho_{i,j} * SD(R_i) * SD(R_j)
$$

Where:
- $Cov(R_i, R_j)$ - Covariance between returns on asset i and asset j
- $\rho_{i,j}$ - Correlation coefficient between returns on asset i and asset j
- $SD(R_i)$ - Standard deviation of returns on asset i
- $SD(R_j)$ - Standard deviation of returns on asset j

The portfolio risk depends on:
- The risk of the component assets
- The weights of the component assets in the portfolio
