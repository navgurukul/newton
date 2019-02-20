```ngMeta
name: chapter-7
```
# Chapter 7
The re.compile() function returns Regex objects.

Raw strings are used so that backslashes do not have to be escaped.

The search() method returns Match objects.

The group() method returns strings of the matched text.

Group 0 is the entire match, group 1 covers the first set of parentheses, and group 2 covers the second set of parentheses.

Periods and parentheses can be escaped with a backslash: \., \(, and \).

If the regex has no groups, a list of strings is returned. If the regex has groups, a list of tuples of strings is returned.

The | character signifies matching “either, or” between two groups.

The ? character can either mean “match zero or one of the preceding group” or be used to signify nongreedy matching.

The + matches one or more. The * matches zero or more.

The {3} matches exactly three instances of the preceding group. The {3,5} matches between three and five instances.

The \d, \w, and \s shorthand character classes match a single digit, word, or space character, respectively.

The \D, \W, and \S shorthand character classes match a single character that is not a digit, word, or space character, respectively.

Passing re.I or re.IGNORECASE as the second argument to re.compile() will make the matching case insensitive.

The . character normally matches any character except the newline character. If re.DOTALL is passed as the second argument to re.compile(), then the dot will also match newline characters.

The .* performs a greedy match, and the .*? performs a nongreedy match.
Either [0-9a-z] or [a-z0-9]
'X drummers, X pipers, five rings, X hens'
The re.VERBOSE argument allows you to add whitespace and comments to the string passed to re.compile().
re.compile(r'^\d{1,3}(,\d{3})*$') will create this regex, but other regex strings can produce a similar regular expression.

re.compile(r'[A-Z][a-z]*\sNakamoto')
re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)
