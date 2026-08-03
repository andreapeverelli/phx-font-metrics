# phx-font-metrics
Extract metrics from a TTF font file for generating a custom Material You typescale.

## Install from Source
```bash
git clone https://github.com/andreapeverelli/phx-font-metrics.git
makepkg -si
```

## Install from Repository
```bash
# Add Repository to Pacman
sudo printf '[phx]\nServer = https://andreapeverelli.github.io/phx-repo/\n' | sudo tee -a /etc/pacman.conf > /dev/null
wget -O /tmp/phx-repo-key.asc https://andreapeverelli.github.io/phx-repo/key.asc
sudo pacman-key --add /tmp/phx-repo-key.asc
sudo pacman-key --lsign-key CAF1FE155FED7B2F6E05EC6BD88ABED0A94852EC

# Update Repositories and install phx-tools
sudo pacman -Syy phx-font-metrics
```

## Usage
The main purpose is to be used from PHX-TOOLS generate:typescale but it can also be run independently with this command:
```bash
phx-font-metrics ttf_font_file [weight_axis_name] [weight_axis_value]
```
