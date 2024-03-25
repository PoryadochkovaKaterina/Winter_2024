def AGTC(text, ch1, ch2, ch3, ch4, ch5, ch6):
    text = text.replace(ch2, ' ')
    text = text.replace(ch1, ch2)
    text = text.replace(' ', ch1)
    text = text.replace(ch3, ch5)
    text = text.replace(ch4, ch6)
    return text

print(AGTC(input().upper(), 'ГА','АГ', 'ТЦ', 'ЦТ', 'ТАГЦ', 'ЦАГТ'))