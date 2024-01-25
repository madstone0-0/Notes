Tested with `values`
```python
    >>> values = [2_000,600,6_000,16_000,50_000,60_000]
    >>> for val in values:
    ...     print(f"{val}: {income_tax(val)}")
    2000: 256.15
    600: 14.3
    6000: 1133.0
    16000: 3633.0
    50000: 13631.15
    60000: 17131.15
```

- $2000$ was chosen to check correctness with the question.

- $600$ was chosen to check the bracket $512<=$ gross $<=642$

- $6000$ was chosen to check the bracket $642<=$ gross $<=3642$

- $16000$ was chosen to check the bracket $3642 <=$ gross $<=20037$

- $50000$ was chosen to check the bracket $20037 <=$ gross $<= 50000$

- $60000$ was chosen to check the bracket gross $> 50000$
