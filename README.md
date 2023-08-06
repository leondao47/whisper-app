## Installation

Requirements:

- `python3` (version higher or equal to 3.7, at least 3.9 is recommended)
- `ffmpeg` (see instructions for installation on the [whisper repository](https://github.com/openai/whisper)

### Install `ffmpeg`:

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

### Installation steps:

```bash
# clone the project
git clone https://github.com/leondao47/whisper-app.git

# create and active virtual environment
cd whisper-app
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip3 install git+https://github.com/linto-ai/whisper-timestamped
pip install flask flask_cors

# run application
cd be
python app.py

```

Now App is running on http://127.0.0.1:5000
