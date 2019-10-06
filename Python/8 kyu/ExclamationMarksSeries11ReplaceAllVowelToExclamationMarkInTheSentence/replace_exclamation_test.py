import string, random

def correct(s):
   return "".join(['!' if _ in 'aeiouAEIOU' else _ for _ in s])

def letters(n):
    return "".join([random.choice(string.ascii_letters) for i in range(n)])

Test.describe("Random Tests")
for i in range(10):
    sequence = letters(10)    
    Test.assert_equals(replace_exclamation(sequence) , correct(sequence))