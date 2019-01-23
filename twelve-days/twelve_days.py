def recite(start_verse, end_verse):

    days = ["first", "second", "third", "fourth","fifth", "sixth","seventh",
            "eighth", "ninth", "tenth", "eleventh", "twelfth"]

    gifts = [
            "a Partridge in a Pear Tree",
            "two Turtle Doves",
            "three French Hens",
            "four Calling Birds",
            "five Gold Rings",
            "six Geese-a-Laying",
            "seven Swans-a-Swimming",
            "eight Maids-a-Milking",
            "nine Ladies Dancing",
            "ten Lords-a-Leaping",
            "eleven Pipers Piping",
            "twelve Drummers Drumming",
            ]

    if start_verse > 1: gifts[0] = "and a Partridge in a Pear Tree"

    dict = { "first": "".join(gifts[0]),
            "second": ", ".join(gifts[1::-1]),
            "third": ", ".join(gifts[2::-1]),
            "fourth": ", ".join(gifts[3::-1]),
            "fifth": ", ".join(gifts[4::-1]),
            "sixth": ", ".join(gifts[5::-1]),
            "seventh": ", ".join(gifts[6::-1]),
            "eighth": ", ".join(gifts[7::-1]),
            "ninth": ", ".join(gifts[8::-1]),
            "tenth": ", ".join(gifts[9::-1]),
            "eleventh": ", ".join(gifts[10::-1]),
            "twelfth": ", ".join(gifts[11::-1]),
            }

    refrain = "On the {} day of Christmas my true love gave to me: ".format(days[start_verse-1])

    result = [refrain]

    for daynum in range(start_verse-1, end_verse):
        day = days[daynum]
        verse = refrain + "".join(dict[day]) + "."
        result[0] = verse

    return result

    


if __name__ == "__main__":
    print(recite(3,3))

