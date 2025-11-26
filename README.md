A system tray application to popup alert message when the battery charger has been disconnected. 

## Installation

Start by clonning the project to your apps folder 
download the executable file from here : https://github.com/nukadelic/BatteryTrayAlert/releases 
place in the same directory as the powershell (ps1) script

## Autostart app on system startup  
right click on `windows_autostart.ps1` and run with powershell - will auto create a windows startup link to the current directory

## Manually Build the app (2 min process)

Create and activate conda environment
```sh
conda create -n trayapp python=3.10 -y
conda activate trayapp
```

Install dependencies
```sh
pip install pystray pillow psutil pyinstaller
```

test run ( optional ) 
```sh
python app.py
```

Create Portable executable (icon can be NONE)
```sh
pyinstaller --onefile --windowed --icon=icon.ico --name=Battery app.py
```

Cleanup ( windows )
```sh
copy .\dist\Battery.exe .\Battery.exe && RD /S /Q build && RD /S /Q dist && del Battery.spec
```


**Attribution and tools:**
+ Battery icons created by Freepik - Flaticon : ( https://www.flaticon.com/free-icons/battery ) 
+ base64 png converter : https://www.base64-image.de/
+ convert PNG to ico : https://www.icoconverter.com/
