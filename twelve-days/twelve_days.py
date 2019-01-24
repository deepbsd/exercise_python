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

    result = []

    for daynum in range(start_verse-1, end_verse):
        day = days[daynum]
        refrain = "On the {} day of Christmas my true love gave to me: ".format(day)
        if day == "first": 
            verse = refrain + "".join(gifts[daynum::-1]).replace("and ","",1) + "."
        else: 
            verse = refrain + ", ".join(gifts[daynum::-1]) + "."
        result.append(verse)

    return result

    


if __name__ == "__main__":
    print(recite(1,12))

