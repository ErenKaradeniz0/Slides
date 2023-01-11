def main():
    search_word = get_word()
    file = open("text/imdb.txt")
    line = search(file, search_word)

    if (len(line) > 0):
        print("Rank\tvotes\tRating\tTitle")
        matches = 0
        while (len(line) > 0):
            display(line)
            line = search(file, search_word)
            matches += 1
            print(str(matches)+" matches. ")


def get_word():
    search_word = input("Search word: ")
    search_word = search_word.lower()
    print()
    return search_word


def search(file, search_word):
    for line in file:
        line_lower = line.lower()
        if (search_word in line):
            return line
        return ""


def display(line):
    parts = line.split()
    rank = parts[0]
    rating = parts[1]
    votes = parts[2]
    title = ""
    for i in range(3, len(parts)):
        title += parts[i]+" "
    print(rank + "\t" + votes + "\t" + rating + "\t" + title)

main()