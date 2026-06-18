import re

txt = "The rain in Spain"
# re.match finds the first matching word
# txt is the string and re.I ignores the case sensitivity
match = re.match("The rain", txt, re.I)
print(match)
# .span() helps find the start end index of string
span = match.span()
print(span)
# start , end helps to identify the starting index and ending index
start, end = span
print(start,end)
# 
substring = txt[start:end]
print(substring)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']
