# dis = 6, 9, 10, 3
# speed = 2, 2, 1, 1
# time 3, 4.5, 10, 3

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        for i in range(len(speed)):
            d[position[i]]=speed[i]
        
        position.sort()
        print(position)

        time = []
        for i in range(len(position)):
            time.append(float((target-position[i])/d[position[i]]))
        print(time)
        
        m = time[-1]
        fl = 1
        for t in time[::-1]:
            print(t)
            if t<=m:
                
                continue
            else:
                m = t
                fl+=1
        return fl
        