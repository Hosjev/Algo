"""
    Though this problem is interesting, it doesn't respect industry standards,
    such as leading zeros and nested IPv4 inside IPv6.
"""

import re


class Solution:
    chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
    
    chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
    patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

    def validIPAddress(self, IP: str) -> str:        
        if self.patten_IPv4.match(IP):
            return "IPv4"
        return "IPv6" if self.patten_IPv6.match(IP) else "Neither" 


class Solution:
    """ HOT STEAMING PILE """
    def _validate_v4(self, string):
        # Validate notation
        pattern = re.compile(r'(\w+).(\w+).(\w+).(\w+)')
        if not string.count('.') == 3: return "Neither"
        try:
            nots = len(pattern.match(string).groups())
        except AttributeError:
            return "Neither"
        else:
            if nots != 4:
                return "Neither"

        # Validate numeric
        for entry in pattern.match(string).groups():
            if entry.startswith("0") or \
                not entry.isdigit() or \
                not -1 < int(entry) < 256:
                    return "Neither"
        return "IPv4"

    def _validate_v6(self, string):
        # Validate notation
        # RULES
        # *double :: only used once
        pattern = re.compile(r'\w(::)\w')
        if len(pattern.findall(string)) > 1 or \
            string.count(":") > 7:
            return "Neither"

        # Validate hex
        pattern = re.compile(r'(\w)+')
        matches = pattern.findall(string)
        if not matches: return "Neither"

        #hex_pattern = re.compile(r'[\dA-Fa-f]')
        for hex_entry in matches:
            if len(hex_entry) > 4: return "Neither"
            try:
                temp = int(hex_entry, 16)
            except ValueError:
                return "Neither"

        return "IPv6"

    def validIPAddress(self, queryIP: str) -> str:
        # Expected to parse CIDR notations?
        # Eval v6 first 
        if ":" in queryIP:
            return self._validate_v6(queryIP)
        else:
            return self._validate_v4(queryIP)



if __name__ == "__main__":
    v6 = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    v6 = "2001::85a3:0::0:8A2E:0370:7334"
    v6 = "::85a3:0:8A2E:0370:7334"
    v6 = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
    v4 = "192.156.2.1"
    #v4 = "192.1e6.2.1"
    #v4 = "1.0.1."
    #v4 = "1.0.1.3.4"
    obj = Solution()
    print(obj.validIPAddress(v6))
    print(obj.validIPAddress(v4))
