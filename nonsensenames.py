first = ["stinky", "lumpy", "buttercup", "gidget", "crusty", "greasy", "fluffy",
        "cheeseball", "chim-chim", "poopsie", "flunky", "booger", "pinky", "zippy",
        "goober", "doofus", "slimy", "loopy", "snotty", "falafel", "dorkey", "squeezit",
        "oprah", "skipper", "dinky", "zsa-zsa"]

second = ["diaper", "toilet", "giggle", "bubble", "girdle", "barf", "lizard", "waffle",
            "cootie", "monkey", "potty", "liver", "banana", "rhino", "burger", "hamster",
            "toad", "gizzard", "pizza", "gerbil", "chicken", "pickle", "chuckle", "tofu",
            "gorilla", "stinker"]

third = ["head", "mouth", "face", "nose", "tush", "breath", "pants", "shorts", "lips",
        "honker", "butt", "brain", "tushie", "chunks", "hiney", "biscuits", "toes",
        "buns", "fanny", "sniffer", "sprinkles", "kisser", "squirt", "humperdinck", "brains", "juice"]

name = input("What is your name? ").lower().split(" ")

newname = ""
newname += first[ord(name[0][0]) - ord("a")] + " "
newname += second[ord(name[1][0]) - ord("a")]
newname += third[ord(name[1][-1]) - ord("a")]

print(newname.title())
