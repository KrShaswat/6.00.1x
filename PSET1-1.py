#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5
#Code below
v ='aeiou'
sum = 0
for n in range(len(s)):
    for n1 in range(len(v)):
        if s[n] == v[n1]:
            sum += 1
            break
print (sum)
