def reverse_words_order_and_swap_cases(sentence):
    list_str = []
    for x in sentence:
        if x.isupper():
            x = x.lower()

        elif x.islower():
            x = x.upper()
        list_str.append(x)
    string_sentece = ""
    for x in list_str:
        string_sentece += x

    print(string_sentece)

    list_str2 = string_sentece.split(' ')
    list_str2 = list_str2[::-1]
    fix_str =" ".join(list_str2)
    print(fix_str)


reverse_words_order_and_swap_cases("aWESOME is cODING")