def recite(start_verse, end_verse):

    days = ["first", "second", "third", "fourth","fifth", "sixth","seventh",
            "eighth", "ninth", "tenth", "eleventh", "twelfth"]

    gifts = [
            "and a Partridge in a Pear Tree",
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

    dict = { "first": "".join(gifts[0]),
            "second": ", ".join(gifts[1::-1]),
            "third": ", ".join(gifts[2::-1]),
            "fourth": gifts[3::-1],
            "fifth": gifts[4::-1],
            "sixth": gifts[5::-1],
            "seventh": gifts[6::-1],
            "eighth": gifts[7::-1],
            "ninth": gifts[8::-1],
            "tenth": gifts[9::-1],
            "eleventh": gifts[10::-1],
            "twelfth": gifts[11::-1],
            }

    refrain = "On the {} day of Christmas my true love gave to me: ".format(days[start_verse-1])

    result = [refrain]

    for daynum in range(start_verse-1, end_verse):
        day = days[daynum]
        verse = refrain + "".join(dict[day])
        result[0] = verse

    return result

    


if __name__ == "__main__":
    print(recite(3,3))

