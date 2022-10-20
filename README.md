# Desktop-Weather

Find the build guide here:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://mustardcorner.com/desktop-weather


Code for the Desktop Weather build:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```sudo apt-get install git```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```git clone https://github.com/yojoebosolo/Desktop-Weather.git```


Libraries needed:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Requests - ```pip install requests```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; IF using RaspiOS Lite, you will need to install pip.


Crontab setup needed:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```crontab -e```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; add the following line to the bottom: 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ``` @reboot sleep 100 && python3 /home/pi/Desktop-Weather/main.py ```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "Control + X"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "Y" _(yes)_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "Enter"

For Arduino/ESP32 versions, go here:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; https://github.com/MaeseppTarvo/DesktopWeather
