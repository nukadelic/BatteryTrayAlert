
Clone project to your apps folder

### Build 

Create and activate conda environment
```sh
conda create -n trayapp python=3.10 -y
conda activate trayapp
```

Install dependencies
```sh
pip install pystray pillow psutil pyinstaller
```

test run
```sh
python app.py
```

Create Portable executable ( icon can be --icon=NONE )
```sh
pyinstaller --onefile --windowed --icon=icon.ico --name=Battery app.py
```

Cleanup ( windows )
```sh
copy .\dist\Battery.exe .\Battery.exe && RD /S /Q build && RD /S /Q dist && del Battery.spec
```

### Autostart 
right click on `windows_autostart.ps1` and run with powershell - will auto create a windows startup link to the current directory


### Attribution (icon) : 
+ Battery icons created by Freepik - Flaticon : ( https://www.flaticon.com/free-icons/battery ) 
+ base64 png converter : https://www.base64-image.de/
+ convert PNG to ico : https://www.icoconverter.com/