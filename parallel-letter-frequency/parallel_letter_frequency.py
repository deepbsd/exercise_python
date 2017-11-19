def calculate(list):
    dict = {}
    for word in list:
        for char in word.lower():
            if char.isalpha() and char in dict:
                dict[char] += 1
            elif char.isalpha():
                dict[char] = 1
            else:
                next
    return dict
