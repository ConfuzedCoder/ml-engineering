# ml-engineering
Machine Learning Engineering


## Installation

```
pyenv versions
pyenv local 3.11.9
export POETRY_VIRTUALENVS_IN_PROJECT
poetry init 
poetry shell
poetry add ipykernel -G dev

# Install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

#Uninstall Rust
rustup self uninstall

# Install vllm
poetry add vllm

```