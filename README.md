## Install

### Install PyTorch


>pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

Or any other PyTorch version that is compatible with your computer's specifications.

This repository uses https://github.com/openai/whisper, and its readme mentions "We used Python 3.9.9 and PyTorch 1.10.1 to train and test our models, but the codebase is expected to be compatible with Python 3.8-3.11 and recent PyTorch versions." 

[`whisper`](https://github.com/openai/whisper) also requires the command-line tool [`ffmpeg`](https://ffmpeg.org/) to be installed on your system, which is available from most package managers:

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

### Install other requirements

>pip install -r requirements.txt
