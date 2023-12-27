##### Data types #####

#### String (perl necklace)
print("Hello"[len("Hello")-1])

#### Integer

123_456_678 # (python ignores the underscores, they are just there for readability)

#### Float

2577371.738748

#### Boolean

True, False  # starts with a capital letter always

#### type() is used to check data type
#### str(), int(), float(), bool(), float() are used for typecasting (starts with small letters)

print(type(len("2000")))

# print(int("3.14"))  #### error (only typecasts int-like strings)
# print(int("3"))
# print(float("3.14"))
# print(float("3"))
#### float() can typecast any string
#### int() only typecasts integer-like string 


##### Mathematical Operators #####

#### + , - , * , / , // , ** 

print(type(8/4))      # always gives float 

print(type(3//4))     # (floor division) always gives int

#### Operators always follow ---> PEMDAS <---

# ()
# **
# * /      (multiply, divide & add, subtract have same priority and always gets evaluated from left to right)
# + -

#### Round function ####

print(round(66.5))            # OUTPUT --> 66
print(round(67.5))            # OUTPUT --> 68
# rounds to the nearest even integer in case of "tie", even for floats

print(round(1.465, 2))        # OUTPUT --> 1.47
print(round(2.475, 2))        # OUTPUT --> 2.48
print(round(2.675, 2))        # OUTPUT --> 2.67
# does not work as expected, because of floating point arithmetic

print(round(2.675, -2))       # OUTPUT --> 0.0
print(round(224.675, -2))       # OUTPUT --> 200.0
# -ves are allowed, rounds to 10**(-[n-digit])


#### f-string ####
name = "MJF"
score = 5000.9870
isWinning = True

print(f"My name is {name}, my score is {score}. Am I winning? {isWinning}") 
# just like template literal (JS)