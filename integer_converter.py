result_dollars = '76,43'

res = result_dollars.replace(',', '.')
res = float(res)
print(res)


result = []
result_del_conv = []
for i in result_dollars:
    result.append(i)


def podbor(integ):
    for i in range(9):
        if int(integ) == i:
            return i


print(result)

result_del_conv.append(podbor(result[0]))
result_del_conv.append(podbor(result[1]))

print(result_del_conv)