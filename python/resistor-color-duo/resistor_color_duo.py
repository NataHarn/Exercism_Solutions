# func to calculate value
def value(colors):
    color_lst = ["black", "brown", "red", "orange","yellow",
                 "green", "blue", "violet", "grey", "white"]
    return color_lst.index(colors[0]) * 10 + color_lst.index(colors[1])
    
