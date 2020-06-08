"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def addStrings(self, num1, num2):
        # ans1
        # return str(int(num1)+int(num2))
        # ans2
        if num1 == '0' and num2 =='0':
            return '0'
        elif num1 == '0': return num2
        elif num2 == '0': return num1
        else:
            if len(num2) > len(num1):
                num1, num2 = num2, num1

        hash_map={
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
        }

        num1 = list(num1)
        num2 = list(num2)
        tmp = 0
        tmp2 = 0
        res = []
        count = 0
        while len(num1) and len(num2):
            tmp = hash_map[num1.pop()]
            tmp2 = hash_map[num2.pop()]

            if tmp + tmp2+count >= 10:
                res += [(tmp+tmp2+count)%10]
                count = 1
            else:
                res += [tmp+tmp2+count]
                count = 0

        print("num1: ", num1)

        while len(num1) and count != 0:
                tmp = hash_map[num1.pop()]

                if tmp + count >= 10:

                    res += [(tmp+count)%10]
                else:
                    res += [tmp+count]
                    count = 0


        if len(num1):
            num1[:] = num1[::-1]
            res += num1
        if count == 1:
            res += [1]

        res = res[::-1]
        res = ''.join(str(num) for num in res)
        return res
if __name__ == "__main__":
    num1 = '9'
    num2 = '99'
    result = Solution().addStrings(num1, num2)
    print(result)
