import sys
import read_map_file
import 

vcf_file = sys.argv[1]
map_file = sys.argv[2]

def main():
    
    # map variants to centimorgans
    #read_map_file.cm_kmers(map_file)

    # get slices by centimorgans
    # WORK AROUND: get slices by strict window
    


if __name__ == '__main__': 
    main()
