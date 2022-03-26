def is_anagrams(str_1, str_2):
    len_str_1 = len(str_1)
    len_str_2 = len(str_2)

    if len_str_1 != len_str_2:
        return False

    sort_str_1 = sorted(str_1.lower())
    sort_str_2 = sorted(str_2.lower())

    for i in range(0, len_str_1):
        if sort_str_1[i] != sort_str_2[i]:
            return False
    return True