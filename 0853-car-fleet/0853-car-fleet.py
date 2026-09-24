class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        car=[]

        for i in range(len(position)):
            time=(target-position[i])/speed[i]

            car.append((position[i],time))

        car.sort(reverse=True)

        fleet=0
        slowest_time=0

        for pos,time in car:
            if time > slowest_time:
                fleet+=1
                slowest_time=time

        return fleet        
        