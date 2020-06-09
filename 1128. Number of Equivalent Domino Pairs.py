class Solution:
    def numEquivDominoPairs(self, dominoes):

        count = {}

        for i in dominoes:
            tmp = min(i)*10+max(i)

            if tmp in count:
                count[tmp]+=1

            else:
                count[tmp] = 1

        res = 0
        print(count)

        for i in count:
            print(i)
            if count[i] >= 2:
                print(">2")
                res += count[i]*(count[i]-1)//2
                print(res)
        return res

if __name__ == "__main__":
    dominoes = [[1,2],[2,1],[3,4],[5,6]]

    result = Solution().numEquivDominoPairs(dominoes)
    print(result)
