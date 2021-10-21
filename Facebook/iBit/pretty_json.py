class Solution:
    """ Basically, serialize this input A == json.dumps() """
    def prettyJSON(self, A):
        # Prime
        string = A
        i = p = 0
        indent = 0
        left = set('{[')
        right = set('}]')
        json_result = []

        while not p == len(string):
            if string[p] == ',':
                json_result.append('\t' * indent + string[i:p+1].strip())
                i = p = p + 1
                continue
            elif string[p] in left.union(right):
                entry = string[i:p].strip()
                if not len(entry) == 0:
                    json_result.append('\t' * indent + entry)
                if string[p] in left:
                    json_result.append('\t' * indent + string[p])
                    indent += 1
                else:
                    indent -= 1
                    r = '\t' * indent + string[p]
                    if p < len(string) -1 and string[p+1] == ',':
                        r += ','    
                        p += 1
                    json_result.append(r)
                i = p = p + 1
                continue
            else:
                p += 1

        return json_result


A = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
A = '["foo", {"bar":["baz",null,1.0,2]}]'
#A = '{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,"Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}'



print(Solution().prettyJSON(A))
