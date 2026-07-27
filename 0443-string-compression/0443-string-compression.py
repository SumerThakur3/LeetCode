class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0                        # Read pointer
        index=0                    # Write pointer
        while i < len(chars):
            current=chars[i]        # Current character
            count=0                # Count how many times it repeats

            # Count repeated characters
            while i<len(chars) and chars[i]==current:
                count+=1
                i+=1
            
            # Write the character
            chars[index]=current
            index+=1
            
            # If character repeats, write its count
            if count>1:
                for digits in str(count):      #Convert count to string like 1 to '1'
                    chars[index]=digits
                    index+=1

        return index           