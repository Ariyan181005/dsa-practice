class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d={"2":("a","b","c"),"3":("d","e","f"),"4":("g","h","i"),"5":("j","k","l"),"6":("m","n","o"),"7":("p","q","r","s"),"8":("t","u","v"),"9":("w","x","y","z")}
        r = [""]
        for digit in digits:
            n = []
            for combination in r:
                for letter in d[digit]:
                    n.append(combination + letter)
            r = n
        return r  