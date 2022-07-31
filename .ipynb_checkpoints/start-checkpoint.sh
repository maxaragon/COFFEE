conda env create -f coffee.yml ipykernel
#source /opt/conda/etc/profile.d/conda.sh
eval "$(conda shell.bash hook)"
conda activate coffee.yml
python -m ipykernel install --user --name coffee.yml
