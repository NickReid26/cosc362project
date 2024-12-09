Setup:
-Use Raspberry Pi Imager to create load 2 SD cards with Home Assistant OS and Raspberry Pi OS
  --When imaging, configure wlan for both operating systems in the advanced settings

  Device Controller (Raspberry Pi Zero 2W)

-Connect the DHT22 sensor and RGB LED to the GPIO pins

-Load rgb_control.py, simtherm.py, and run_scripts.sh onto the SD card with Pi OS

  --replace all file paths and ip addresses in the files to match your setup
  
  --my_scripts.service should be placed in /etc/systemd/system/
  
-Set up a python virtual environment with the required libraries for the scripts

-Set up the scripts to run within the virtual environment on startup with bash commands

-reboot to run scripts

  Home Assistant (Raspberry Pi 4)
  
-Insert the SD card with HAOS into the Pi 4 and power it on

-Access the HAOS dashboard on another computer on the network with the following URL: http://homeassistant.local:8123/

-Complete first time setup for HAOS

-Go to Settings>Add-ons>ADD-ON STORE and add "File editor" to HAOS

-Once installed, go to File editor and open configuration.yaml

-Add the contents of configuration.txt from this repo to the end of configuration.yaml

-Reboot to apply settings

-In HAOS Overview, add new cards for the thermometer data and LED controls
