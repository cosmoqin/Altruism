class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        如果可以使用以下操作从一个字符串得到另一个字符串 则认为两个字符串 接近 
        操作 1交换任意两个 现有 字符。
        例如 abcde -> aecdb
        操作 2将一个 现有 字符的每次出现转换为另一个 现有 字符 并对另一个字符执行相同的操作。
        例如 aacabb -> bbcbaa 所有 a 转化为 b  而所有的 b 转换为 a  
        你可以根据需要对任意一个字符串多次使用这两种操作。
        给你两个字符串 word1 和 word2 。如果 word1 和 word2 接近  就返回 true ；否则 返回 false 。
        """
        word1 ,word2 = "a","aa"

        list1 = [i for i in word1]
        list2 = [_ for _ in word2]
        if len(list1) != len(list2):return False
        # 因为不限制次数 所以只需要判断频次和出现的字符次数即可决定
        set1 = {}
        set2 = {}
        n= len(list1)
        for i in range(n):
            if list1[i] not in set1.keys():
                set1[list1[i]]=1
            else:
                set1[list1[i]]+=1
            if list2[i] not in set2.keys():
                set2[list2[i]]=1
            else:
                set2[list2[i]]+=1
        print(set1)
        print(set2)
        print(set1.keys())
        print(set2.keys())
        print(set1.keys() == set2.keys())
        print(sorted(set1.values(),reverse=True))
        print(sorted(set1.values()) == sorted(set2.values()))
        return True if set1.keys() == set2.keys() and sorted(set1.values()) == sorted(set2.values()) else False
