import string
print("Welcome to my Password Strengther Determiner")
password = input("Insert your password:")
#factors determining password strength
#-length(12-16 letters is strong)
#-character variety(numbers,uppercase letters,special symbols)

if len(password) <5:
     print("Length:Bad")
     score = 1
elif 5<= len(password) < 10:
    print("Length:Mediocre")
    score = 2
elif 10<= len(password) < 15:
    print("Length:Good")
    score = 3
elif len(password)>15:
    print("Length:Excellent")
    score = 4
    
   

# checks for specific factors
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in string.punctuation for c in password)


VarietyScore = has_upper + has_lower+has_digit+has_special

if VarietyScore == 3:
    print("Variety:Good")
elif VarietyScore == 4:
    print("Variety:Excellent")
elif VarietyScore == 2:
    print("Variety:Average")
elif VarietyScore == 1:
    print("Variety:Bad")
 
OverallScore = score + VarietyScore
print("OverallScore:",OverallScore,"out of 8")

if OverallScore <= 4:
    print("Password Strength:Weak")
elif 4< OverallScore <=6:
    print("Password Strenght:Good")
elif 6< OverallScore <=8:
    print("Password Strength:Strong")




      
     
 
