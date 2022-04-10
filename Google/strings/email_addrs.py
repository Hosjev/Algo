from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # We def have to sanitize
        # Sanitize == 1) rid dots, 2) right of +, left of @ delete
        result = set()
        for addr in emails:
            # sanitize 1
            item = addr.split("@")
            left = [i for i in item[0] if i != "."]
            # sanitize 2
            try:
                plus = left.index("+")
            except:
                plus = None
            if plus: left = left[:plus]
            result.add(("".join(left) + "@" + item[1]))
        print(result)
        return len(result)



if __name__ == "__main__":
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    obj = Solution()
    print(obj.numUniqueEmails(emails))

