class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = []
        for i in path.split("/"):
            if i == "" or i == ".":
                continue
            elif i == "..":
                if s:
                    s.pop()
            else:
                s.append(i)
        return "/" + "/".join(s)