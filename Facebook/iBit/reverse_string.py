class Solution:
    def solve(self, A):
         import re
         # Main
         A = A.lstrip() # strip any left space
         A += " " # artifically match below pattern on last stretch
         pattern = re.compile(r'([\w]+)\s+')
         idx = 0
         result = ""
         while not idx >= len(A) - 1:
             match = pattern.match(A[idx:])
             result = " " + match.group(1) + result
             idx += match.span()[1]

         return result.lstrip()


A = "I think I have it but a"
A = "fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq"
#A = "fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq    "
#A = "       fwbpudnbrozzifml osdt ulc jsx kxorifrhubk ouhsuhf sswz qfho dqmy sn myq igjgip iwfcqq                 "

print(Solution().solve(A))
