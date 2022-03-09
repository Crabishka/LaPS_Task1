# критерии подмассива
# наибольшая сумма
# длина
# из равных длин - выбираем первый
def max_subarray(array):
    if len(array) == 0:
        return []
    max_sum = array[0] if array[0] > 0 else 0  # максимальная сумма
    dp_array = [0 for x in range(0, len(array))]
    curr_l = 0
    max_l = 0
    max_r = 0
    for i in range(0, len(array)):
        if array[i] + dp_array[i - 1] > 0:
            dp_array[i] = array[i] + dp_array[i - 1]
        else:
            dp_array[i] = 0
            curr_l = i + 1
        if dp_array[i] >= max_sum:
            max_sum = dp_array[i]
            if i - curr_l > max_r - max_l:
                max_r = i
                max_l = curr_l
    if max_r == max_l:
        return []
    else:
        return array[max_l:max_r + 1:]
