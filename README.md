# Desktop-Weather
Code for the Desktop Weather build

  ```sudo apt-get install git```

  ```git clone https://github.com/yojoebosolo/Desktop-Weather.git```


Libraries needed:

  Requests - ```pip install requests```


Crontab setup needed:

  ```crontab -e```

add the following line to the bottom: 

  ``` @reboot sleep 100 && python3 /home/pi/Desktop-Weather/main.py ```

  "Control + X"

  "Y" _(yes)_

  "Enter"
