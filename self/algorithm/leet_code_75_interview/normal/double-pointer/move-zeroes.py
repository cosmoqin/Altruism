class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        给定一个数组 nums 
        编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
        请注意 ，必须在不复制数组的情况下原地对数组进行操作。
        """
        # solution 1 : calculate the number of 0 then create two pointer , first point start with index '0' , another pointer start with n-count(0) 
        # 双指针考察
        # n = len(nums)
        # pre_pointer = 0
        # suffix_pointer = n-1
        # for i in range(0,n):
        #     if nums[pre_pointer] == 0 and pre_pointer > suffix_pointer:
        #         nums[pre_pointer],nums[suffix_pointer] = nums[suffix_pointer],nums[pre_pointer]
        #         pre_pointer += 1
        # n = len(nums)
        # move_cnt = 0
        # for i in range(0,n):
        #     if nums[i] == 0: move_cnt+=1
        
        # bw_pointer = n-move_cnt
        # for i in range(0,n):
        #     if nums[i] == 0:
        # solution 2 : double for rotation 
        nums = [0,1,0,3,12]
        n = len(nums)-1
        for i in range(0,n):
            if nums[i] == 0 and i<n:
                j = i
                while j <= n:
                    if nums[j] != 0:
                        nums[i],nums[j] = nums[j],nums[i]
                        break
                    else:
                        j+=1

        print(nums)     