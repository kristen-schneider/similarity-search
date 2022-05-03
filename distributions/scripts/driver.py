import sys
import read_map_file

map_file = sys.argv[1]
def main():
    read_map_file.cm_kmers(map_file)


if __name__ == '__main__': 
    main()
