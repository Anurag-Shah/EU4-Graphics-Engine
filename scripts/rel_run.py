relstr = "%s = { change_religion = rel_8b_%s }"

j = 40
for i in range(8, 32008):
    print(relstr % (i, j))
    j = j + 1
    if j == 240:
        j = 40