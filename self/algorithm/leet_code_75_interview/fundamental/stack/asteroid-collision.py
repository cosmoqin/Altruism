class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        给定一个整数数组 asteroids
        表示在同一行的行星。
        对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
        找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。
        """
        asteroids = [-2,-2,1,-2]
        n = len(asteroids)
        temp = [asteroids[0]]
        for i in range(1,n):
            if len(temp) > 0 and asteroids[i] < 0 and temp[-1] > 0:
                while temp and temp[-1] > 0:
                    if abs(asteroids[i]) > abs(temp[-1]) :
                        temp.pop()
                    elif abs(asteroids[i]) == abs(temp[-1]):
                        temp.pop()
                        break
                    else:
                        break
                else:
                    temp.append(asteroids[i])
            else:
                temp.append(asteroids[i])
        return temp
