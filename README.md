# Desktop-Weather
Code for the Desktop Weather build


Libraries needed:

Requests - ```pip install requests```


Crontab setup needed:

```crontab -e```

add the following line to the bottom: 

``` @reboot sleep 100 && python3 /home/pi/Desktop-Weather/main.py ```

Control + X

Y (yes)

Enter
