A repository to test different similarity searches on genomic variant data.


### FAISS ([Paper](https://pubmed.ncbi.nlm.nih.gov/34112768/), [Code](https://github.com/roohy/iLASH))<br>
`python .../faiss/scripts/driver.py ../toy_data/vcf/`<br>

### iLASH ([Post](https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/), [Code](https://github.com/facebookresearch/faiss))<br>
To convert vcf to pedmap: `plink2 --vcf ./vcf/hundred.vcf.gz --recode ped --out ./plink/hundred`<br>
`.../iLASH/build/ilash config_file`<br>

### shared sites:

### mann whitney u test:
