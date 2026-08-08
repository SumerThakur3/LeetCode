class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant=[]
        dire=[]
        for i in range(len(senate)):
            if senate[i]=='R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r=radiant.pop(0)
            d=dire.pop(0)

            if r < d:
                radiant.append(r + len(senate))
            else:
                dire.append(d + len(senate))

        if radiant:
            return "Radiant"     
        else:
            return "Dire"       
