class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Get the occurrences of each number. (also remove duplicated numbers)
        #store the elements in key value pair
        num_occur = Counter(arr)
        # Remove duplicated occurences using a set.(values=occurence of number)
        unique_occur=set(num_occur.values())
        # return True if each unique number has a unique occurrence (keys=numbers)
        return len(num_occur.keys())==len(unique_occur)
            