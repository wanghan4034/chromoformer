from tqdm import tqdm
import subprocess
from itertools import product
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.constants import *

def download(shells):

    def _func(shell):
        process = subprocess.Popen(shell,stdout=subprocess.PIPE, shell=True)
        for _, line in enumerate(process.stdout):
            decoded_line = line.decode('utf-8')
            if decoded_line.startswith('Length:'):
                total_size = int(decoded_line.split()[1])
            elif decoded_line.startswith('%'):
                progress = int(decoded_line.split()[0].replace('%', ''))
                tqdm.update(progress)

        process.stdout.close()
        process.wait()
    

    with ThreadPoolExecutor(max_workers=5) as executor: 
        future_to_url = {executor.submit(_func, shell): shell for shell in shells}

        for future in as_completed(future_to_url):
            shell = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print(f'{shell} error: {exc}')
            else:
                print(f'{shell} success')

def download_chip_tagalign():
    shells = [f'wget -c "https://egg2.wustl.edu/roadmap/data/byFileType/alignments/consolidated/{eid}-{mark}.tagAlign.gz" -O  hist/{eid}-{mark}.tagAlign.gz' for eid, mark in product(EIDS,MARKS)]
    download(shells)

def download_exp():
    url = 'https://egg2.wustl.edu/roadmap/data/byDataType/rna/expression/57epigenomes.RPKM.pc.gz'
    shells = [f"wget {url} -O- | gunzip -c |  'sed \'s/[ \\t]*$//\' > exp/raw_exp.tsv "]
    download(shells)

def download_frag2neighbors_per_tissue():
    shells = [f"wget https://dohlee-bioinfo.sgp1.digitaloceanspaces.com/chromoformer-data/{tissue}_frag2neighbors.pickle -O- > annotations/{tissue}_frag2neighbors.pickle" for tissue in EID2TISSUE.values()]
    download(shells)

def download_pair2score_per_tissue():
    shells = [f"wget https://dohlee-bioinfo.sgp1.digitaloceanspaces.com/chromoformer-data/{tissue}_pair2score.pickle -O- > annotations/{tissue}_pair2score.pickle" for tissue in EID2TISSUE.values()]
    download(shells)


if __name__ == '__main__':
    download_chip_tagalign()
    download_exp()
    download_frag2neighbors_per_tissue()
    download_pair2score_per_tissue()