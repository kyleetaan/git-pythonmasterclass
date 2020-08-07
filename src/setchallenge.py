string = """ Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. Curabitur ipsum nisl, 
efficitur lobortis nisi nec, sagittis sollicitudin eros. 
Etiam iaculis. """

vowel = frozenset("aeiou")
# vowel = {'a', 'e', 'i', 'o', 'u'}

finalSet = set(string).difference(vowel)
final_list = list(sorted(finalSet))

print(final_list)