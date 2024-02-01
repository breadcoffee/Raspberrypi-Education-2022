def cut_list(ls):
    result = []
    for e in ls:
        if e % 2 == 1:
            result.append(e)
    return result
