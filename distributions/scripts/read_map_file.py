def cm_kmers(map_file):
    '''
    chromosome (1-22, X, Y or 0 if unplaced)
    rs# or snp identifier
    genetic distance position (morgans or centimorgans)
    base-pair position (bp units)
    '''
    cm_max = 1.
    cm_start = 0.
    curr_cm_len = 0. 
    cm_prev = 0.

    all_kmers = []   
    curr_kmer = []

    for line in map_file:
        L = line.rstrip().split()
        chrm = L[0]
        snp_id = L[1]
        cm = L[2]
        bp_position = L[3]

        cm_addition = cm - cm_prev
        
        temp_cm = curr_cm_len + cm
    
        # if we havent reached segment length,
        # add current pos and extend counts
        if temp_cm < cm_max:
            curr_kmer.append(L)
            cm_curr = temp_cm
            cm_prev = cm
        else:
            all_kmers.append(curr_kmer)
            curr_kmer = [L]
            cm_curr = temp_cm
            
