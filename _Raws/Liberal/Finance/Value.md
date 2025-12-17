# Valuation Concepts

The value of money, it's purchasing power, tends to be different at different time due to inflation/deflation. The nominal value of cash flows should be adjusted accordingly to obtain the real value of cash flows.

## Methods of Interest Computation

### Interest

The cost of borrowing money or the return on investment is often expressed as interest. There are two primary methods of calculating interest: simple interest and compound interest. Interest is needed because:

- The opportunity cost of money - To compensate them for the opportunity cost of forgoing the possible returns from alternative investments.
- The risk of losing money - To compensate them for risks they bear due to future uncertainties. 

#### Determination of Market Interest Rate

The nominal/quoted interest rate on a security is determined as:
$$
k^* + IP + DRP + LP + MRP = NIR
$$

Where:

- $k^*$ - Real risk-free rate of interest
- IP - Inflation Premium, i.e. compensation for reduced purchasing power due to inflation
- DRP - Default Risk Premium, i.e. compensation for risk of default by borrower
- LP - Liquidity Premium, i.e. offset the inconvenience of not being able to sell a security for cash at maturity
- MRP - Maturity Risk Premium, i.e. longer duration security should pay higher rate.
- NIR - Nominal Interest Rate

### Simple Interest
$$
SI = P_0 \times i \times t
$$

Where:

- $SI$ - Simple Interest in currency
- $P_0$ - Principal amount (initial investment)
- $i$ - Annual interest rate 
- $t$ - Time period

The future amount is the um of the Principal and Simple Interest:
$$
FV = P_0 + SI = P_0(1 + it)
$$

Or

$$
FV_t = P_0 [1 + it]
$$

The present value of a future receipt / payment is calculated using the formula:

$$
PV_0 = P_0 = \frac{FV_t}{1 + it}
$$


### Compound Interest

#### Amount Payable

The amount payable at the end of a specified future period is the aggregate of the principal and interest accrued.

##### With Periodic Compounding

$$
A_n = P_0 (1 + i)^n
$$

Where:

- $A_n$ - Amount after n periods
- $P_0$ - Principal amount (initial investment)
- $i$ - Interest rate per period
- $n$ - Number of compounding periods

#### With continuous compounding

$$
A_n = P_0 e^{in}
$$

Where:

- $A_n$ - Amount after n periods
- $P_0$ - Principal amount (initial investment)
- $i$ - Interest rate per period
- $n$ - Number of compounding periods

#### Interest Accrued

##### With Periodic Compounding

$$
CI = P_0 ((1 + i)^n - 1)
$$

Or

$$
CI = P_0 (1 + i)^n - P_0
$$

Or

$$
CI = A_n - P_0
$$

And the future value can be expressed as:
$$
FV = P_0 + CI
$$

##### With Continuous Compounding
$$
CI = P_0 (e^{in} - 1)
$$

Or

$$
CI = P_0 e^{in} - P_0
$$

### Multiple Compounding 

#### Periodic Compounding

When interest is accrued for fixed periods such as monthly, quarterly, semi-annually, etc.:

$$
A_n = P_0 \left(1 + \frac{i}{m}\right)^{mn}
$$

Where:

- $A_n$ - Amount after n years
- $P_0$ - Principal amount (initial investment)
- $i$ - Annual nominal interest rate
- $m$ - Number of compounding periods per year
- $n$ - Number of years

#### Continuous Compounding

When interest is compounded continuously, the formula is:
$$
A_n = P_0 e^{in}
$$

Where:

- $A_n$ - Amount after n years
- $P_0$ - Principal amount (initial investment)
- $i$ - Annual nominal interest rate
- $n$ - Number of years

#### Equivalent Periodic Rate (EPR)

The equivalent periodic rate (EPR) is the interest rate per compounding period that is equivalent to the nominal annual interest rate when compounding occurs multiple times per year. It can be calculated as:

$$
EPR = \frac{i}{m}
$$

### Nominal Rate vs. Effective Rate
> Nominal Interest Rate (NIR) - The face value cost of a loan, without taking compounding into account

> Effective Interest Rate (EIR) - The true cost of a loan after accounting for compounding within the year

#### Effective Annual Rate (EAR)
$$
EAR = \left(1 + HPR\right)^m - 1
$$

Where HPR is the holding period rate:
$$
HPR = \frac{i}{m}
$$

For example:
Jane is considering two investment options:

- Option A requires a deposit of GHS 10,0000 now. Interest will be paid on the deposit at an interest rate of 15\%
- Option B requires a deposit of GHS 10,0000 now. Interest will be paid on the deposit at an interest rate of 15\% compounded semi-annually.

1. Compute the effective annual interest rate for each option
$$
EAR = (1 + \frac{0.15}{1})^1 - 1 = 0.15
$$

$$
EAR = (1 + \frac{0.15}{2})^2 - 1 = 0.155625
$$

2. Compute the future value of each of the options.
$$
FV = 10,000 (1 + 0.15) = 11500
$$

$$
FV = 10,000 (1 + 0.155625) = 11556.25
$$

3. Which option is better.

   Option B is better for Jane because she earns more.

## Cash Flow Patterns

### Forms of Annuity

> Annuity - A series of equal payments occurring within a fixed time interval

- Ordinary Annuity - Payments or cash receipts occur at the end of each period (In arreas)
- Annuity Due - Payments or receipts occur at the beginning of each period (In advance)

### Single Amount

Lump sum payment or one-off payment or bullet payment, I.e when only one payment or receipt occurs in a specified time frame.

#### Future (Compounded) Value 

$$
FV_t = P_0 (1 + i)^t = P_0 \times FVIF_{i,t}
$$

#### Present (Discounted) Value

$$
PV_0 = \frac{FV_t}{(1 + i)^t} = FV_t \times PVIF_{i,t}
$$

### Series of even cash flows

- Ordinary Annuity - Cash flows occur at the end of each period
- Annuity Due - Cash flows occur at the beginning of each period

#### Ordinary Annuity

#### Future (Compounded) Value

$$
FVA_t = PMT [\frac{(1 + i)^t - 1}{i}] = PMT \times FVIFA_{i,t}
$$

Where the $PMT$ is the periodic payment amount.

#### Present (Discounted) Value
$$
PVA_0 = PMT [\frac{1 - (1 + i)^{-t}}{i}] = PMT \times PVIFA_{i,t}
$$

#### Perpertuity

An ordinary annuity that occurs forever.

$$
PVA_{\infty} = \frac{PMT}{i}
$$

#### Annuity Due

##### Future (Compounded) Value

$$
FVAD_t = PMT [\frac{(1 + i)^t - 1}{i}] (1 + i) = PMT \times FVIFA_{i,t} \times (1 + i)
$$

##### Present (Discounted) Value
$$
PVAD_0 = PMT [\frac{1 - (1 + i)^{-t}}{i}] (1 + i) = PMT \times PVIFA_{i,t} \times (1 + i)
$$

### Series of uneven cash flows

- Mixed cash flows - Cash flows that vary in amount and timing

#### Mixed Flows

##### Future (Compounded) Value
$$
FVV_t = \sum_{k=1}^{n} CF_k (1 + i)^{t - k}
$$

##### Present (Discounted) Value
$$
PVV_0 = \sum_{k=1}^{n} \frac{CF_k}{(1 + i)^k}
$$

### Dealing with Multiple Compounding In FV and PV Computations

When interest is compounded more than once in a year, you may use the EPR in place of the annual nominal rate and convert the time from years in to number of compounding periods. You may also use the EAR in place of the nominal rate and keep the time in years.

## Implied Interest Rate

### Single Amount

You may want to determine the interest rate at which an initial deposit will grow to achieve a target terminal value at the end of a certain number of periods. 

- First using the FV formula, rearranged to solve for i:
$$
i = \left(\frac{FV_t}{P_0}\right)^{\frac{1}{t}} - 1
$$
- Alternatively, using the PV formula, rearranged to solve for i:
$$
i = \left(\frac{FV_t}{P_0}\right)^{\frac{1}{t}} - 1
$$


