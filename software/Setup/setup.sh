# This script is used to set up the environment for the software

# Set up for the python environment
python3 -m venv environment
source environment/bin/activate

# Set up for the python packages
pip install --upgrade pip
pip install --upgrade setuptools

# Set up for the python packages
pip install -r requirements.txt

# The setup script will install the required dependencies and set up the software for the DIY Dashboard project. You can now start recording videos with the Raspberry Pi Zero.

# Make the setup script executable
chmod +x setup.sh

# Run the setup script
./setup.sh

