# Desktop-Weather

Find the build guide here:
https://mustardcorner.com/desktop-weather


Code for the Desktop Weather build

```sudo apt-get install git```

```git clone https://github.com/yojoebosolo/Desktop-Weather.git```


Libraries needed:

Requests - ```apt-get install python3-pip -y```


Crontab setup needed:

```crontab -e```

add the following line to the bottom: 

``` @reboot sleep 100 && python3 /home/pi/Desktop-Weather/main.py ```

"Control + X"

"Y" _(yes)_

"Enter"
