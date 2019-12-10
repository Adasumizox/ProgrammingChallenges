def longest_palindrome (s):
    longest = 0
    for left in range(len(s)):
        for right in range(len(s), left, -1):
            if s[left:right] in (s[left:right])[::-1]:
                longest = max(right-left, longest)
                break
    return longest