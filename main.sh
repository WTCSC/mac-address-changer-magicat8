#!/bin/bash

usage() { echo "Usage: $0 [-i <eth0|eth1|...>] [-a <new-mac-address>]" 1>&2; exit 1; }

verify_mac_address() {
    echo "${1}" | grep -E "^[0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5}$" >/dev/null 2>&1
}

while getopts ":i:a:" opt; do
    case "${opt}" in
        i)
            i=${OPTARG}
            ;;
        a)
            a=${OPTARG}
            if ! verify_mac_address "${a}"; then
                echo "Error: Invalid MAC address format. Please use format like XX:XX:XX:XX:XX:XX."
                usage
            fi
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND - 1))

# Check if arguments are given
if [ -z "${i}" ] || [ -z "${a}" ]; then
    usage
fi

echo "Disabling network interface ${i}..."
sudo ifconfig "${i}" down
if [ $? -ne 0 ]; then
    echo "Error: Failed to disable network interface ${i}."
    exit 1
fi

echo "Changing MAC address to ${a}..."
sudo ifconfig "${i}" hw ether "${a}"
if [ $? -ne 0 ]; then
    echo "Error: Failed to change MAC address."
    exit 1
fi

echo "Enabling network interface ${i}..."
sudo ifconfig "${i}" up
if [ $? -ne 0 ]; then
    echo "Error: Failed to enable network interface ${i}."
    exit 1
fi

echo "MAC address changed successfully to ${a} for interface ${i}."
exit 0