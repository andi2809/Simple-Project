def get_count(sentence):
    hitung = []
    for x in sentence:
        if x in "aiueo":
            hitung.append(x)
    print(len(hitung))


get_count("awokwow")
