class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        https://leetcode.cn/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
        给你两个字符串 word1 和 word2 。
        请你从 word1 开始，通过交替添加字母来合并字符串。
        如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。
        返回 合并后的字符串
        """
        '''
        也可以双指针
        '''
        s1 = list(word1)
        s2 = list(word2)
        n1 = len(s1)
        n2 = len(s2)
        nmax = n1 if n1 > n2 else n2
        nmin = n2 if n1 > n2 else n1
        result = ""
        for i in range(0,nmin):
            result = result + s1[i] + s2[i]
        substr = "".join(s1[nmin:nmax]) if n1 > n2 else "".join(s2[nmin:nmax])
        return result + substr

                
