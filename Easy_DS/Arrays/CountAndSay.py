'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

Example:
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211
'''


class CountAndSay:
    def __init__(self):
        return

    def count_and_say(self, num):
        s = "1"
        if num <= 1:
            return s
        for _ in range(2, num+1):
            temp = ""
            curr = ""
            count = 0
            j = 0
            while(j<len(s)):
                if curr == "":
                    curr = s[j]
                    count += 1
                    j += 1
                elif curr == s[j]:
                    count += 1
                    j += 1
                else:
                    temp += str(count) + curr
                    curr = ""
                    count = 0
            temp += str(count) + curr
            s = temp
        return s


num = 4
print(CountAndSay().count_and_say(num))