#Quotes inside quotes, as long as they don't match the quotes surrounding the string
print("It's alright")
print("He is called 'Johnny'")
print('He is called"Johnny"')

#Multiline Strings
a = """Lorem ipsum dada
dadadedaefnui
fafhiaefna
afeifaeifaeifnea
afaifeafiafinefi."""
print(a)
a = '''fauefbeaufea
afeuafaeub
faeu.'''
print(a)

#Strings are Arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x in "banana":
    print(x)

#String length
a = "Hello, World!"
print(len(a))

#Check String
txt = "The best things in life are free!"
print("free" in txt)
print("Hello" in txt)
if "free" in txt:
    print("Yes, 'free' is present.")

#Check if NOT
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

#Slicing
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

#Upper Case
a = "Hello, World!"
print(a.upper())

#Lower Case
a = "Hello, World!"
print(a.lower())

#Remove Whitespace
a = " Hello, World! "
print(a.strip())

#Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
a = "Hello, World!"
print(a.split(","))

#String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#F-String
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifers
price = 59
txt = f"The price is {price} dollars" # Placeholder
print(txt)
txt = f"The price is {price:.2f} dollars" #Placeholder with modifer by adding a colon ":" followed by a legal formatting type
print(txt)
txt = f"The price is {20 * 59} dollars"
print(txt)

#Escape Character with backslash \
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
txt = "\!+\\+\n+\r+\t+\b+\f+\110\145\154\154\157+\x48\x65\x6c\x6c\x6f"
print(txt)