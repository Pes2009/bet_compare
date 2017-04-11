# Footbal bets Comparison
## Quick Intro

Football bets Comparison is application which help you to 

compare bets from diffrent bookmakers.

## Functional Requirements 

* App is installable through Python package manager (PIP)
* checking everyday bets from bookmakers side
* save bets and compare them
  
## User should be allowed to change

* number of bets
* bookmakers
* amount


## Technical requirements

* App needs to be connected to the internet 
* App has to contain functional test suit. 

## Expansion Intentions

* user can make own account
* user can save his bets
* deploy with django



# Examples
```
> bets "barcelona-real" 
1) basketball [10]
2) footbal    [20]
2
+-----------------+-----------------+
| bwin            | betathome       |
+-----------------+-----------------+
| 1.7 | 1.4 | 2.4 | 1.9 | 1.5 | 2.6 | 
+-----------------+-----------------+
1) home win
2) draw
3) away win
2
whole rate
+-----------------+-----------------+
| bwin            | betathome       |
+-----------------+-----------------+
| 1.4             |  1.5            |
+-----------------+-----------------+
1) add new bet
2) change bid (default=1)
3) change last bet
4) print strike and end
1
> bets "Legia-Ajax" 
+-----------------+-----------------+
| bwin            | betathome       |
+-----------------+-----------------+
| 9.5 | 2.4 | 1.2 | 9.0 | 1.9 | 1.1 | 
+-----------------+-----------------+
1) home win
2) draw
3) away win
1
whole rate
+-----------------+-----------------+
| bwin            | betathome       |
+-----------------+-----------------+
| 13.3            | 13.5            | 
+-----------------+-----------------+
1) add new bet
2) change bid (default=1)
3) change last bet
4) print strike and end
3
+-----------------+-----------------+
| bwin            | betathome       |
+-----------------+-----------------+
| 9.5 | 2.4 | 1.2 | 9.0 | 1.9 | 1.1 | 
+-----------------+-----------------+
1) home win
2) draw
3) away win
2
whole rate
+-----------------+-----------------+
| bwin            | betathome       |
+-----------------+-----------------+
| 3.36            | 2.85            | 
+-----------------+-----------------+
1) add new bet
2) change bid (default=1)
3) change last bet
4) print strike and end
4
whole rate
+-----------------+-----------------+
| bwin            | betathome       |
+-----------------+-----------------+
| 3.36            | 2.85            | 
+-----------------+-----------------+
1) change bid (yours=1)
2) end
1
your's bid = 1
write new bid
> 15
your's bid now is 15
whole rate
+-----------------+-----------------+
| bwin            | betathome       |
+-----------------+-----------------+
| 50.4            | 42.7            | 
+-----------------+-----------------+
1) change bid (yours=15)
2) end
```
  
    
