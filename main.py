from musical import get_search_note, do_search

def main():
    while True:
        note = get_search_note()
        results = do_search(note)
        print(results)
        cont = input("Start new search?[y/n] ")
        if cont != "y":
            break

if __name__ == '__main__':
    main()