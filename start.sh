#conda update -n base conda -y
conda install -c conda-forge nb_conda_kernels
conda env create -f env_opnc.yml ipykernel
conda activate env_opnc
python -m ipykernel install --user --name env_opnc
