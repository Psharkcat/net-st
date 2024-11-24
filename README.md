
---

# net-st

This is a simple Python script that measures your internet connection's download speed, upload speed, and ping.

## Features
- Test download and upload speeds in **Mega Bits per Second (Mbps)** or **Mega Bytes per Second (MBps)**.
- Display ping latency.
- Simple command-line interface with clear output.
- Option to view a help message for usage instructions.

## Requirements

- Python 3.x
- `speedtest-cli` library

### Install the required dependencies:

#### For Arch Linux (and derivatives):

If you're on an Arch-based system, you can install `speedtest-cli` directly from the official repositories with `pacman`:

```bash
sudo pacman -S speedtest-cli
```

#### For other systems:

You can install `speedtest-cli` via `pip`:

```bash
pip install speedtest-cli
```

## Clone the Repository

You can clone this repository to your local machine using `git`:

```bash
git clone https://github.com/Psharkcat/net-st.git
```

After cloning, navigate into the project directory:

```bash
cd net-st
```

## Usage

### Running the Script

To use the script, run it via the command line with one of the following options:

1. **Test speed in Mega Bits per Second (Mbps)**:
   ```bash
   python net-st.py -bits
   ```

2. **Test speed in Mega Bytes per Second (MBps)** (default if no argument is passed):
   ```bash
   python net-st.py -bytes
   ```

3. **View help message**:
   ```bash
   python net-st.py -h
   ```

## How it Works

1. The script uses the **Speedtest-cli** library to measure internet speed by connecting to nearby Speedtest servers.
2. The script will automatically select the best server based on your location.
3. It will measure the download speed, upload speed, and ping latency.
4. You can choose to display the results in either Mega Bits per Second (Mbps) or Mega Bytes per Second (MBps).

## License

This project is licensed under the **GNU General Public License** (GPL). See the [LICENSE](LICENSE) file for details.

---
