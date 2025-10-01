# VLLM_text Setup Guide

This is part of youtube video here: https://www.youtube.com/watch?v=tO3WOE9sZV0
and part of playlist: https://www.youtube.com/playlist?list=PLKQlkwtnLtvIoovO4LNXYpzLwG0rGPIK_

## Requirements

- NVIDIA driver supporting CUDA 12.8 (`nvidia-smi` should show CUDA 12.8 or higher)
- Used in the video  Driver Version: 575.64.03 and 580.82.09 CUDA Version: 12.9 (in nvidia-smi)
- Docker installed https://docs.docker.com/engine/install/ubuntu/ I used Docker version 28.3.3, build 980b856
- NVIDIA Container Toolkit https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html
- I use Linux  6.14.0-29-generic #29~24.04.1-Ubuntu x86_64 x86_64 x86_64 GNU/Linux
## Installation for Test Script

### 1. Update your system and install Python venv

```bash
sudo apt update
sudo apt install python3.12-venv
```

### 2. Create and activate a virtual environment

#### Fish shell

```fish
python3 -m venv .venv
source .venv/bin/activate.fish
pip install --upgrade pip
pip install openai
```

#### Bash shell

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install openai
```

# Further reading
- Docker parameters for VLLM Image https://docs.vllm.ai/en/latest/configuration/engine_args.html#modelconfig 
- VLLM project https://docs.vllm.ai/en/latest/ 

# Dictionary
- KV Cache 
    - In old autoregressive language models, when generating text token by token, the model needs to compute attention over all previous tokens. The KV cache stores these intermediate computations so they don’t need to be recalculated for each new token, dramatically speeding up inference (https://cloudthrill.ca/kv_cache-explained).
    - It's like if we write multiple words but each time we forget what was written so we need to read it again to write next word. KV cache remember it and then we just add one word we don't need to read everything before by adding tokens (https://www.youtube.com/watch?v=80bIUggRJf4)
