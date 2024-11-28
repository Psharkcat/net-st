import speedtest
import sys

def test_speed(unit):
    st = speedtest.Speedtest()
    st.get_best_server()
    print("Testing download speed...")
    download_speed = st.download()

    print("Testing upload speed...")
    upload_speed = st.upload()

    print("Testing ping...")
    ping = st.results.ping

    if unit == "bytes":
        download_speed /= 8  # Convert bits to bytes
        upload_speed /= 8
        unit_label = "MBps"
    else:
        unit_label = "Mbps"

    download_speed /= 1_000_000  # Convert to Mbps or MBps
    upload_speed /= 1_000_000

    # Function to get color based on speed
    def get_color(speed):
        if speed < 5:
            return "\033[91m"  # Red
        elif 5 <= speed < 20:
            return "\033[92m"  # Green
        elif 20 <= speed < 50:
            return "\033[94m"  # Blue
        else:
            return "\033[93m"  # Gold

    # Get colors for download and upload speeds
    download_color = get_color(download_speed)
    upload_color = get_color(upload_speed)

    # Reset color
    reset_color = "\033[0m"

    print(f"\nResults:")
    print(f"Download Speed: {download_color}{download_speed:.2f} {unit_label}{reset_color}")
    print(f"Upload Speed: {upload_color}{upload_speed:.2f} {unit_label}{reset_color}")
    print(f"Ping: {ping:.2f} ms")

def print_help():
    print("  -bits     Test internet speed in Mega Bits per Second (Mbps)")
    print("  -bytes    Test internet speed in Mega Bytes per Second (MBps)")
    print("  -h, -help Show this help message")
    print("Developed by Psharkcat in github.")

def main():
    if len(sys.argv) < 2:
        test_speed("bytes")
    else:
        arg = sys.argv[1].lower()
        if arg == "-bytes":
            test_speed("bytes")
        elif arg == "-bits":
            test_speed("bits")
        elif arg in ("-h", "-help"):
            print_help()
        else:
            print("Invalid argument. Use '-h' or '--help' for more information.")

if __name__ == "__main__":
    main()
