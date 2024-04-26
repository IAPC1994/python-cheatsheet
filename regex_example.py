import re
import camelcase

txt = "The rain in Spain"
txt2 = "hello world"
x = re.search("^The.*Spain$", txt)
y = re.findall("ai", txt)
z = re.search("\s", txt)
s = re.split("\s",txt)
r = re.sub("\s", ",", txt, 2)

cc = camelcase.CamelCase()


print(x)
print(y)
print(f"The first white-space character is located in position: { z.start() }")
print(f"The first white-space character is end in position: { z.end() }")
print(s)
print(r)
print(z.span())
print(z.string)
print(z.group())
print(cc.hump(txt2))

"""
Methods: 

findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
"""

"""
Metacharacters:

]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group

"""