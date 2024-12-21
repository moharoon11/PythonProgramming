#Strings

name = "moharoon"
print(name);
print(name.upper())
print(name.lower())
print(name.replace("m", "M"))
print(len(name))
print("haroon" in name)
print("mohammed" not in name)
print("haroon" not in name)

# Multiline strings but comes in single line

# 1 way
aboutMe = "My name is Mohammed Haroon" \
    "Right now im exploring python" \
    "this language is pretty cool and" \
    "simpler to learn... so far"

print(aboutMe)

# 2 way of multiple line strings
whyIamLearningPython = """
  The is the most famous language and 
  very simpler to learn most of it's 
  getting used in every other field
"""

# String formatting
aboutYourSelf = "My name is {} and I completed my degree in {}"

aboutYourselfMore = """
 I am {} and i learned 
 {}, {} in my college days
 and built more project like 
 {}, {} and much more
"""

brotherName = "Mohamed Sameer"
skill1 = "java"
skill2 = "node js"
project1 = "project1"
project2 = "project2"
aboutMyBrother = f"""
 I am {brotherName} and i learned 
 {skill1}, {skill2} in my college days
 and built more project like 
 {project1}, {project2} and much more
"""

print(aboutYourSelf.format("BSc-IT", "2023"))
print(aboutYourselfMore.format("haroon", "java", "springboot", "blogging api", "Portfolio management api"))
print(aboutMyBrother)
# single line comments
"""
  We can use this quotes to 
  make multiple line comments 
  in your code.
"""