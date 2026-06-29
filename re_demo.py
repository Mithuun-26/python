import re
text = "My name is Prince. My roll number is 12345. Email: prince@gmail.com"
print("Original Text:")
print(text)
print("\n1. match()")
result = re.match(r"My", text)
print(result.group() if result else "No match")
print("\n2. search()")
result = re.search(r"Prince", text)
print(result.group() if result else "Not found")
print("\n3. findall()")
numbers = re.findall(r"\d+", text)
print(numbers)
print("\n4. finditer()")
for match in re.finditer(r"\w+", text):
    print(match.group(), "->", match.start())
print("\n5. sub()")
new_text = re.sub(r"Prince", "John", text)
print(new_text)
print("\n6. split()")
words = re.split(r"\s+", text)
print(words)
print("\n7. Email Validation")
email = "prince@gmail.com"
pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
print("\n8. Common Patterns")
sample = "Python123"
print("Digits:", re.findall(r"\d", sample))
print("Letters:", re.findall(r"[A-Za-z]", sample))
print("Word Characters:", re.findall(r"\w", sample))
print("Non-word Characters:", re.findall(r"\W", sample))
print("Whitespace:", re.findall(r"\s", "Python is fun"))
print("Starts with Python:", bool(re.match(r"^Python", sample)))
print("Ends with 123:", bool(re.search(r"123$", sample)))
print("\n9. Phone Number")
phone = "Contact: 9876543210"
match = re.search(r"\d{10}", phone)
if match:
    print("Phone:", match.group())
print("\n10. Extract Email")
text2 = "Contact us at support@example.com"
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text2)

print(emails)
