import sys

map_file = sys.argv[1]
def main():
    read_map(map_file)

def read_map(map_file):
    '''
    chromosome (1-22, X, Y or 0 if unplaced)
    rs# or snp identifier
    Genetic distance (morgans)
    Base-pair position (bp units)
    '''
    cm_max = 1.
    cm_curr = 0. 

    all_kmers = []   
    curr_kmer = []

    for line in map_file:
        L = line.rstrip().split()
        chrm = L[0]
        snp_id = L[1]
        cm = L[2]


        temp_cm = cm_curr + cm
        if temp_cm < cm_m:
            curr_kmer.append(L)
            cm_curr = temp_cm
        else:
            all_kmers.append(curr_kmer)
            curr_kmer = [L]
            cm_curr = temp_cm


    


if __name__ == '__main__': 
    main()
