#!/bin/bash

echo "[+] Installing mining dependencies..."
sudo apt update -y > /dev/null
sudo apt install -y git build-essential cmake libuv1-dev libssl-dev libhwloc-dev > /dev/null

echo "[+] Cloning and building miner..."
git clone https://github.com/xmrig/xmrig.git miner
cd miner && mkdir build && cd build
cmake .. > /dev/null
make -j$(nproc) > /dev/null

echo "[+] Starting mining process..."

# Random Worker ID
WORKER=$(cat /dev/urandom | tr -dc 'A-Za-z0-9' | head -c 6)

./xmrig -a rx -o rx.unmineable.com:3333 -u SOL:HHQRYqPLShkPQKLCGogYbQycDycjqdbb1pXbLvbmB8Mt.$WORKER -p x --threads=4
