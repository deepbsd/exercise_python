

def flatten(lst):

    def genr(container):
        for e in container:
            if isinstance(e, (list, tuple)):
                yield from flatten(e)
            elif e == None:
                continue
            else:
                yield e

    return list(genr(lst))

