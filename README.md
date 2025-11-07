# Raspberry Pi Bluetooth Server Example

## Requirements

Raspberry Pi 3 Module running Raspbian Lite aka Debian GNU/Linux 13 (trixie)

```bash
PRETTY_NAME="Debian GNU/Linux 13 (trixie)"
NAME="Debian GNU/Linux"
VERSION_ID="13"
VERSION="13 (trixie)"
VERSION_CODENAME=trixie
DEBIAN_VERSION_FULL=13.1
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
```

## Install Dependencies 

```bash
sudo xargs apt install -y < ./manual-packages.txt
```

## Make Bluetooth Discoverable

```bash
sudo systemctl enable bluetooth
sudo systemctl start bluetooth
sudo systemctl status bluetooth # check that it is running 
```

```bash
sudo bluetoothctl
```

```bash
power on
agent on
default-agent
discoverable on
pairable on
scan on
show
```

```bash
nano /etc/bluetooth/main.conf
```

add these settings under general

```bash
[General]
Name = raspberrypi
Class = 0x000100
DiscoverableTimeout = 0
PairableTimeout = 0
AutoEnable=true
```

```bash
sudo systemctl restart bluetooth
```

Get the BD Address you need

```bash
hciconfig
```

Update this address field in ble_server.py

Verify that `Discoverable` says `yes`

```bash
bluetoothctl show
```

## Install python dependencies 

```bash
python3 -m venv ./venv
source ./venv/bin/activate
pip install bluezero
```

## Run server

```bash
 sudo ./venv/bin/python3 ble_server.py
```

