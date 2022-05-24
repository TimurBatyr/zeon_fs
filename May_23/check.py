import filecmp

file1 = 'test.txt'
file2 = 'ModelDecomposition.txt'
comp = filecmp.cmp(file1, file2, shallow=True)
print(comp)