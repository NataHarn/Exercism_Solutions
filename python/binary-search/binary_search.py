def find(search_list, value):
    length = len(search_list)
    if length == 0:
        raise ValueError("value not in array")
    n = length//2 # index of the middle member
    # base case
    if value == search_list[n]:
        return n
    elif value > search_list[n]:
        return find(search_list[n+1:], value) + (n + 1)
    else:
        return find(search_list[:n], value)
        
    
