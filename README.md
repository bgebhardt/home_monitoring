# Home Monitoring

This is my home monitoring setup repo.

A few goals.

- Monitor Powerwall battery charging
    - Alert at certain levels
- Monitor my indoor thermostat temperature over time and compare to weather forecast
    - Optimize when to turn on the AC when there is enough solar generation to offset its use
    - Pre-cool the house

The first thing is to decide which home automation software to run. Two I'm considering.

- Homeassistant
- Homekit with Homebridge

# [Home Assistant](https://www.home-assistant.io/)

You run this as a server and it can run without a hub like Homekit requires. Has great out of the box functionality and a ton of integrations. There's an iOS app which I haven't set up yet.

## Install

Good background: [Which Installation Method is Best for Home Assistant? – Siytek](https://siytek.com/which-installation-method-is-best-for-home-assistant/)

*This was the best tutorial I found to install.*
To install as a VM on a mac (hard) - [How To Install Home Assistant Supervised on Mac OS – Siytek](https://siytek.com/home-assistant-supervised-on-mac-os/)
Note there may be updates here: [home-assistant/supervised-installer: Installer for a generic Linux system](https://github.com/home-assistant/supervised-installer)
It uses [UTM | Virtual machines for Mac](https://mac.getutm.app/) which is very cool. UTM has lots of Mac friendly features. Even AppleScript [Scripting | UTM Documentation](https://docs.getutm.app/scripting/scripting/)!

*Other options reviewed*
To install natively on a mac (easy, but didn't work and no addons) - [How To Install Home Assistant On Mac OS – Siytek](https://siytek.com/install-home-assistant-on-mac/) - But you miss the Home Assistant Supervisor and its features
Official install docs which require understanding VM's (hard) - [MacOS - Home Assistant](https://www.home-assistant.io/installation/macos)

## Configure

[Getting started with the home assistant app for MAC os | JuanMTech](https://www.juanmtech.com/getting-started-with-the-home-assistant-app-for-macos/)
[(838) HOW TO Connect Home Assistant to Apple Homekit - YouTube](https://www.youtube.com/watch?v=3tutxHO0J78)

Devices to configure
- Tesla Powerwall
- Honeywell Thermostat
- Samsung TV
- Vizio TV

Top Add Ons to install
- File editor
- Log Viewer
- Grafana - [addon-grafana/grafana/DOCS.md at main · hassio-addons/addon-grafana](https://github.com/hassio-addons/addon-grafana/blob/main/grafana/DOCS.md)
- InfluxDB
- JupyterLab
- Glances

Integrations to consider
- [AirNow - Home Assistant](https://www.home-assistant.io/integrations/airnow/)
    - [AirNow API Documentation](https://docs.airnowapi.org/aq101)
- [National Weather Service (NWS) - Home Assistant](https://www.home-assistant.io/integrations/nws)
- [AccuWeather - Home Assistant](https://www.home-assistant.io/integrations/accuweather/)
    - [Home Assistant How To - get most out of AccuWeather integration - YouTube](https://www.youtube.com/watch?v=DXehQBgdsHk)
- Google Drive
- Local Calendar
- [International Space Station (ISS) - Home Assistant](https://www.home-assistant.io/integrations/iss)

- [sabeechen/hassio-google-drive-backup: Automatically create and sync Home Assistant backups into Google Drive](https://github.com/sabeechen/hassio-google-drive-backup)

- Package tracking - [How To Install Mail and Packages Integration Home Assistant - Smart Home Pursuits](https://smarthomepursuits.com/how-to-install-mail-and-packages-integration-home-assistant/?expand_article=1)

[The Best Home Assistant Addons And Repos Of 2023 - Gadget-Freakz.com](https://gadget-freakz.com/the-best-home-assistant-addons-and-repos-of-2023/)

## Companion App

- Get the companion app installed and connected
- Move instance to run on mac mini

## Automation approaches

Tutorial:
[Easy home Assistant Notifications using Alerts! - YouTube](https://www.youtube.com/watch?v=uQwIusogTZE&t=9s)
[I was wrong about Home Assistant Automations - YouTube](https://www.youtube.com/watch?v=7xfHiD4AuXM)
[5 Home Assistant Built-In Integrations You Probably Should be Using - YouTube](https://www.youtube.com/watch?v=QZB_o62AuV0)
[Easy Notifications with Alerts — Slacker Labs](https://www.slacker-labs.com/blog/2022/04/13/home-assistant-alerts)
[HOW TO Connect Home Assistant to Apple Homekit - YouTube](https://www.youtube.com/watch?v=3tutxHO0J78)
[Getting started with the home assistant app for MAC os | JuanMTech](https://www.juanmtech.com/getting-started-with-the-home-assistant-app-for-macos/)

Notification options

- [SendGrid - Home Assistant](https://www.home-assistant.io/integrations/sendgrid) - free 100 mails/day
- in browser - [HTML5 Push Notifications - Home Assistant](https://www.home-assistant.io/integrations/html5)
- Email SMTP server - [Can Home Assistant Send Email? – Siytek](https://siytek.com/can-home-assistant-send-email/#:~:text=Can%20Home%20Assistant%20Send%20Email%3F%201%20Setting%20up,service%20to%20Home%20Assistant.%20...%203%20Conclusion%20)
- [ClickSend SMS - Home Assistant](https://www.home-assistant.io/integrations/clicksend/)

## References

- Great tutorials are here: [Home Assistant – Siytek](https://siytek.com/category/smart-home-tek/home-assistant/)
- [Home Assistant Beginner’s Guide: Setting up Home Assistant](https://home-assistant-guide.com/guide/the-home-assistant-beginners-guide-part-1-setting-up-hass-io/#:~:text=The%20Home%20Assistant%20Supervisor%20allows%20you%2C%20the%20user%2C,Make%20and%20restore%20backups%20Add-ons%20Unified%20audio%20system) - Explains different Home Assistant parts
- [Home Assistant COMPLETE Beginners Guide 2023 - YouTube](https://www.youtube.com/watch?v=LI3lhgOiZ-8)

# Homekit and Homebridge

[Homebridge](https://homebridge.io/) is a services with integrations written to allow devices not supported by Homekit are supported.

## Install & Configure

Good docs here:

- [Install Homebridge on macOS · homebridge/homebridge Wiki](https://github.com/homebridge/homebridge/wiki/Install-Homebridge-on-macOS)
- [homebridge/homebridge-config-ui-x: The Homebridge UI. Monitor, configure and backup Homebridge from a browser.](https://github.com/homebridge/homebridge-config-ui-x)

## Plugin install and set up

### Thermostat 
- [homebridge-resideo - npm](https://www.npmjs.com/package/homebridge-resideo) - for some reason this doesn't include the thermostat on the web but does in the app.
- Total Comfort Control (TCC)
    - [homebridge-tcc - npm](https://www.npmjs.com/package/homebridge-tcc) - this one seems to work.
    - [honey-tcc - npm](https://www.npmjs.com/package/honey-tcc)

### Tesla Powerwall 

Follow installation and configuration instructions in [homebridge-tesla-powerwall - npm](https://www.npmjs.com/package/homebridge-tesla-powerwall)
This plugin can support the Eve app (supports HomeKit and Matter protocols)

Code is based on [vloschiavo/powerwall2: Tesla Powerwall 2 - Local Gateway API documentation](https://github.com/vloschiavo/powerwall2)

### Eve app from Elgato

Install on iPad (M1 Macs) and iPhone
https://www.bing.com/ck/a?!&&p=d3a0f2d99efa2ed3JmltdHM9MTY4OTM3OTIwMCZpZ3VpZD0wZjhhZGY2My02ZjFhLTYzZDgtMDVmYS1jYzU5NmU5ZTYyMzQmaW5zaWQ9NTE5Nw&ptn=3&hsh=3&fclid=0f8adf63-6f1a-63d8-05fa-cc596e9e6234&psq=elgato+eve+app&u=a1aHR0cHM6Ly9hcHBzLmFwcGxlLmNvbS91cy9hcHAvZXZlLWZvci1tYXR0ZXItaG9tZWtpdC9pZDkxNzY5NTc5Mg&ntb=1

# Powerwall scripts and monitoring

see notes in obsidian://open?vault=Personal&file=Coding%20%26%20Hack%20Projects%2FTesla%20Solar%20Powerwall%20Monitoring

## Logging into your Gateway via web

You can use the app, but you can also login via the web

1. Get the ip address of your gateway
2. In a browser go to that ip
3. Select customer login
4. Enter the email you used in the Tesla app
5. Password - can find on the sticker inside your invertor. It's the last 5 characters of that password.

These are the same credentials PyPowerwall uses.

Reference Links
- [Connecting to Tesla Gateway and Powerwall+ | Tesla Support](https://www.tesla.com/support/energy/powerwall/own/connecting-network)
- [How to connect to Tesla Energy Gateway](https://solareenergy.com/solar-articles/tesla-energy-gateway/#:~:text=Select%20%E2%80%9CCustomer%E2%80%9D%20for%20login%20type%20and%20enter%20the,enter%20the%20password%20for%20your%20home%20WiFi%20network.)

## PyPowerwall install

```
# Install pyPowerwall
python -m pip install pypowerwall

# Scan Network for Powerwalls
python -m pypowerwall scan
```

## Using pypowerwall

- [GitHub - jasonacox/pypowerwall: Python API for Tesla Powerwall and Solar Power Data](https://github.com/jasonacox/pypowerwall)

Ultimately I want to set up this solution. Very cool.
[jasonacox/Powerwall-Dashboard: Grafana Dashboard for Tesla Powerwall](https://github.com/jasonacox/Powerwall-Dashboard)

Example output from my simple script

```bash
./pypowerwall_check.py
Site Name: My Home - Firmware: 23.12.1 7ca1b02c - DIN: <redacted>
System Uptime: 119h18m30.79789591s

Battery power level: 67%
Combined power metrics: {'site': -202, 'solar': 8739.7001953125, 'battery': -3680, 'load': 4960.1650390625}

Grid Power: -0.20kW
Solar Power: 8.74kW
Battery Power: -3.68kW
Home Power: 4.96kW
```

Create a file powerwallconfig.py with your credentials in it for pypowerwall_check.py to work.

```python
# Credentials for your Powerwall - Customer Login Data
password =''
email =''
host = "" # Address of your Powerwall Gateway
timezone = "" # Your local timezone
```

# Monitoring Thermostat

see obsidian://open?vault=Personal&file=Household%20and%20Home%2FMonitoring%20Thermostat%20and%20Smart%20Home

## Resideo / Honeywell

[Honeywell Home Developer Site | home](https://developer.honeywellhome.com/)
[Honeywell Home Developer Site | Obtain OAuth2 Client Credentials Token](https://developer.honeywellhome.com/authorization-oauth2/apis/post/accesstoken)

[donavanbecker/homebridge-resideo: The Homebridge Resideo plugin allows you to access your Resideo thermostat from HomeKit.](https://github.com/donavanbecker/homebridge-resideo)

### Total Connect Comfort link
Older API is Total Connect Comfort. Seems to be replaced by Resideo.
[Honeywell Home - My Total Connect Comfort](https://mytotalconnectcomfort.com/portal/)
[Total Connect Comfort Web API Help Page](https://www.mytotalconnectcomfort.com/WebApi/Help/LogIn?ReturnUrl=%2FWebApi%2FHelp)
[HoneywellThermo-TCC/HoneywellThermo-TCC_C.groovy at master · HubitatCommunity/HoneywellThermo-TCC](https://github.com/HubitatCommunity/HoneywellThermo-TCC/blob/master/HoneywellThermo-TCC_C.groovy)


## Smartthings approach

This doesn't get realtime Thermostat updates so going to research using the Resideo/Honeywell API directly.

My thermostat can be registered with Samsung Smartthings

Trying Smartthings CLI to pull indoor temperature reading.
[SmartThingsCommunity/smartthings-cli: Command-line Interface for the SmartThings APIs.](https://github.com/SmartThingsCommunity/smartthings-cli)
docs: [Get Started With the SmartThings CLI | SmartThings Developers](https://developer.smartthings.com/docs/sdks/cli/introduction/)
configuration docs: [smartthings-cli/packages/cli/doc/configuration.md at main · SmartThingsCommunity/smartthings-cli](https://github.com/SmartThingsCommunity/smartthings-cli/blob/main/packages/cli/doc/configuration.md)
api docs: [API | SmartThings Developers](https://developer.smartthings.com/docs/api/public/)

### Smartthings CLI Install

To install

```bash
brew install smartthingscommunity/smartthings/smartthings
```

### Example usage

After login here's an example of useful commands.

A personal access token is not needed as CLI logs in when you first run a command. But for reference you can create a personal access token at [SmartThings. New Access Token.](https://account.smartthings.com/tokens/new)

```bash
smartthings devices
────────────────────────────────────────────────────────────────────────────────────
 #  Label       Name                    Type   Device Id
────────────────────────────────────────────────────────────────────────────────────
 1  Samsung TV  Samsung TV              OCF    blah blah
 2  THERMOSTAT  TCC Thermostat H-C-Hum  VIPER  blah blah2
────────────────────────────────────────────────────────────────────────────────────`
```

```bash
smartthings devices:history
────────────────────────────────────────────────────────────────────────────────────
 #  Label       Name                    Type   Device Id
────────────────────────────────────────────────────────────────────────────────────
 1  Samsung TV  Samsung TV              OCF    
 2  THERMOSTAT  TCC Thermostat H-C-Hum  VIPER  
────────────────────────────────────────────────────────────────────────────────────
? Select a device. 2
──────────────────────────────────────────────────────────────────────────────────────
 Time                    Component  Capability                   Attribute    Value
──────────────────────────────────────────────────────────────────────────────────────
 7/15/2023, 9:38:02 AM   main       relativeHumidityMeasurement  humidity     "58" %
 7/15/2023, 9:20:08 AM   main       relativeHumidityMeasurement  humidity     "57" %
 7/15/2023, 9:18:08 AM   main       relativeHumidityMeasurement  humidity     "58" %
 7/15/2023, 9:15:04 AM   main       relativeHumidityMeasurement  humidity     "57" %
 7/15/2023, 9:11:33 AM   main       relativeHumidityMeasurement  humidity     "58" %
 ```

Status for my thermostat

```bash
smartthings devices:status <id>
───────────────────────────────────────────────────────────────────────────────────────
 Capability                     Attribute                    Value
 relativeHumidityMeasurement    humidity                     58 %
 healthCheck                    checkInterval                60 s
 healthCheck                    healthStatus
 healthCheck                    DeviceWatch-Enroll
 healthCheck                    DeviceWatch-DeviceStatus     "online"
 temperatureMeasurement         temperature                  72 F
 thermostatFanMode              thermostatFanMode            "auto"
 thermostatFanMode              supportedThermostatFanModes  ["auto","on","circulate"]
 thermostatHeatingSetpoint      heatingSetpoint              66 F
 thermostatMode                 thermostatMode               "cool"
 thermostatMode                 supportedThermostatModes     ["cool","heat","off"]
 watchpanel55613.tccthermostat  drcapable                    true
 thermostatCoolingSetpoint      coolingSetpoint              82 F
───────────────────────────────────────────────────────────────────────────────────────
```

Hacky way to get the temperature measurement. Need to properly parse the json but will figure that out later.

```bash
smartthings devices:status <id> | grep -A 3 "temperature"
            "temperatureMeasurement": {
                "temperature": {
                    "value": 72,
                    "unit": "F",
                    "timestamp": "2023-07-15T14:18:13.570Z"
```
