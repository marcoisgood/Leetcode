"""
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().



Example 1:

Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.


Note:

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seems to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.
"""
import threading
"""
Ans 1, using Lock()
release(): locked -> unlocked
acquire(): unlocked -> locked or when locked, wait for unlocked
"""


class Foo:
     def __init__(self):
         self.lock1 = threading.Lock()
         self.lock2 = threading.Lock()

         self.lock1.acquire()
         self.lock2.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.lock1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        self.lock2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lock2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


"""
Ans2, using Event()
set(): setting free
wait(): waiting for free signal
clear(): clearing the signal (1 -> 0)
"""

class Foo:
    def __init__(self):
        self.E1 = threading.Event()
        self.E2 = threading.Event()

        self.E1.clear()
        self.E2.clear()


    def first(self, printFirst: 'Callable[[], None]') -> None:

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.E1.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.E1.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        self.E2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.E2.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
