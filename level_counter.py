from texts import texts 

def level_count(result_lst):

    lst = result_lst[1:]
    res = [eval(i) for i in lst]

    score = sum(res)

    if 0 <= score <= 41:
        return texts.first_level
    elif 42 <= score <= 50:
        return texts.second_level
    elif 51 <= score <= 70:
        return texts.third_level
    elif 71 <= score <= 100:
        return texts.forth_level
    elif 101 <= score <= 120:
        return texts.fifth_level
    else:
        return 'Повторите опрос: не все ответы на месте.'
    