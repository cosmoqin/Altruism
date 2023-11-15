class Solution:
    def maxDiff(self, num: int) -> int:
        '''
        给你一个整数 num 。你可以对它进行如下步骤恰好 两次 :
        选择一个数字 x (0 <= x <= 9).
        选择另一个数字 y (0 <= y <= 9) 。数字 y 可以等于 x 。
        将 num 中所有出现 x 的数位都用 y 替换。
        得到的新的整数 不能 有前导 0 ，得到的新整数也 不能 是 0 。
        令两次对 num 的操作得到的结果分别为 a 和 b 。
        请你返回 a 和 b 的 最大差值 
        链接:https://leetcode.cn/problems/max-difference-you-can-get-from-changing-an-integer
        '''
        """
        for max : the first character in X will be replaced to 9
        for min : the first characert which not equals 0 in X will be replaced to 0 
        first time tried failed : for max - if the first character equals '9' ,the maxnum should be search for next character which suppose to replace
        """
        """
        min几条规则
        1.首位不 = 1, 可以改成1
        2.首位 = 1 但存在!=1 !=0的位置 改成0
        """
        num = 123456
        numStr = str(num)
        maxIndex = 0 
        while maxIndex < len(numStr):
            if numStr[maxIndex:maxIndex+1] != '9':
                maxIndex +=1
                break
            else: maxIndex +=1

        maxNum = numStr.replace(numStr[maxIndex-1:maxIndex],'9')

        minNum = ''
        minIndex = 0
        if numStr[0:1] != '1':
            minNum = numStr.replace(numStr[0:1],'1')
        else:
            while minIndex < len(numStr):
                if numStr[minIndex:minIndex+1] != '1' and numStr[minIndex:minIndex+1] != '0':
                    minNum = numStr.replace(numStr[minIndex:minIndex+1],'0')
                    break
                else:
                    minIndex +=1
                    minNum = numStr
        # minIndex = 0
        # if numStr[0:1] != '1':
        #     minNum = numStr.replace(numStr[0:1],'1')
        # else:
        #     while minIndex < len(numStr):
        #         if numStr[minIndex:minIndex+1] != '1' and numStr[minIndex:minIndex+1] != '0':
        #             minIndex +=1
        #             break
        #         else:
        #             minIndex += 1
        #     if numStr[minIndex-1:minIndex] != '1' and numStr[minIndex-1:minIndex] != '0' and minIndex = 0:
        #         minNum = numStr.replace(numStr[minIndex-1:minIndex],'1') 
        #     elif numStr[minIndex-1:minIndex] != '1' and numStr[minIndex-1:minIndex] != '0' and minIndex = len(numStr):
        #         minNum = numStr.replace(numStr[minIndex-1:minIndex],'0') 
        #     elif minIndex != len(numStr) :
        #         minNum = numStr.replace(numStr[minIndex-1:minIndex],'0')
        #     else:
        #         minNum = numStr
        #     minNum = numStr.replace(numStr[minIndex-1:minIndex],'0') if minIndex != len(numStr) \
        #     and numStr[minIndex-1:minIndex] != '0' \
        #     else numStr.replace(numStr[minIndex-1:minIndex],'1')
        return int(maxNum) - int(minNum)