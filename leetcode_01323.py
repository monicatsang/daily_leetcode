#1323. Maximum 69 Number
#https://leetcode.com/problems/maximum-69-number/

#You are given a positive integer num consisting only of digits 6 and 9.
#Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).


class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = map(int,str(num))
        change_digit = int(1)
        s = ""
        for digit in digits:
            if digit == 6 and change_digit > 0:
                digit = 9
                change_digit = change_digit - 1
            print (digit)
            s += str(digit)
        print (str(s))     
        return int(str(s))     
       

