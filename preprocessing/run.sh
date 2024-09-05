rm -rf .snakemake
rm hist/*.bam
rm hist/*.tagAlign
rm hist/._*
rm hist/*.bedGraph
snakemake --resources network=1 -j 8 --restart-times 3 

