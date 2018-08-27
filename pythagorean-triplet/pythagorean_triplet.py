def primitive_triplets(number_in_triplet):
    pass


def triplets_in_range(range_start, range_end):
    triplets = []
    for x in range(range_start, range_end):
        for y in range(range_start, range_end):
            square = x**2 + y**2
            z = square ** 0.5
            if is_triplet((x,y,int(z))):
                if triplets.count(tuple(sorted((x,y,int(z))))) < 1:
                    triplets.append(tuple(sorted((x,y,int(z)))))
    return triplets




def is_triplet(triplet):
    triplet = sorted(triplet)
    return triplet[0]**2 + triplet[1]**2 == triplet[2]**2
