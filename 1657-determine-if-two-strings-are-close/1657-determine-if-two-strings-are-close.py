
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #Length must be same
        if len(word1)!=len(word2):
            return False
        #Count character frequencies ex: "abbccc" → {a:1, b:2, c:3}
        count1=Counter(word1)
        count2=Counter(word2)
        #Check same unique characters
        if set(count1.keys())!=set(count2.keys()):  #check keys like a b c
            return False
        #Check frequency pattern like a:1,b:2,c:3 same in word2
        if sorted(count1.values())!=sorted(count2.values()): 
            return False
        return True                
          
        # count1.values() → How many times each character appears  