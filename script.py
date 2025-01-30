import argparse
import re
import subprocess
import sys
import platform

def usage():
    print("Usage: script.py -i <interface> -a <new-mac-address>")
    sys.exit(1)

def verify_mac_address(mac):
    return bool(re.match(r"^[0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5}$", mac))

def run_command(command):
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.strip() if e.stderr else 'Command failed'}")
        sys.exit(1)

def change_mac_linux(interface, mac_address):
    print(f"Disabling network interface {interface}...")
    run_command(["sudo", "ifconfig", interface, "down"])
    
    print(f"Changing MAC address to {mac_address}...")
    run_command(["sudo", "ifconfig", interface, "hw", "ether", mac_address])
    
    print(f"Enabling network interface {interface}...")
    run_command(["sudo", "ifconfig", interface, "up"])

def change_mac_windows(interface, mac_address):
    print(f"Changing MAC address to {mac_address} on Windows...")
    
    reg_command = ["reg", "add", f"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4d36e972-e325-11ce-bfc1-08002be10318}}\\{interface}", "/v", "NetworkAddress", "/t", "REG_SZ", "/d", mac_address.replace(":", ""), "/f"]
    run_command(reg_command)
    
    print("Restarting network adapter...")
    run_command(["netsh", "interface", "set", "interface", interface, "admin=disable"])
    run_command(["netsh", "interface", "set", "interface", interface, "admin=enable"])
    
    print(f"MAC address changed successfully to {mac_address} for interface {interface}.")

def main():
    parser = argparse.ArgumentParser(description="Change MAC Address")
    parser.add_argument("-i", required=True, help="Network interface (e.g., eth0, Wi-Fi, Ethernet)")
    parser.add_argument("-a", required=True, help="New MAC address (format: XX:XX:XX:XX:XX:XX)")
    args = parser.parse_args()
    
    if not verify_mac_address(args.a):
        print("Error: Invalid MAC address format. Please use format like XX:XX:XX:XX:XX:XX.")
        usage()
    
    system_platform = platform.system()
    if system_platform == "Linux":
        change_mac_linux(args.i, args.a)
    elif system_platform == "Windows":
        change_mac_windows(args.i, args.a)
    else:
        print("Unsupported operating system.")
        sys.exit(1)

if __name__ == "__main__":
    main()
