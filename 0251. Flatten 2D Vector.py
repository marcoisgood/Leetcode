"""
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.



Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false
"""

class Vector2D:

    def __init__(self, v):
        self.values = []
        for i in v:
            while i:
                self.values.append(i.pop(0))


    def next(self) -> int:
        return self.values.pop(0)


    def hasNext(self) -> bool:
        return self.values

if __name__ == "__main__":
    iterator = Vector2D([[1,2],[3],[4]]);
    iterator.next()
    iterator.next()
    iterator.next()
    iterator.hasNext()


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
