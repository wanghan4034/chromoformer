export LD_LIBRARY_PATH=/GPUFS/sysu_jjzhang_3/.conda/envs/chromoformer/lib:$LD_LIBRARY_PATH
export WANDB_MODE=offline
nohup python chromoformer/train.py --config chromoformer/configs/default.yaml --meta preprocessing/meta_data_E003.csv  --npy-dir preprocessing/data/E003   --fold 0  -o model.pt --exp-id 123 > train.log 2>&1 &

nohup python chromoformer/train.py --config chromoformer/configs/default.yaml --meta preprocessing/meta_data_E003.csv  --npy-dir preprocessing/data/E003   --fold 0  -o model.pt --exp-id 123 --regression > train.log.regression 2>&1 &