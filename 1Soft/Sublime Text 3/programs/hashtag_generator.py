'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
'''
def generate_hashtag(s):
    #your code here
    if len(s) < 1:
        return False
    
    s0 = '#'
    s_capitalized = s.title()
    result = s0 + s_capitalized.replace(' ', '')
    
    max_len = 140
    if len(result) > max_len:
        return False
    
    return result