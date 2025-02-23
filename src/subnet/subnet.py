#!/usr/bin/env python3

import ipaddress
import argparse

def calculate_subnet(ip, subnet):
    try:
        network = ipaddress.ip_network(f"{ip}/{subnet}", strict=False)
    except ValueError as e:
        print(f"Error: {e}")
        return
    print("Network:", network)
    print("Network Address:", network.network_address)
    print("Broadcast Address:", network.broadcast_address)
    print("Number of Hosts:", network.num_addresses - 2)  # Excludes network & broadcast addresses

def main():
    parser = argparse.ArgumentParser(description="Subnetting Calculator CLI")
    parser.add_argument("ip", help="IP address, e.g., 192.168.1.0")
    parser.add_argument("subnet", help="Subnet mask in CIDR notation, e.g., 24", type=int)
    args = parser.parse_args()

    calculate_subnet(args.ip, args.subnet)

if __name__ == "__main__":
    main()
