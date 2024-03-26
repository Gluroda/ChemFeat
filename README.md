# ChemFeat

## Purpose
ChemFeat gives an easy python interface for the creation of different descriptor sets or other representative sets for molecules. It is packaged in a container to overcome potential dependency issues.

## Instructions
After cloning the repository you need to build the image. `<>` mark variable names that can follow your preferred naming conventions.
- `podman build -t <chemfeat> .`

Having the image, you can start your container and run an interactive python session:
- `podman run -it <chemfeat>`
Or you can pass a script to the command and have it executed:
- `podman run <chemfeat> python your_script.py`
