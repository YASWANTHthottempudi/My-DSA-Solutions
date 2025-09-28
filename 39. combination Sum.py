class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def combiSum(index, target, array):
            if index >= len(candidates):
                if target == 0:
                    res.append(array[:])  # <--- FIXED
                return
            
            if target >= candidates[index]:
                array.append(candidates[index])
                combiSum(index, target - candidates[index], array)
                array.pop()
            combiSum(index + 1, target, array)
        
        combiSum(0, target, [])
        return res
