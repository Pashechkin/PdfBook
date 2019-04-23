def slicer(lst: list, limit):
    retlist = []
    while len(lst) >= limit:
        retlist.append(lst[0:limit])
        lst = lst[limit:]
    if len(lst) > 0:
        retlist.append(lst)
    return retlist
