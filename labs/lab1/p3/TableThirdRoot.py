# -*- coding: utf-8 -*-
"""
Table of third root Problem 3
Create a table with third root so that the solution is a dictionary where the key is the integer and the value is the third root of the integer.
The keys should be numbers whose third root is also an integer between two values m and n.
or a given input, print out the third root if it is already calculated in the dictionary.
If the dictionary doesn't contain the value print out that there is no data.
After that print out the sorted list of the key-value pairs from the dictionary.
"""

if __name__ == "__main__":
    m = input()
    n = input()
    x = input()
    # your code here
    tablica = {}
    for i in range(m, n+1):
        tablica[i*i*i] = i
    if x in tablica:
        print(tablica[x])
    else:
        print("nema podatoci")
    print(sorted(tablica.items()))
