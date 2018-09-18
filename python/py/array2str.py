def array2str(array):
    str = ''
    for i in range(len(array)):
        if i == (len(array) - 1):
            str += 'and ' + array[i]
        else:
            str += array[i] + ', '
    return str

print(array2str(['apple', 'bananas', 'tofu', 'cats']))
