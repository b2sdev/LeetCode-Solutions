class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for component in path.split("/"):
            if component == "..":
                if stack:
                    stack.pop()
            elif component and component != ".":
                stack.append(component)
        return "/" + "/".join(stack)


s = Solution()
assert s.simplifyPath("/home//foo/") == "/home/foo"
assert s.simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures"
assert s.simplifyPath("/../") == "/"
assert s.simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d"
