# Makeshift

## Introduction
> A simple shuffle encryption

Source Code :
```python
from secret import FLAG

flag = FLAG[::-1]
new_flag = ''

for i in range(0, len(flag), 3):
    new_flag += flag[i+1]
    new_flag += flag[i+2]
    new_flag += flag[i]

print(new_flag)
```
And output.txt:
```
!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB
```

## Solution
```python
flag = '!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB'

new_flag = ''

for i in range(0, len(flag), 3):
    new_flag += flag[i+2]
    new_flag += flag[i]
    new_flag += flag[i+1]


print(new_flag[::-1])
> HTB{4_b3tTeR_w3apOn_i5_n3edeD!?!}
```
