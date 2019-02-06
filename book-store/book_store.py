def calculate_total(books):

   # books should be a list of ints from 1-5
    price = 8.0
    discounts = [0, 0.05, 0.10, 0.20, 0.25]
    purchase = {1:0, 2:0, 3:0, 4:0, 5:0}
    total_cost = 0.0
    total_discount = 0.0
    distinct_books = 0
    
    def grouper(purchases_dict):
        groups = {'cost': 0}
        for book, copies in purchases_dict.items():
            newgroup = {'cost': 0}
            if copies: 
                groups[book] = 1
                #purchases_dict[book] -= 1
        for group in groups:
            discount = discounts[len(group)]
            group['cost'] += (len(group) * price) * discount
        groups['cost'] += group['cost']
        return groups['cost']
   

    for book in books:
        purchase[book] += 1
        # this will be total cost before any discount
        total_cost += price

    # compute discount for entire shebang without grouping
    for booknum, book in enumerate(purchase.values()):
        if purchase[booknum+1]: distinct_books += 1
        discount_pct = discounts[distinct_books-1]

    
    total_discount1 = total_cost*discount_pct
    total_discount2 = grouper(purchase)
    total_discount = max(total_discount1, total_discount2)


    total_cost = int((total_cost - total_discount)*100)
    return total_cost


        

    #def discounter(group, discounts):
    #    # this takes a group as argument and returns it as a dict with 
    #    # its discount as key
    #    pass


if __name__ == "__main__":
    print(calculate_total([1,1,2,2,3,3,4,5]))


