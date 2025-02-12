word = raw_input().strip()

uppercase_count = sum(1 for c in word if c.isupper())
lowercase_count = len(word) - uppercase_count

if uppercase_count > lowercase_count:
    result = word.upper()
else:
    result = word.lower()
print(result)
