class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0
        read = 0
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            while read < n and chars[read] == char:
                read += 1
                count += 1

            # Now, while the count is increasing and the value of the current char is same as the read                     #character, we need to increment read and count variable. But, we also need to write the current               #char in the #array, if or if not the count is 1.
            # Initially, we just write the character we are currently on and then after that we will write the             #count if it is more than 1
            
            chars[write] = char # Rewrite the chars array at the write pointer with the value of char.
            write += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
        return write