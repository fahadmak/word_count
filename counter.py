import string
def words(str):
    counts = dict()
    wordsr = str.split()
    numbers = [int(x) for x in wordsr if x.isdigit()]
    others = [x for x in wordsr if not any(c.isdigit() for c in x)]
    complete = others + numbers


    """wordie = [x for x in wordsr if x.isalpha()]"""
    
    

    for word in complete:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
    
    

print( words('the quick brown 1 1 1 1 1 jumps  jumps fox fox over the lazy ** dog.'))

    
