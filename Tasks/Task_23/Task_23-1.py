# text = 'ggabcdcbakjh'
text = input()
len_text = ""
for i in range(len(text)):
    for l, r in [(i, i), (i, i + 1)]:
        while l >= 0 and r < len(text) and text[l] == text[r]:
            l -= 1
            r += 1
            if len(len_text) < r - l - 1:
                len_text = text[l + 1: r]

print(len_text)



# Метод Манакера
# n = len(text)
# h = [0] * n
# C = R = 0      # центр и радиус или крайний правый палиндром
# besti, bestj = 0, 0     # центр и радиус самого длинного палиндрома
# for i in range(n):
#     if i < C + R:         # если есть пересечение
#         j = h[C-(i-C)]       # отражение
#         if j < C + R - i:    # случай A
#             h[i] = j
#             continue
#         elif j > C + R - i:  # случай B
#             h[i] = C + R - i
#             continue
#         else:                # case C
#             pass
#     else:                 # если нет пересечения
#         j = 0
#     while i-j > 0 and i+j<n-1 and text[i-j-1] == text[i+j+1]:
#         j += 1
#     h[i] = j
#     if j > bestj:
#         besti, bestj = i, j
#     if i + j > C + R:
#         C, R = i, j
# print(text[besti-bestj : besti+bestj+1])
#
