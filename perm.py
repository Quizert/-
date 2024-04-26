from sympy.combinatorics import Permutation
from itertools import combinations, permutations, product

def generate_permutations(n):
    return list(permutations(range(1, n+1)))

def add_one(a):
    s = []
    for i in range(len(a)):
        s.append(a[i] + 1)
    return s

def minus_one(a):
    s = []
    for i in range(len(a)):
        s.append(a[i] - 1)
    return s

def check_order(perms): 
    n = len(perms[0])
    a = [[i for i in range(1, n + 1)]]
    for i in perms:
        perm = Permutation(minus_one(i))
        if perm.order() == n and list(range(n)) != list(perm**2):
            a.append(add_one(list(perm)))
    return a


def check_degree(perms, degree): 
    n = len(perms[0])
    a = []
    for i in perms:
        perm = Permutation(minus_one(i))
        if list(range(n)) == list(perm**degree):
            a.append(add_one(list(perm)))
    return a
def normalize_perms_b(perms):
    normalize_perms_b = []
    def normalize_b(perm):
        n = len(perm)
        d = {}
        j = 1
        for i in range(n, 0, -1):
            d[-i] = n + j
            j += 1
        s = [0 for _ in range(n)]

        for i in range(n):
            if perm[i] in d:
                s[i] = d[perm[i]]
            else:
                s[i] = perm[i]
        for i in range(n, 0, -1):
            if -perm[i - 1] in d:
                s.append(d[-perm[i - 1]])
            else:
                s.append(-perm[i - 1])
        return s
   
    for i in perms:
        normalize_perms_b.append(normalize_b(i))
    return normalize_perms_b

def get_perm_b(n):
    numeric_elements = [i for i in range(1, n + 1)]

    numeric_perms = list(permutations(numeric_elements))

    signs = [1, -1]

    sign_combinations = list(product(signs, repeat=len(numeric_elements)))

    def apply_numeric_signs(perm, signs):
        return tuple(p if s == 1 else -p for p, s in zip(perm, signs))

    signed_numeric_permutations = []
    for perm in numeric_perms:
        for signs in sign_combinations:
            signed_numeric_permutations.append(apply_numeric_signs(perm, signs))
    return signed_numeric_permutations