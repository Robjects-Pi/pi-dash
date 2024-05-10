#!/bin/bash

# Update and upgrade the system
echo "Updating and upgrading the system..."
sudo apt-get update && sudo apt-get upgrade -y

# Install Python3 and pip if they are not installed
echo "Installing Python3 and pip..."
sudo apt-get install python3 python3-pip -y

# Install virtualenv for creating virtual environments
echo "Installing virtualenv..."
sudo pip3 install virtualenv

# Create a virtual environment for Picamera2
echo "Creating a virtual environment for Picamera2..."
virtualenv picamera2_env

# Activate the virtual environment
echo "Activating the virtual environment..."
source picamera2_env/bin/activate

# Install Picamera2 and its dependencies
echo "Installing Picamera2 and its dependencies..."
pip install picamera2

# Install additional dependencies if needed
echo "Installing additional dependencies..."
sudo apt-get install libatlas-base-dev libopenjp2-7 libtiff5 -y

# Deactivate the virtual environment
echo "Deactivating the virtual environment..."
deactivate

echo "Setup complete. You can now use Picamera2 by activating the virtual environment with 'source picamera2_env/bin/activate'."