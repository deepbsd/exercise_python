def primitive_triplets(number_in_triplet):
    return triplets_in_range(1, number_in_triplet)


def triplets_in_range(range_start, range_end):
    triplets = []
    for x in range(range_start, range_end+1):
        for y in range(range_start, range_end+1):
            for z in range(range_start, range_end+1):
                if is_triplet((x,y,z)):
                    if triplets.count(tuple(sorted((x,y,z)))) < 1:
                        triplets.append(tuple(sorted((x,y,z))))
    return triplets




def is_triplet(triplet):
    triplet = sorted(triplet)
    return triplet[0]**2 + triplet[1]**2 == triplet[2]**2
