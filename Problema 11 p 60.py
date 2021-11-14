import itertools
M={'A','B','C','D'}
print('Submulţimile mulţimii {’A’, ’B’, ’C’, ’D’}:')
for i in range(0,len(M)):
    subset=itertools.combinations(M,i+1)
    print(set(subset))