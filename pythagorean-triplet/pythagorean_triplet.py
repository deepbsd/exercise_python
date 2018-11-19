def primitive_triplets(number_in_triplet):
    triplets = []

    for triplet in triplets_in_range(int(number_in_triplet**0.5), number_in_triplet**2):
        if number_in_triplet in triplet:
            triplets.append(triplet)
    return set(triplets)



def triplets_in_range(range_start, range_end):
    triplets = []
    for x in range(range_start, range_end+1):
        for y in range(range_start, range_end+1):
            for z in range(range_start, range_end+1):
                if is_triplet((x,y,z)):
                    if triplets.count(tuple(sorted((x,y,z)))) < 1:
                        triplets.append(tuple(sorted((x,y,z))))
                        print("triplets: ", triplets)
    return set(triplets)




def is_triplet(triplet):
    triplet = sorted(triplet)
    return triplet[0]**2 + triplet[1]**2 == triplet[2]**2 and triplet[0]<triplet[1]<triplet[2]
