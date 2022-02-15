#Return the number (count) of vowels in the given string.

#We will consider a, e, i, o, u as vowels (but not y).

#The input string will only consist of lower case letters and/or spaces.

#ex:
#get_count('hello_world') => 3


def count_vowels(s1):
    v=0
    vowels=('a','e','i','o','u')
    
    for char in s1:
        if char in vowels:
            v +=1

    return v

print(count_vowels('the great big dog'))
print(count_vowels('the quick brown fox jumped'))