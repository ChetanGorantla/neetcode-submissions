class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [strs[0]]
        
        dct = {}
        for s in strs:
            clist = [0]*26
            for c in s:
                clist[ord(c)-ord('a')]+=1
            clist = str(clist)
            if clist not in dct:
                dct[clist] = list()
                
            dct[clist].append(s)
        return list(dct.values())
        
        

        