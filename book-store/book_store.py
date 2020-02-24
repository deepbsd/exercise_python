discounts = [0, 0.05, 0.1, 0.2, 0.25]

def grouper(cart, length):
    prices = []

    while len(cart):
        books = []
        while len(books) < length:
            try:
                vol = next(v for v in cart if v not in books)
            except StopIteration:
                break
            cart.remove(vol)
            books.append(vol)
        if books: 
            p = 800 * len(books)
            prices.append(p - (p * discounts[len(books)-1]))

    return sum(prices)


def calculate_total(cart):
    return min(grouper(cart[:], i) for i in range(5, 1, -1))

