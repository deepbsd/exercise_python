def transform(oldObj):
    newObj = {}
    for points, letters in oldObj.items():
        for l in letters:
            newObj[l.lower()] = int(points)
    return newObj
