def disemvowel(string_):
    new_string = ""
    vocals = ['a', 'e', 'i', 'o', 'u', 'y', ]
    for i in string_:
        if i.lower() in vocals :continue
        new_string += i
    return(print(new_string))

disemvowel("This website is for losers LOL!")