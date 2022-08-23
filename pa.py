
import random
a = []  
a.append(random.choice('abcdefghijklmnopqrstuvwxyz') + random.choice(
    'abcdefghijklmnopqrstuvwxyz') + random.choice('abcdefghijklmnopqrstuvwxyz'))
a.append(random.choice('abcdefghijklmnopqrstuvwxyz') + random.choice(
    'abcdefghijklmnopqrstuvwxyz') + random.choice('abcdefghijklmnopqrstuvwxyz'))
a.append(random.choice('abcdefghijklmnopqrstuvwxyz') + random.choice(
    'abcdefghijklmnopqrstuvwxyz') + random.choice('abcdefghijklmnopqrstuvwxyz'))
a.append(random.choice('abcdefghijklmnopqrstuvwxyz') + random.choice(
    'abcdefghijklmnopqrstuvwxyz') + random.choice('abcdefghijklmnopqrstuvwxyz'))
a.append(random.choice('abcdefghijklmnopqrstuvwxyz') + random.choice(
    'abcdefghijklmnopqrstuvwxyz') + random.choice('abcdefghijklmnopqrstuvwxyz'))
a = ['asd','bbc','dob','ooc','bab']

print(a)  

b = ""     #
c = a[0]  
if c[0] in 'aeiou': 
    if c[1] not in 'aeiou':
        if c[2] not in 'aeiou':
            b += c
else:  
    if c[1] in 'aeiou':
        if c[2] not in 'aeiou':
            b += c
bbc
c = a[1] 
if c[0] in 'aeiou':  
    if c[1] not in 'aeiou':
        if c[2] not in 'aeiou':
            if b != "":
                b += "-"
            b += c
else:  
    if c[1] in 'aeiou':
        if c[2] not in 'aeiou':
            if b != "":
                b += "-"
            b += c
dob
c = a[2]  
if c[0] in 'aeiou': 
    if c[1] not in 'aeiou':
        if c[2] not in 'aeiou':
            if b != "":
                b += "-"
            b += c
else: 
    if c[1] in 'aeiou':
        if c[2] not in 'aeiou':
            if b != "":
                b += "-"
            b += c
ooc
c = a[3] 
if c[0] in 'aeiou': 
    if c[1] not in 'aeiou':
        if c[2] not in 'aeiou':
            if b != "":
                b += "-"
            b += c
else: 
    if c[1] in 'aeiou':
        if c[2] not in 'aeiou':
            if b != "":
                b += "-"
            b += c

c = a[4] 
if c[0] in 'aeiou':  
    if c[1] not in 'aeiou':
        if c[2] not in 'aeiou':
            if b != "":
                b += "-"
            b += c
else:  
    if c[1] in 'aeiou':
        if c[2] not in 'aeiou':
            if b != "":
                b += "-"
            b += c


if b == "":
    print("No luck this time...")
else:
    print("A possible word: " + b)