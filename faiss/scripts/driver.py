import read_vcf
import sample_major_format
import faiss_ss
import sys
import numpy as np

vcf_file = sys.argv[1]


def main():

    # read vcf file
    print('Reading VCF file...\n')
    genotypes = read_vcf.all_genotypes(vcf_file)
    print('...number of variants: ', len(genotypes))
    print('...number of samples: ', len(genotypes[0]))

    # transform / encode vcf genotype data
    print('\nTransposing genotype data to Sample Major Format (SMF)...')
    smf = sample_major_format.transpose_data(genotypes)

    # make queries
    d = len(smf[0])  # dimension
    num_queries = 4
    q_indices = [4, 728, 1786, 2311]
    queries = [smf[q_i] for q_i in q_indices]


    k = 25     # number of nearest neighbors to report

    # make (transform) genotype data the input data to similarity search
    print('\nConducting similarity search on transposed genotypes...')
    match_indices_flatL2 = faiss_ss.flatL2(smf, queries, k)
    # print(match_indices_flatL2)
    # match_indices_inner_product = faiss_ss.inner_product(smf, queries, k)
    # print(match_indices_inner_product)

    print('\nEnd.')


    # similarity search

if __name__ == '__main__':
    main()
