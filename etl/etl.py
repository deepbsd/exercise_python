def transform(oldObj):
    return {l.lower() : points for points, letters in oldObj.items() for l in letters}
