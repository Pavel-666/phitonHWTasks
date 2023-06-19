# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no


rows = int(input('введите размер по M '))
columns = int(input('введите размер по N '))
requiredNumberSlices = int(input('сколько долек вы хотите отломить? '))
if (requiredNumberSlices % rows == 0 or requiredNumberSlices % columns == 0) \
        and requiredNumberSlices < rows*columns:
    print(F'одним надрезом можно отломить {requiredNumberSlices} долек')
else:
    print(F'одним надрезом нельзя отломить {requiredNumberSlices} долек, или же столько долек нет в плитке')








