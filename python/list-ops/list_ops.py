def append(list1, list2):
    return [*list1, *list2]


def concat(lists):
    return [elem for list in lists for elem in list]


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    counter = 0
    while True:
        try:
            list[counter]
        except IndexError:
            return counter
        counter += 1

def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    for item in reverse(list):
        initial = function(item, initial)
    return initial


def reverse(list):
    return list[::-1]
