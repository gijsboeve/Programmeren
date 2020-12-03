list = ("hoi", "hallo", "kerel", "hi", "sam", "gijs")

words_until_sam = 0
for word in list:
    if word == "sam":
        break
    words_until_sam += 1

print("the total of the even numbers is", words_until_sam)