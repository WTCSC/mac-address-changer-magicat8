# MAC Address Changer Script

This script allows you to change the MAC address of a specified network interface on your system. It is a lightweight and simple tool designed for users who need to quickly modify their MAC address.

## Installation and Dependencies

### Prerequisites
1. Ensure you have `bash` installed on your system.
2. You need root or sudo privileges to run this script as it modifies network interface settings.
3. The `ifconfig` command must be available on your system. Install `net-tools` if it is not already installed:
   ```bash
   sudo apt-get install net-tools  # For Debian/Ubuntu
   sudo yum install net-tools      # For CentOS/RHEL
   ```

### Installation
1. Download the script and save it locally:
   ```bash
   wget https://example.com/mac_changer.sh -O mac_changer.sh
   ```
2. Make the script executable:
   ```bash
   chmod +x mac_changer.sh
   ```

## Usage Examples

### Basic Usage
Run the script with the required options:
```bash
./mac_changer.sh -i <interface> -a <new-mac-address>
```

#### Example
To change the MAC address of interface `eth0` to `AA:BB:CC:DD:EE:FF`:
```bash
sudo ./mac_changer.sh -i eth0 -a AA:BB:CC:DD:EE:FF
```

### Command-Line Arguments
- `-i`: Specifies the network interface (e.g., `eth0`, `wlan0`).
- `-a`: Specifies the new MAC address in the format `XX:XX:XX:XX:XX:XX`.

### Displaying Help
For usage instructions, run:
```bash
./mac_changer.sh
```

## Error Handling and Validation
The script includes robust error handling for common issues:
1. **Invalid MAC Address Format:**
   If the MAC address does not match the expected format, an error is displayed:
   ```
   Error: Invalid MAC address format. Please use format like XX:XX:XX:XX:XX:XX.
   ```
2. **Missing Arguments:**
   If required arguments are missing, the script provides a usage message and exits.
3. **Interface Errors:**
   If disabling, changing, or enabling the network interface fails, the script displays an error message and exits.

## Common Troubleshooting Tips

### "Permission Denied" Error
Ensure you run the script with `sudo`:
```bash
sudo ./mac_changer.sh -i eth0 -a AA:BB:CC:DD:EE:FF
```

### "Command Not Found: ifconfig"
Install `net-tools` using your system's package manager:
```bash
sudo apt-get install net-tools
```

### "Failed to disable/enable network interface"
Check if the specified network interface exists and is spelled correctly. Verify by listing available interfaces:
```bash
ifconfig -a
```

## Script in Action
#### Successful MAC Address Change:
```text
$ sudo ./mac_changer.sh -i eth0 -a AA:BB:CC:DD:EE:FF
Disabling network interface eth0...
Changing MAC address to AA:BB:CC:DD:EE:FF...
Enabling network interface eth0...
MAC address changed successfully to AA:BB:CC:DD:EE:FF for interface eth0.
```
#### Error Example:
```text
$ ./mac_changer.sh -i eth0 -a INVALID_MAC
Error: Invalid MAC address format. Please use format like XX:XX:XX:XX:XX:XX.
Usage: ./mac_changer.sh [-i <eth0|eth1|...>] [-a <new-mac-address>]
```
