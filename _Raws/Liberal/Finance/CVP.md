# Cost Volume Profit (CVP) Analysis

How changes in cost, volume and price, affect a company's profit.

## Key Concepts

### Variable Costs
Costs that vary in total in direct proportion to changes in activity level. Unit variable cost remains constant.

### Fixed Costs

Costs that remain constant in total as activity level changes. Unit fixed cost however reduces as activity level
increases.

#### Two Forms of Fixed Costs

1. Committed Fixed Costs: Organizational investments with multiyear planning horizon that cannot be significantly reduced
   without making fundamental changes. 

2. Discretionary Fixed Costs: Arise from annual management decision to spend on certain fixed cost items.

### Linearity Assumption

Assumes that the relationship between cost and activity level is linear within the relevant range.

### Cost Classification

#### Separating Mixed Costs

##### High-Low Method

Variable cost per unit is computed from cost details relating to the highest and lowest activity levels. I.e.
$$
\text{Unit Variable Cost} = \frac{\text{Cost at Highest Activity Level} - \text{Cost at Lowest Activity Level}}{\text{Highest Activity Level} - \text{Lowest Activity Level}}
$$

## CVP Analysis

### Marginal/Profit Analysis

#### Contribution Margin (CM)

The difference between total sales revenue (selling price) and total variable costs (unit variable cost). It is the proportion of sales that contributes to the recovery of fixed costs.
$$
\text{Unit CM} = \text{Selling Price per Unit} - \text{Unit Variable Costs}
$$

$$
\text{Total CM} = \text{Total Sales Revenue} - \text{Total Variable Costs}
$$

$$
\text{CM Ratio} = \frac{\text{Unit CM}}{\text{Selling Price per Unit}} \times 100\%
$$

### Break-Even Analysis

The determination of break-even point in units and currency value and margin of safety in units and currency value.

> Break-Even Point (BEP): The level of sales at which total revenue equals total costs, resulting in zero profit.

#### Break-Even Point Calculation

##### Equation Method

$$
\text{Profit} = \text{Sales} - \text{Total Variable Costs} - \text{Total Fixed Costs}
$$

Therefore, at break-even point where Profit = 0,
$$
0 = \text{Sales} - \text{Total Variable Costs} - \text{Total Fixed Costs}
$$

$$
\text{Sales} = \text{Total Variable Costs} + \text{Total Fixed Costs}
$$

##### Contribution Margin Method

Using Unit CM,
$$
\text{BEP (units)} = \frac{TFC}{\text{Unit CM}}
$$

Using CM Ratio,
$$
\text{BEP (currency value)} = \frac{TFC}{\text{CM Ratio}}
$$

#### Margin of Safety (MOS)

Excess of budgeted or actual sales over break-even sales. It indicates the amount by which sales can drop before incurring a loss.
$$
MOS (\text{units}) = \text{Actual Sales (units)} - \text{BEP (units)}
$$

$$
MOS (\text{currency value}) = \text{Actual Sales (currency value)} - \text{BEP (currency value)}
$$

##### Break-Even Analysis For Single Product

For a single product, the break-even point can be calculated directly using the unit contribution margin. For example

|                          | Total (GHC)           | Per Unit (GHC)     | Percent of Sales |
| ------------------------ | --------------------- | ------------------ | ---------------- |
| Sales (500,000 barrels)  | 30,000,000            | 60                 |  100%
| Less Variable Expenses   | <ins>18,000,000</ins> | 36                 | 60% 
| Contribution Margin      | 12,000,000            | 24                 | 40% 
| Less Fixed Expenses      | <ins>8,000,000</ins>  |                    |  
|  Net Income              | <ins>4,000,000</ins>  |                    |  

This is the contribution income statement for month ending 30th June. Suppose unit variable cost and total fixed cost will remain as shown in the June statement and planned sales volume is 500,000.
1. Compute the break-even point in units and sales value
$$
\text{Unit CM} = 60 - 36 = 24
$$

$$
BEP (\text{units}) = \frac{TFC}{\text{Unit CM}} = \frac{8,000,000}{24} = 333,333 \text{ barrels}
$$

$$
\text{CM Ratio} = \frac{24}{60} = 0.4
$$

$$
BEP (\text{GHC}) = \frac{8,000,000}{0.4} = 20,000,000
$$

2. The margin of safety as a percentage of budgeted sales

$$
MOS = 30,000,000 - 20,000,000 = 10,000,000
$$

$$
= \frac{10,000,000}{30,000,000} \times 100 = 33.333333\%
$$

##### Break-Even Analysis For Multiple Products

Break-even analysis can be applied to multiple products provided:
- There is a constant sales mix
- CM ratio is the same for all the products

###### Sales Mix

The relative proportions in which an organization sells its products. CVP analysis can be used to determine the sales mix that will maximize profit.

###### Break-Even Sales Mix 
First we need to compute the overall CM ratio.
$$
\text{Overall CM ratio} = \frac{\text{Total CM}}{\text{Total Sales}}
$$

Then we can compute the overall BEP in units and currency value.
$$
\text{Overall BEP (currency value)} = \frac{TFC}{\text{Overall CM ratio}}
$$

Finally , we can compute the BEP for each product using the sales mix proportions.
Using the example below:

| Product | Sales (GHC) | Variable Cost (GHC) | CM (GHC) | CM Ratio |
| ------- | ----------- | ------------------- | -------- | -------- |
| A       | 50,000      | 30,000              | 20,000  | 40%      |
| B       | 30,000      | 18,000              | 12,000  | 40%      |
| C       | 20,000      | 12,000              | 8,000   | 40%      |
| Total   | 100,000     | 60,000              | | 40,000  | 40%      |
The overall CM ratio is 40%. If the total fixed costs are GHC 16,000, then
$$
\text{Overall BEP (GHC)} = \frac{16,000}{0.4} = 40,000
$$

The sales mix proportions are:
- Product A: $50,000 / 100,000 = 50\%$
- Product B: $30,000 / 100,000 = 30\%$
- Product C: $20,000 / 100,000 = 20\%$

Therefore, the BEP for each product is:
- Product A: $40,000 \times 50\% = 20,000$
- Product B: $40,000 \times 30\% = 12,000$
- Product C: $40,000 \times 20\% = 8,000$

### Target Profit Analysis

The quantity of sales needed to achieve a specific target profit can be calculated using the formula:
$$
\text{Required Sales (units)} = \frac{TFC + \text{Target Profit}}{\text{Unit CM}}
$$

### Operating Leverage Analysis

The use of fixed-cost inputs in operations. Operating leverage is said to be high when fixed cost is higher than variable in the operating cost structure and vice versa.

#### Degree of Operating Leverage (DOL)

A measure of the responsiveness of net income to a given percentage change in sales. If DOL is high, a percentage change in sales will result in a larger percentage change in net income, and vice versa.
$$
\text{DOL} = \frac{\text{Contribution Margin}\quad(TR - TVC)}{\text{Net Income}\quad(CM - TFC)}
$$
