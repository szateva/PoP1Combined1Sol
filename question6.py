def shortest_atom(s):
    match = 0
    for i in range(1, len(s) + 1):
        if len(s) % i == 0:
            match = 0
        for j in range(0, len(s)):
            if s[j] == s[j % i]:
                match += 1
        if match == len(s):
            return s[:i]


assert shortest_atom("ababab") == "ab"
assert shortest_atom("abcabc") == "abc"
assert shortest_atom("abcab") == "abcab"
