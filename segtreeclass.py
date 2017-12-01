'''
My favorite data structure - the Segment Tree!
Building the tree in O(n)
Query in O(log N)
Modify element in O(log N)

You can do all sorts of things with a segment tree on a list!
This implementation does range querying and point modifying, so
you can modify only one element at a time but you can query over a
range. Querying is inclusive of the left range but exclusive of the
exclusive of the right range.

You can do Range Sum, Range Maximum/Minimum Query and other stuff


'''

class Segtree:

    def __init__(self, list, id):
        self.n = len(list)
        temp = [0] * self.n
        self.stree = temp
        self.stree += list
        self.id = id

    def printlist(self):
        print(self.stree[self.n:])

    def build(self):
        for i in range(self.n-1, -1, -1):
            self.stree[i] = self.stree[i*2] + self.stree[i*2 + 1];

    def modify(self, i, x):
        i += self.n
        self.stree[i]  = x
        while i > 1:
            self.stree[i//2] = self.stree[i] + self.stree[i^1]
            i //= 2

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n

        while l < r:
            if l % 2 == 1:
                res += self.stree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                res += self.stree[r]
            l //= 2
            r //= 2
        return res

    def getid(self):
        return self.id

    def __add__(self, stree2):
        tp = Segtree(self.stree[self.n:] + stree2.stree[stree2.n:], 0)
        tp.build()
        return tp



#example list
li = [0,1,2,3,4,5,6,7,8]
print(li)

#init Segment Tree and build it
stree = Segtree(li, 0)
stree.build()

#query sum of the 1st to 4th elements
print(stree.query(0,5))

#make the 2nd element 2 and query again
stree.modify(1,2)
stree.printlist()
print(stree.query(0,5))

print(stree.id)

li2 = [1,2,3,4,5,6,7]

stree2 = Segtree(li2, 1)
stree3 = stree + stree2

stree3.printlist()
print(stree3.query(6, 10))
