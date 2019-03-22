# spiderbot
just a spider bot 
## Component list
* 1 * Raspberry Pi 2B/B+/2B+/3B/3B+/zero/Zero w/3A+
* 2 * PCA9685A servo drive board
* 1 * 7.4v-5V DCDC 
* 18 * LDX-218 Robot Servo (digital Servo)
* 1 * Acrylic skelton of the spider (Design by yourself)
* 1 * 7.4v lipo battery 
## How to buid it
* 1. Download the latest Raspbian image from official site and burn you SD card.
* 2. Connect PCA9685A drive board to Raspberry pi via I2C connection pins( 5v,GND,SDA,SCL)
* 3. Connect PCA9685A drive board to another PCA9685A drive board via extended pins 
* 4. Connect PCA9685A drive board's VSS & GND to battery.
* 5. Connect DCDC module to the battery, and it will supply power to raspberry pi
----
## How to install the driver from github
`sudo apt-get update `
`sudo apt-get upgrade `
`sudo apt-get -y install git `
`cd ~`
`git clone https://github.com/yoyojacky/spiderbot.git`
`cd spiderbot/`
`sudo python robot.py `
