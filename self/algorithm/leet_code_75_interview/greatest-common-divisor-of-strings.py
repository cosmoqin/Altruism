class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        https://leetcode.cn/problems/greatest-common-divisor-of-strings/
        """
        '''
        failed - 多用数学思维思考，直接找两个长度的最大公约数，判断 
            candidate = str1[: candidate_len]
            candidate * (len(str1) // candidate_len) == str1
            即可
            1.遍历找公约数
            2.公约数 * str[] == str

        第一次解答错误：
        input "ABABABAB" "ABAB"
        expect "ABAB"
        output "AB"
        solution 倒序找公约数
        '''
        str1,str2 = "AA","A"
        n1,n2 =len(str1),len(str2)
        for i in range(min(n1,n2),0,-1):
            if n1%i == 0 and n2%i == 0:
                candidate = str1[0:i]
                if candidate * (int(n1/i)) == str1 and candidate *(int(n2/i))==str2:
                    return candidate
        return ''
        # str1 = 'ABABAB'
        # str2 = 'ABAB'
        # s1 = list(str1)
        # s2 = list(str2)
        # n1 = len(s1)
        # n2 = len(s2)
        # l1 = 0
        # l2 = 0
        # divisor = ''
        # while  l2 < n2 and l1 < n1 and s1[l1] == s2[l2]:
        #     divisor += s2[l2]
        #     l1 += 1
        #     l2 += 1
        # n3 = len(divisor)
        # if divisor != '' and (n1 % n3 == 0) and (n2 % n3 == 0):
        #     for i in range(0,int(n1/n3)):
        #         if divisor != str1[n3*i:n3*i+n3]:
        #             print("failed")
        #             # return ''
        #     for i in range(0,int(n2/n3)):
        #         if divisor != str2[n3*i:n3*i+n3]:
        #             print("failed")
        #             # return ''
        #     return divisor
        # return ''

        