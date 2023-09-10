class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # 给你字符串 s 和整数 k 。
        # 请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
        # 英文中的 元音字母 为（a, e, i, o, u）。
        base = List[s]