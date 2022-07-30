#conda update -n base conda -y
conda install -c conda-forge nb_conda_kernels
#conda create --name env-wekeo ipykernel -y 
conda env create -f env_opnc.yml ipykernel -y
conda activate env-wekeo 
python -m ipykernel install --user --name env-wekeo

#conda init