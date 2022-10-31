from time import time
import itertools
from tkinter import W
 
def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

# use build in itertool method
@timer_func
def combinations(elements):
    toReturn = set()
    queue = list()

    queue.append((frozenset(), elements))

    while queue:
        r, toAdd = queue.pop()

        for elem in toAdd:
            ot = set(r)
            ot.add(elem)
            curr = frozenset(ot)
            if curr not in toReturn:
                toReturn.add(curr)

                t = set(toAdd)
                t.remove(elem)
                queue.append((curr, t))

    toReturn.add(frozenset())
    return toReturn

# @timer_func
def powerset(iterable):
    s = list(iterable)
    return list(itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1)))

# for i in range(int(input("integer: "))):
#     # combinations(range(i))
#     powerset(range(i))

# results
    # for elem in sorted(list(combinations(range(int(input("array size"))))), key=lambda x: len(x)):
        # print(elem)

def getPreferredSellerGraph(buyers, p):
    length = len(buyers)
    toReturn = []

    for buyer in buyers:
        tmp = list(zip(
            buyer, 
            p,
            range(length)
        ))
        payout = max(
            tmp, 
            key=lambda t: t[0] - t[1]
        )
        payout = payout[0] - payout[1]
        toReturn.append([
            e[2] for e in filter(lambda t: t[0] - t[1] == payout, tmp)
        ])

    return toReturn

# preferredSellerGraph: [int]
def getConstrictedSet(preferredSellerGraph):
    for combination in powerset(
        range(len(preferredSellerGraph))
    ):
        tset = set()
        for i in combination:
            tset = tset.union(preferredSellerGraph[i])

        if len(tset) < len(combination):
             return (tset, combination)

def updatePrices(p, constrictedSet):
    for i in constrictedSet[0]:
        p[i] += 1

    pmin = min(p)
    for i in range(
        len(p)
    ):
        p[i] -= pmin

    return p
    
def bidIteration(people):
    prices = [
        0 for _ in range(
            len(people)
        )
    ]
    while True:
        preferredSellerGraph = getPreferredSellerGraph(people, prices)
        print(preferredSellerGraph)
        constrictedSet = getConstrictedSet(preferredSellerGraph)
        print(constrictedSet)
        if not constrictedSet:
            break 
        prices = updatePrices(prices, constrictedSet)
        print(prices)

subjectiveValues = [
    [
        10, 2, 5, 2, 0, 0, 0, 0
    ],
    [
        32, 23, 23, 6, 0, 0, 0, 0
    ],
    [
        12, 55, 77, 11, 0, 0, 0, 0
    ],
    [
        5, 6, 23, 3, 0, 0, 0, 0
    ],
    [
        0, 0, 0, 0, 10, 2, 5, 2
    ],
    [
        0, 0, 0, 0, 32, 23, 23, 6
    ],
    [
        0, 0, 0, 0, 12, 55, 77, 11
    ],
    # [
    #     0, 0, 0, 0, 5, 6, 23, 3
    # ]
    # [
    #     5, 6, 23, 3, 5, 6, 23, 3
    # ]
    [
        5, 6, 23, 3, 0, 0, 0, 0
    ]
]

bidIteration(subjectiveValues)