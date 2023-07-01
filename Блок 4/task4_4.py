from itertools import combinations


thelist =  [4, 3, 2, 1]
target = 7

combs = []
result = []    
if len(thelist) > 0:
    for r in range(0,len(thelist)+1):        
        combs += list(combinations(thelist, r))
    for item in combs:        
        if sum(item) == target:
            result.append(item)

print(result)
