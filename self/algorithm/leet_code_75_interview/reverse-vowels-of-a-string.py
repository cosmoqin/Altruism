class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        https://leetcode.cn/problems/reverse-vowels-of-a-string/
        双指针 + set
        1.set will be more efficient then string.find
        '''
        h = set("aeiouAEIOU")
        n = len(s)
        s = list(s)
        l, r = 0, n-1
        while l < r:
            while l < n and s[l] not in h:
                l = l+1
                # 找到左边第一个元音
            while r > 0 and s[r] not in h:
                r -=1
                # 找到右边第一个元音
            if l < r :
                # 不加if 会遍历到尾
                s[l] ,s[r] = s[r],s[l]
            l += 1
            r -= 1
        return "".join(s)
            
#         def splitStringByVowels(self,orl,vowel):
#             s = orl.pop()
#             for i in s:
#                 pos = 'aeiouAEIOU'.find(i)

#                 if pos == len(s)-1:
#                     orl.append(s[0:pos])
#                     vowel.append(s[pos:pos+1])
#                     return reverseVowels(orl,vowel)
#                 elif pos != -1:
#                     orl.append(s[0:pos])
#                     vowel.append(s[pos:pos+1])
#                     orl.append(s[pos+1:-1])
#                     return reverseVowels(orl,vowel)
#                 else:
#                     return orl,vowel
            

#         vowel = []
#         origin = []
#         origin.append(s)
#         origin,vowel = splitStringByVowels(origin,vowel)
#         result = ''
#         for i in origin:
#             result = result + i
#             if len(vowel) > 0:
#                 result = result + vowel.pop()
#         return result
# def main():
#     solution = Solution()
#     solution.reverseVowels("A man, a plan, a canal -- Panama")

# if __name__ = "__main__":
#     main()