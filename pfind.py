from os import walk
from os.path import join
import argparse

ResultsLists = [[], []]


def FindStr(Dir, SearchStr, Sensitive):

    if not Sensitive:
        SearchStr = SearchStr.upper()

    for (dirpath, dirnames, filenames) in walk(Dir):
        for dname in dirnames:
            if not Sensitive:
                tmpdname = dname.upper()
                if SearchStr in tmpdname or SearchStr == tmpdname:
                    ResultsLists[0].append(join(dirpath, dname))
            else:
                if SearchStr in dname or SearchStr == dname:
                    ResultsLists[0].append(join(dirpath, dname))

        for fname in filenames:
            if not Sensitive:
                tmpfname = fname.upper()
                if SearchStr in tmpfname or SearchStr == tmpfname:
                    ResultsLists[1].append(join(dirpath, fname))
            else:
                if SearchStr in fname or SearchStr == fname:
                    ResultsLists[1].append(join(dirpath, fname))


def PrintResults():

    if len(ResultsLists[0]) > 0:
        print("\nDirectories found:")
        for Dirs in ResultsLists[0]:
            print(str(Dirs))

    if len(ResultsLists[1]) > 0:
        print("\nFiles found:")
        for Files in ResultsLists[1]:
            print(str(Files))
        print("\n")


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("Directory")
    parser.add_argument("SearchString")
    parser.add_argument("-s", "--sensitive", help="Turns ON case sensitive search", action="store_true")
    args = parser.parse_args()

    if args.sensitive:
        print("Case sensitive search is ON")
    else:
        print("Case sensitive search is OFF")

    FindStr(args.Directory, args.SearchString, args.sensitive)

    print("Total directories found: ", str(len(ResultsLists[0])))
    print("Total files found: ", str(len(ResultsLists[1])))

    if len(ResultsLists[0]) + len(ResultsLists[1]) > 0:
        answer = input("Would you like to print results? [Y/N]: ")

        if answer == 'Y' or answer == 'y':
            PrintResults()

if __name__ == "__main__":
    main()
