# Define the name of the Conda environment
$conda_env_name = "Neurips_2024"
Write-Output "The Conda environment name is: $conda_env_name"

conda update -n base conda -y
conda update --all -y
python -m pip install --upgrade pip

conda create -n $conda_env_name python=3.11.4 -y
conda activate $conda_env_name
pip install -r requirements.txt