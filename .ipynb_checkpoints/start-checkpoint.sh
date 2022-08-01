conda env create -f coffee.yml ipykernel
#source /opt/conda/etc/profile.d/conda.sh
eval "$(conda shell.bash hook)"
conda activate coffee
python -m ipykernel install --user --name coffee
mkdir data
cd data
wget --max-redirect=20 -O data.zip https://www.dropbox.com/sh/l3xu7bv91946hwt/AAAV_6oscivAbSpyTpRQKJq4a?dl=1
unzip data.zip
rm -r data.zip
