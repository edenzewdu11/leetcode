class Solution(object):
    def isHappy(self, n):
        def num(number):
            return sum(int(digit) ** 2 for digit in str(number))

        i = n
        j = n

        while True:
            i = num(i)
            j = num(num(j))

            if j == 1:
                return True
            if i== j:
                return False


        