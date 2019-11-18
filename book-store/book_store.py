def calculate_total(books):

    price = 8.0
    discounts = {1:0, 2:0.05, 3:0.10, 4:0.20, 5:0.25}
    #total_cost = 0.0
    total_discount = 0.0
    purchase_groups = {}
    book_groups = []
    book_regroups = []

    def grouper(purchases_dict):
        '''Make the max number of longest groups possible 
        from purchases_dict supplied.  Longer groups,
        greater discounts applied, lowest cost to 
        customer. This function returns an array of
        dictionaries.'''
        newgroup = {}

        for (book, copies) in purchases_dict.items():
            if copies > 0:
                newgroup[book] = 1
                purchases_dict[book] -= 1
        if (len(newgroup) > 0 ): book_groups.append(newgroup)

        '''recurse through dictionary until no books remain, then 
        return the array of book groups'''
        if sum(purchases_dict.values()) > 0:
            return grouper(purchases_dict)
        else:
            return book_groups

    def regrouper(purchase_arr):
        print("Regroup - PD: {}".format(purchase_dict))
        """Take a purchase dict and balance the length of the two dicts"""
        new_regroup = []
        if len(purchase_arr[0]) != len(purchase_arr[1]):
            diff = abs(len(purchase_arr[0]) - len(purchase_arr[1]))
            for key in purchase_arr[0].keys():
                if key not in purchase_arr[1].keys():
                    purchase_arr[0].pop(key)
                    purchase_arr[1][key] = purchase_arr[0][key]
                    new_regroup.append(purchase_arr[0])
                    new_regroup.append(purchase_arr[1])
            diff -= 1
        return new_regroup


    def make_purchase_dict(books):
        purchase_dict = {1:0, 2:0, 3:0, 4:0, 5:0}
        for book in books:
            '''Create a dictionary of quantities for each volume'''
            purchase_dict[book] += 1
        return purchase_dict


    def compute_cost(dict):
        discount = discounts[len(dict.values())]
        price = len(dict.values()) * 8.00
        total = price - (price*discount)
        return total

    purchase_dict = make_purchase_dict(books)

    groups = grouper(purchase_dict)
    print("Groups: {}".format(groups))
    regroups = regrouper(groups)
    print("regroup: {}".format(regroups))

    total_cost1 = 0
    for dict in groups:
        total_cost1 += compute_cost(dict)

    total_cost2 = 0
    for dict in groups1:
        total_cost2 += compute_cost(dict)

    print("1: {}, 2: {}".format(total_cost1, total_cost2))

    return min([int(total_cost1 * 100), int(total_cost2 * 100)])



if __name__ == "__main__":
    print(calculate_total([1,1,2,2,3,3,4,5]))


