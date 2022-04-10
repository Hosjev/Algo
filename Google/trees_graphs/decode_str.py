class Solution:

    def _empty_stack(self, ext_ph, stack):
        int_ph = str()
        while stack:
            char = stack.pop()
            if char == "]":
                c = stack.pop()
                while stack[-1].isalpha():
                    c = stack.pop() + c
                stack.pop() # [
                d = stack.pop()
                while stack[-1].isdigit():
                    d = stack.pop() + d
                int_ph = (int(d) * c) + int_ph
            elif char.isalpha():
                int_ph = char + int_ph
            else: # [
                d = stack.pop()
                while stack and stack[-1].isdigit():
                    d = stack.pop() + d
                ext_ph = (int(d) * int_ph) + ext_ph
        return ext_ph

    def decodeString(self, s: str) -> str:
        # EC

        # Prime
        ext_ph, int_ph = str(), str()
        stack = list()
        pointer = int()
        lb = int()

        # Use stack
        while pointer < len(s):
            if s[pointer] != "]":
                if s[pointer] == "[": lb += 1
                if lb == 0 and s[pointer].isalpha(): ext_ph += s[pointer]
                else: stack.append(s[pointer])
            else: # RIGHT
                lb -= 1
                if lb == 0: # empty stack
                    ext_ph = self._empty_stack(ext_ph, stack)
                else: stack.append(s[pointer])
            pointer += 1
        
        # Check stack
        if bool(stack): ext_ph = ext_ph + "".join(stack)

        return ext_ph


if __name__ == "__main__":
    s = "3[a2[c]]ef"
    s = "abc3[cd]xyz"
    obj = Solution()
    print(obj.decodeString(s))
