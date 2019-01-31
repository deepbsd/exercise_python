def calculate_total(books):
    # books should be a list of ints from 1-5
    price = 8.0
    discounts = [0, 0.05, 0.10, 0.20, 0.25]
    purchase = {1:0, 2:0, 3:0, 4:0, 5:0}
    total_cost = 0.0
    total_discount = 0.0
    distinct_books = 0

    for book in books:
        purchase[book] += 1
        # this will be total cost before any discount
        total_cost += price

    for booknum, book in enumerate(purchase.values()):
        if purchase[booknum+1]: distinct_books += 1

    for booknum, copies in enumerate(purchase.values()):
        total_discount += ((copies*price) - (price*copies*discounts[copies-1]))

    total_cost = int((total_cost - total_discount)*100)
    return total_cost







if __name__ == "__main__":
    print(calculate_total([1,1,1]))


