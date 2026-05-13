class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        index = 0

        sumTarget = sum(target)


        firstVal = float('-inf')
        secondVal = float('-inf')
        thirdVal = float('-inf')

        for triple in triplets:

            if triple[0] > target[0] or triple[1] > target[1] or triple[2] > target[2]:
                continue

            for j in range(3):
            
                if j == 0:
                    firstVal = max(firstVal, triple[j])
                elif j == 1:
                    secondVal = max(secondVal, triple[j])
                else:
                    thirdVal = max(thirdVal, triple[j])
            
            if [firstVal, secondVal, thirdVal] == target:
                return True

        return False

