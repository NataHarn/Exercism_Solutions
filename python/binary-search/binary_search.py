index = 0 # global var to store ans index
def find(search_list, value):
    global index
    length = len(search_list)
    if length == 0:
        raise ValueError("value not in array")
    n = length//2 # index of the middle member
    # base case
    if value == search_list[n]:
        index += n
        ans, index = index, 0 # set global index to 0
        return ans
    elif value > search_list[n]:
        index += n + 1
        return find(search_list[n+1:], value)
    else:
        return find(search_list[:n], value)
        
    
