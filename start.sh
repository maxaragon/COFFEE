conda env create -f env_opnc.yml ipykernel
#source /opt/conda/etc/profile.d/conda.sh
eval "$(conda shell.bash hook)"
conda activate env_opnc
python -m ipykernel install --user --name env_opnc
