import speedtest
import sys

def test_speed(unit):
    st = speedtest.Speedtest()
    
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

    print(f"\nResults:")
    print(f"Download Speed: {download_speed:.2f} {unit_label}")
    print(f"Upload Speed: {upload_speed:.2f} {unit_label}")
    print(f"Ping: {ping:.2f} ms")

def print_help():
    print("  -bits     Test internet speed in Mega Bits per Second (Mbps)")
    print("  -bytes    Test internet speed in Mega Bytes per Second (MBps)")
    print("  -h, -help Show this help message")

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
            print_help()

if __name__ == "__main__":
    main()
