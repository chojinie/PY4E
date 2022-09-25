fh = open('../guest_book.txt')

for lx in fh:
    ly = lx.rstrip()


def wrong_guest_book():
    if ly.starswith('010') and ly.find('-') == 4 and ly.find('-') == 9 :
        pass
    else :
        print(ly)

wrong_guest_book()