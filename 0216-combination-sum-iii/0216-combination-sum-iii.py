class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer=[]
        def backtrack(start,path,k,target):
            if target ==0 and k == 0:
                answer.append(path[:])
                return

            for i in range(start,10):
                if i > target and k<=0:  
                    break
                path.append(i)

                backtrack(i+1,path,k-1,target-i)   
                path.pop()

        backtrack(1,[],k,n)       
        return answer    
           
        
        