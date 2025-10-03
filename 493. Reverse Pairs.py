class Solution:
    global_count = 0

    def merge(self, sublist, l, mid, h):
        temp = [0] * (h-l+1)
        k = 0

        i = l
        j = mid + 1

        while i <= mid and j <= h:
            if sublist[i] > 2 * sublist[j]:
                
                Solution.global_count += mid - i + 1
                j += 1
            else:
                i += 1

        
        i = l
        j = mid + 1

        while i <= mid and j <= h:
            if sublist[i] < sublist[j]:
                temp[k] = sublist[i]
                k += 1
                i += 1
            else:
                temp[k] = sublist[j]
                k += 1
                j += 1

        while i <= mid:
            temp[k] = sublist[i]
            k += 1
            i += 1

        while j <= h:
            temp[k]= sublist[j]
            k += 1
            j += 1
        for ptr in range(h-l+1):
            sublist[l+ptr] = temp[ptr] 


    def merge_splitter(self, sublist, l, h):
        if l < h:
            mid = (l + h) // 2
            self.merge_splitter(sublist, l, mid)
            self.merge_splitter(sublist, mid + 1, h)

            self.merge(sublist, l, mid, h)


    def reversePairs(self, nums: List[int]) -> int:
        Solution.global_count = 0

        self.merge_splitter(nums, 0, len(nums)-1)
        return Solution.global_count
