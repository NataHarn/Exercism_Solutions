def transform(legacy_data):
    new_format = dict()
    for point in legacy_data:
        for letter in legacy_data[point]:
            new_format[letter.lower()] = point
    return new_format