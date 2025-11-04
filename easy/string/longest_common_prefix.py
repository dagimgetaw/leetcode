class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        no_iteration = len(min(strs, key=len))
        temp = ""
        output = []

        for i in range(no_iteration):
            chars = [word[i] for word in strs]
            
            if i == 0 and len(set(chars)) != 1:
                return ""
            
            if len(set(chars)) == 1:
                temp += chars[0]
            else:
                output.append(temp)
                temp = ""
                break

        output.append(temp)
        new_output = [x for x in output if x.strip()]
        
        return new_output[0] if new_output else ""
