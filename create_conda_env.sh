# Check if the dirpi-web environment exists
ENV_EXISTS=$(conda info --envs | grep dirpi-web)

# If the environment exists
if [[ -n "$ENV_EXISTS" ]]; then
    echo "Environment dirpi-web already exists."
else
    # Create the environment and install pip
    # conda create -n dirpi-web
    # conda install -n dirpi-web pip

    # create dirpi-web environment with no confirmation
    conda create -n dirpi-web --yes pip
fi

# Activate the environment
conda activate dirpi-web

# Install or check required packages
pip install -r requirements.txt
