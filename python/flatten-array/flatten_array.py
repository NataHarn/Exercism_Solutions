def flatten(iterable):
    items = []
    for item in iterable:
        if hasattr(item, '__iter__'):
            items.extend(flatten(item))
        else:
            if item != None:
                items.append(item)
    return items