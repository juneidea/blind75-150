def minWindow(s: str, t: str) -> str:
     if t == "": return ""
     target, window = {}, {}

     for c in t:
          target[c] = 1 + target.get(c, 0)
     have, need = 0, len(target)
     res, resLen = [], len(s)
     l = 0
     for r in range(len(s)):
          c = s[r]
          window[c] = 1 + window.get(c, 0)
          if c in target and window[c] == target[c]:
               have += 1
          
          while have == need:
               # update result
               if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
               # pop left out of window
               window[s[l]] -= 1
               if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
               l += 1
     l, r = res
     return s[l:r+1]

s1, t1 = "ADOBECODEBANC", "ABC" # BANC
print(minWindow(s1, t1))
