import itertools
M={1,2,3,4}
print('Submulţimile mulţimii {1, 2, 3, 4}:')
for i in range(0,len(M)):
    subset=itertools.combinations(M,i+1)
    print(set(subset))