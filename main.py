class Solution(object):
    def myAtoi(self, s):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        s = s.lstrip() # Remove whitespaces for step 1

        if not s:
            return 0
        
        #Handle optional sign for step 2
        sign = 1  #Assume a positive sign
        start = 0

        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
        
        #Convert the remaining digits to an iteger
        result = 0
        for i in range(start, len(s)):
            if not s[i].isdigit():
                break #Stop when encounterig a non digit character
            result = result * 10 + int(s[i])

            #Overflow and  underflow
            if sign == 1 and result > INT_MAX:
                return INT_MAX
            if sign == -1 and result > -INT_MIN:
                return INT_MIN

        return sign * result

solution = Solution()
s= "1337c0d3"
print(solution.myAtoi(s))
        
