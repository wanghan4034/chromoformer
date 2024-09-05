
import pandas as pd 
HG19_SIZES = 'annotations/hg19.fa.sizes'

EIDS = [
    'E003', 'E004', 'E005', 'E006', 'E007',
    'E016', 'E066', 'E087', 'E114', 'E116',
    'E118',
]

MARKS = [
    'H3K4me1',
    'H3K4me3',
    'H3K9me3',
    'H3K27me3',
    'H3K36me3',
    'H3K27ac',
    'H3K9ac',
]

TISSUE_MAPPING= pd.read_csv('annotations/tissue_mapping.csv')
EID2TISSUE = {r.eid:r.tissue for r in TISSUE_MAPPING.to_records()}