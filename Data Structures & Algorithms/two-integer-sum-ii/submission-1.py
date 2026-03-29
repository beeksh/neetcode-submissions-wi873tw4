class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hm = {}
        # for i in range(len(numbers)):
        #     if target-numbers[i] in hm:
        #         return [hm[target-numbers[i]]+1, i+1]
        #     hm[numbers[i]] = i
        l, r = 0, len(numbers)-1
        while numbers[l]+numbers[r]!=target:
            if numbers[l]+numbers[r]>target:
                r-=1
            else:
                l+=1
        return [l+1, r+1]

        