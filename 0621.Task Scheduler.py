"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.



Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


explanation
會有兩種模式：
有idle, 沒有idle, 所以最後要比最大值
"""

class Solution:
    def leastInterval(self, tasks, n):
        d = {}
        for i in tasks:
            if i in d:
                d[i]+=1
            else:
                d[i]=1


        list = sorted(d.values(), reverse = True)


        max_num = list[0]


        print("d: {},\nlist: {},\nmax_num: {}\n".format(d,list,max_num))

        i = 0
        count = 0

        while i < len(list) and list[i] == max_num:
            count+=1
            i+=1
            print("i: {},\ncount: {},\n".format(i,count))

        tmp = (max_num-1)*(n+1)+count

        return max(tmp, len(tasks))



if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B","C","C","C","E","F","G"]
    n = 2
    result = Solution().leastInterval(tasks, n)
    print(result)
