words = ['Anna', 'Civic', 'Kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку']
for i in words:
    if str.lower(i) == str.lower(i)[: : -1]:
        print(i, "- Is Palindrome")
    else:
        print(i, "- Not Palindrome")
