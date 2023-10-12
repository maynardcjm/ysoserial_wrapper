# ysoserial_wrapper
a wrapper which generates multiple payloads for different formatters and gadgets ysoserial has to offer

## Setup
Note: it's recommended to do this within a windows container. Window dev boxes can be installed from: https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/

1. Deactivate Windows Defender's Threat Protection
   - Click the windows key and type in "Virus & Threat Protection"
   - Under Virus & threat protection settings click "Manage Settings"
   - Uncheck Real-time protection (this will disable windows defender for a limited time)

2. Download and Install the ysoserial.exe from https://github.com/pwntester/ysoserial.net/releases

## Usage
python payload_generator.py [cmd] [exe-path]
python payload_generator.py "curl http://localhost:8000" "C:\\\\Users\\User\\\\ysoserial.net\\\\ysoserial\\\\bin\\\\Debug\\\\ysoserial.exe"
