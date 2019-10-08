# Reference
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

def KMPSearch(pat, txt):
    m = len(pat)
    n = len(txt)

    # create lps[] that will hold the longest prefix suffix  
    # values for pattern 
    lps = [0]*m

    computeLPS(pat, m, lps)

    i = 0 # index of text
    j = 0 # index of pattern

    while(i < n):
        if pat[j] == txt[i]:
            j += 1
            i += 1
        if j == m:
            print("Found pattern at index: " + str(i-j))
            j = lps[j-1]
        elif i < n and pat[j] != txt[i]: # mismatch after j matches
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


def computeLPS(pat, m, lps):
    l = 0 # Length of previous longest prefix suffix

    # lps[0] is always 0
    i = 1

    while(i < m):
        if pat[i] == pat[l]:
            l += 1
            lps[i] = l
            i += 1
        else:
            # This is tricky. Consider the example. 
            # AAACAAAA and i = 7. The idea is similar  
            # to search step.
            if l != 0:
                l = lps[l-1]
            else:
                lps[i] = 0
                i += 1


txt = "ABABABCDCDABABABABABBBCDABCABABABABA"
pat = "ABAB"
KMPSearch(pat, txt)