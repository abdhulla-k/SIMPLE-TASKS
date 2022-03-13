from dataclasses import replace


text = "WHAT IS THE MEMORANDOM OF ASSOSSIATION MEANS?\n"
text1 = """memorandom of assossiation is an importand document of a company. that includes 
the objectives, rules, position, name and more important data \n."""
text2 = 'omasser'
text3 = 'o\tm\ta\ts\ts\te\tr\ty'
text4 = ['tomato', 'watermilon', 'beetrute', 'cabage']
text5 = 'KERALA is the gods own country'

print(text.lower())
print(text1.upper())
print(text1.capitalize())
print(text2.center(20))
print(text1.count('m'))
print(text1.encode())
print(text1.endswith('.'))
print(text3.expandtabs(3))
print(text1.find('rules'))
print(text.index('M'))
print('#'.join(text4))

MyJoiner = '+'

print(MyJoiner.join(text4))
print(text2.replace('omasser', 'Kozhikode'))

te = 'one one two one'

print(te.replace('one', 'three', 2))
print(text1.rfind('d'))
print(text1.rsplit())
print(text5.swapcase())
print(text1.title())

current = '50'
print(current.zfill(20))