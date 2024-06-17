from collections import deque

class Solution:
    def firstPalindrome(self, words):
        # is_palindrome = lambda x: x == x[::-1]
        # def is_palindrome(s):
        #     deq = deque(s)
        #     while len(deq) > 1:
        #         if deq.popleft() != deq.pop():
        #             return False
        #     return True
        def is_palindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        for word in words:
            if is_palindrome(word):
                return word
        return ""
    

s = Solution()
assert s.firstPalindrome(["xngla","e","itrn","y","s","pfp","rfd"]) == "e"
assert s.firstPalindrome(["umicrszeaswtfmctwvoogehszwdjrwdcgyxxetbzevxrqphubyqbgpfetguyv","vzdzfwyevkvqhmvqssnvpayihawydzcovzmh","drvqqepesvornphmikbimxennygxisdysssmxjmaaecaqiwdgfxitoopigxauoojsebjmbcrymvpnnfomlkg","vvszfvtykdyfiywxgxmjpcawzdaovbujmexggwczovhspkrdsskxzrpgfaspnbncdspktcyfkkshpyojwwlysizd","epdtgfhgninnwqzztwm","dmhynaogcxyaxsghzjwzyqfuwyinstxoqcdkxeobinpqeplw","ruhxgdrzfyqyqmxclfqosyczqapiizxlzgixdxthhrv","dwcblqnxtrwtqmtqenidhxnifdbmdvobwmcvwjxgbyjzgvrqzlskjbfirauguhyyjhlotuckssrkqzppzbqd","gxdq","paesyowqeguvxozbixjqppeagycjx","glstauwugkidegnllapgzbzchckepmhbameuigsiqywbilwolxuwzzjwzouqknhlkbjzejxtponmkqjlojurxnryxyqy","inyhioiwanafuhsprudtkqztoakxhbmqcmibsxlhycbmqrvtfabsncmiymthcxwkwkq","djknenppuleedpptrfjgqfejcoghnxjlvjalxkyvnujgiiwdbtvgqvgsivkzqcrbfcvooyhqmrlacyiozytmampjwpknrj","zzrpjoogwkdmdxdkdwgwugqtmzryrgtelnvydyqewpdzzptqzvffppgnhhcaiqotmyslntlwjajzuzbawidpxjtyxryg","xmegifttkamzbpjqbghgwdrkvtnuwfmjdmwehdqiyvgpxxlbkcvkemjbmhbyeqyfssytuwaeysvgnidhcgpncxdxxzhrkbvyqfrs","wgljaiyhyfdijjgihseciabfcoqfojhswewpkpartzmaaglvdfifpptycyonigwcgyklapzojivgojcrevugspejmwanolg","oceurgzgvvctgydqexhghwcochhmtoxjugreqfdnsshffngchetrwedhinosdhwlgviohpkjowr","dyl","vjxkcihfmnmmz","aheg","dwsomlqmaqifihkwahvywzqamgominhxfsgrgbgvoiopnikhxonpetelfsguvhxgiujrij","pdrjgfqzyqczpwdsfzypgkmsvnpboutmcffqrwuzkchaufymmczrdwulbvbanungpxqk","eudbizaabgfzqytowifsuovmxmkjgajtliyfycbrkxeaarakapqoihawmdzmglfnglpwqnfd","txdclnfwxevu","kslqrafjshhadqszeljcekrpnpxqgppbnadmzmpufvadcghxqdqmafpbnutifigstxyilmgx","yhhvhyoolv","sjtubggxcla","vydf"]) == ""