FROM mcr.microsoft.com/devcontainers/python:3.13

# Install libgl1 for rendering
RUN apt-get update && \
    apt-get install -y libgl1
    
# Install build123d dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install \
    jupyter \
    ocp_vscode \
    cadquery \
    build123d
