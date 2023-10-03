#!/usr/bin/python3
alphabets = ""
char = ""
for i in range(97, 123):
    char = chr(i)
    if char != 'q' and char != 'e':
        alphabets += char

print(alphabets)
