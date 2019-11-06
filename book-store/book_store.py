def calculate_total(books):

   # books should be a list of ints from 1-5
    price = 8.0
    discounts = {1:0, 2:0.05, 3:0.10, 4:0.20, 5:0.25}
    #purchase_dict = {1:0, 2:0, 3:0, 4:0, 5:0}
    total_cost = 0.0
    total_discount = 0.0
    purchase_groups = {}
    book_groups = []
    #distinct_books = 0

    def grouper(purchases_dict):
        '''Make the max number of longest groups possible 
        from purchases_dict supplied.  Longer groups,
        greater discounts applied, lowest cost to 
        customer. This function returns an array of
        dictionaries.'''
        newgroup = {}
        print("items: {}".format(purchases_dict.items()))
        for (book, copies) in purchases_dict.items():
            if copies > 0:
                newgroup[book] = 1
                purchases_dict[book] -= 1
        book_groups.append(newgroup)

        print("book_groups: {}".format(book_groups))


        '''recurse through dictionary until no books remain, then 
        return the array of book groups'''
        if sum(purchase_dict.values()) > 0:
            grouper(purchase_dict)
        else:
            print("groups: {}".format(book_groups))
            return book_groups


    def make_purchase_dict(books):
        purchase_dict = {1:0, 2:0, 3:0, 4:0, 5:0}
        for book in books:
            '''Create a dictionary of quantities for each volume'''
            print("book: {}".format(book))
            purchase_dict[book] += 1
            # this will be total cost before any discount
            #total_cost += price
        return purchase_dict


    #total_cost = sum([copies*price - discounts.get(copies,0) for copies in purchase_dict.values()])

    '''
    # compute discount for entire shebang without grouping
    #for booknum, book in enumerate(purchase.values()):
    #    if purchase[booknum+1]: distinct_books += 1
    #    discount_pct = discounts[distinct_books-1]


    #total_discount1 = total_cost*discount_pct
    #total_discount2 = grouper(purchase)
    #total_discount = max(total_discount1, total_discount2)

    #total_cost = int((total_cost - total_discount)*100)
    #return total_cost
    '''
    purchase_dict = make_purchase_dict(books)
    #print("last purchase_dict: {}".format(purchase_dict))

    groups = grouper(purchase_dict)
    print("last groups: {}".format(groups))

    return groups



if __name__ == "__main__":
    print(calculate_total([1,1,2,2,3,3,4,5]))


