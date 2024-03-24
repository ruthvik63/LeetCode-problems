s=input()
roman_values={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}
total=0
prevs_value=0

for symbol in s:
    value=roman_values[symbol]
    if value>prevs_value:
        total+=value-2*prevs_value
    else:
        total+=value
    prevs_value=value
print(total)