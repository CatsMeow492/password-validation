password = input()
special_chars = re.compile('[@_!#$%^&*()<>?/\|}{~:]') # regex expression to match all special chars
numbbers = re.compile('') # regex expression to match all numbers

if len(password) >= 7:  # Check if length is greater than 7


else:
    print("Weak")