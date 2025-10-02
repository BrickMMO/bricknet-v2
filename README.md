# BrickNet

BrickNet is a Python library to simplify BlueTooth communication between a [Dexter BrickPi](https://www.dexterindustries.com/brickpi/), [LEGO&reg; Spike](https://www.lego.com/en-ca/product/lego-education-spike-prime-set-45678), and [LEGO&reg; EV3&trade;](https://www.lego.com/en-ca/product/lego-mindstorms-ev3-31313). 

## Turn on Bluetooth

Run these commands:

```
sudo rfkill unblock bluetooth
sudo hciconfig hci0 up
```

## Install Raspberry Pi OS

The BrickPi version we has uses Raspberry Pi 3 Model B Rev 1.2. 

1. Download Raspberry [Pi Imageer](https://www.raspberrypi.com/software/).
2. Install **Raspberry Pi OS 32-bit**. Use thesse settings:

    - Raspbery Pi Device: Raspberry Pi 3
    - Operating System: Raspberry Pi OS (32-Bit)
    - Storage: Your SD Card
  
3. Click **Next** and then **Edit Settings**.
4. Use thes options:

    - Set Hostname: alpha, brave, charlie, etc...
    - Set Username: robot
    - Set Password: maker
    - Wireless SSID: ROBOTS2
    - Wireless Password: 99999999
    - Zime Zone: America/Toronto
    - KeyboardL US

5. Click **Start**.

## Connect to Your Pi

Insert your SD card into your Pi and open up the Terminal:

1. Run `ssh robot@alpha.local`.
2. Login using the password `maker`.

> ![NOTE]  
> You may need to reset the connection using this command:
> `ssh-keygen -R alpha.local`

## Test Python Code

Open up Visual Studio Code and your project files and then connect to your Pi and test your code:

1. Push **Ctrl**, **Shift**, **p**.
2. Type **ssh** and choose **Remote-SSH: Connect Current Window to Host...**

---

## Project Stack

This project uses [Python](https://www.python.org/) and [PyBricks](https://pybricks.com/).

<img src="https://console.codeadam.ca/api/image/python" width="60"> <img src="https://console.codeadam.ca/api/image/pybricks" width="60"> 

---

## Repo Resources

- [BrickMMO](https://www.brickmmo.com/)
- [PyBicks](https://pybricks.com/)

<a href="https://brickmmo.com">
<img src="https://cdn.brickmmo.com/images@1.0.0/brickmmo-logo-coloured-horizontal.png" width="300">
</a>
