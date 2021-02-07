"""
Write a function that takes in a non-empty string representing a valid Unix-shell path and returns a shortened version of that path.

A path is a notation that represents the location of a file or directory in a file system.

A path can be an absolute path, meaning that it starts at the root directory in a filesystem, or a relative path, meaning it starts at the current directory in a filesystem.

In Unix-like ops, a path is bound these rules:
    -root dir is /. Meaning, if path starts w/a forward slash, it IS an abs path. If not, it's relative.
    -the symbol / is a separator /foo/bar -- bar is dir under foo
    -the symbol ".." represents parent dir. /foo/bar/.. == /foo
    -the symbol "." represents current dir. /foo/bar/. == /foo/bar
    -symbol together like / and . can be used innumerably. /foo/bar/././. == /foo/bar
    -an exception would be: /../../../ == /

* note that the shortened version of a path must be equivalent to the original path, it must point to the same file or directory as the original path.

Input:
    path = "/foo/../test/../test/../foo//bar/./baz"

Output:
    "/foo/bar/baz"

* a recursive "add to current working" --keys defined as:
     -"/(str of chars)" = valid move forward, add to CW
     -"/." a null move
     -"/.." remove from current working "/(str of chars)/" to 1st / non-inclusive
     -"//" nothing btw, a null move
     -when str/path is exhausted, return result
     -just remember to handle a beginning or resulting (mid-eval) relative path
     -and handle "/../../" like if the "next" iteration or eval is "/.." and you apply it to "/" then null

answer - O(NM)T / O(NM)S --M is 2nd string
"""


def shortenPath(path):
    """
    My version:
        -use hash of symbols
        -for each symbol an action is taken
        -iterate straight thru list, referencing previous when necessary/according to rule

    Algo version:
        -path to array where "/" is the divisor
        -empty / means null (the reason to keep these is in case of a ".."
        -iterate now through, tracking a true/false for a 1st / in a relative path
        -what if we have multiple "/../../../"? this is why I thought a recur, constant eval
    """
    if path[0] == "/":
        absolute = True
    else:
        absolute = False

    path = path.split("/")
    path = [ x for x in path if x != "." ]
    stack = []
    if absolute:
        stack.append("/")
    else:
        stack.append(path[0])

    for segment in range(1, len(path)):
        if path[segment] == "..":
            try:
                y = stack[-1]
            except:
                y = None
            if absolute:
                if y != "/":
                    stack.pop() 
            else:
                if y == ".." or y is None:
                    stack.append(path[segment])
                else:
                    stack.pop()
        elif path[segment] == "": # These are my extra /
            pass
        else:
            stack.append(path[segment])

    return ("/").join(stack) if not absolute else "/" + ("/").join(stack[1:])


if __name__ == "__main__":

    path = "/foo/../test/../test/../foo//bar/./baz"
    # /foo/bar/baz
    #path = "foo/../test/../test/../foo//bar/./baz"
    # foo/bar/baz
    #path = "../../foo/../../bar/baz"
    # what they want ../../../bar/baz

    print(shortenPath(path))
