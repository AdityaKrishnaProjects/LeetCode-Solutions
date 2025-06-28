# standardize input so always ends with /. Backslashes mark bounds of possible 
# names. Check for if name should be removed from stack (name = ".."), check if 
# name is empty ("" or "."), then append name to stack.
def simplifyPath(path):

    path += "/"
    stack = []
    name = ""

    for char in path:
        if char == "/":
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)
            name = ""
        else:
            name += char

    return "/" + "/".join(stack) if stack else "/"

print(simplifyPath("/home/"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/home/user/Documents/../Pictures"))
print(simplifyPath("/../"))
print(simplifyPath("/.../a/../b/c/../d/./"))
print(simplifyPath("/...//////abdc/"))
print(simplifyPath("/home/blah/gleeb/../../../../.."))