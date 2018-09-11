#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2
out = 0
for n in range(0,len(s)+1):
    if n>2:
        if s[n-3:n] == 'bob':
            out+=1
print(out)
