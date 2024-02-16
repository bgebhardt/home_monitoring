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

# TODO's

- Set up secure remote connections - ssl, duckdns, etc. - see [(839) Home Assistant 101: Setting up Remote Access - YouTube](https://www.youtube.com/watch?v=EQEpue7GhdI&t=675s)
- Backup the server
- Set up battery alerts

- Set up energy dashboard once Tesla fixed - here's how [Using Tesla Powerwall Data on the HA Energy Dashboard - Third party integrations - Home Assistant Community](https://community.home-assistant.io/t/using-tesla-powerwall-data-on-the-ha-energy-dashboard/333357)

Done
- Set up companion app
- Move Home Assistant to Mac mini

# [Home Assistant](https://www.home-assistant.io/)

You run this as a server and it can run without a hub like Homekit requires. Has great out of the box functionality and a ton of integrations. There's an iOS app which I haven't set up yet.

## Install

Good background: [Which Installation Method is Best for Home Assistant? – Siytek](https://siytek.com/which-installation-method-is-best-for-home-assistant/)

*This was the best tutorial I found to install.*
To install as a VM on a mac (hard)

Refer to installation guide here:
[Run Home Assistant on macOS with a Debian 12 Virtual Machine – Siytek](https://siytek.com/home-assistant-macos-utm-debian-12/)

Original article I used replaced by above: [How To Install Home Assistant Supervised on Mac OS – Siytek](https://siytek.com/home-assistant-supervised-on-mac-os/)


Note there may be updates here: [home-assistant/supervised-installer: Installer for a generic Linux system](https://github.com/home-assistant/supervised-installer)

*Other options reviewed*
To install natively on a mac (easy, but didn't work and no addons) - [How To Install Home Assistant On Mac OS – Siytek](https://siytek.com/install-home-assistant-on-mac/) - But you miss the Home Assistant Supervisor and its features
Official install docs which require understanding VM's (hard) - [MacOS - Home Assistant](https://www.home-assistant.io/installation/macos)

### UTM set up

It uses [UTM | Virtual machines for Mac](https://mac.getutm.app/) which is very cool. UTM has lots of Mac friendly features. Even AppleScript [Scripting | UTM Documentation](https://docs.getutm.app/scripting/scripting/)!

- Set networking to Bridged (Advanced)
- In your VM run `ip addr | more` to get the internet ip address

On networking: [UTM Networking Mac M1 - YouTube](https://www.youtube.com/watch?v=GgDEwQXpZI8)

- Shared Network (NAT) - can connect out to the WAN but can not be connected to
- Host Only - No connection to the WAN or host network. But can communicate between VMs on the machine with ssh.
- Bridged (Advanced) - select virtio-net-pic. Get IP from your host network.

More references

- [Network | UTM Documentation](https://docs.getutm.app/settings-qemu/devices/network/network/)
- [Virtual Box vs. UTM: Run Virtual Machines on Your Apple Silicon M1 Mac](https://eshop.macsales.com/blog/72081-utm-virtual-machine-on-m1-mac/)
- [Debian 11 + Rosetta | UTM Documentation](https://docs.getutm.app/guides/debian/)

### Start UTM on startup

Ideally I'd run as a service in the background, but choosing to do it as a login item as that's easier for me following these instructions - [Remote Control | UTM Documentation](https://docs.getutm.app/advanced/remote-control/).

Headless can run in the background [Headless | UTM Documentation](https://docs.getutm.app/advanced/headless/), but I don't want to have to login via ssh.
Interseting ideas here too. [\[MacOS\] Start VM Headless/In Background · Issue #2280 · utmapp/UTM](https://github.com/utmapp/UTM/issues/2280)

### Home Assistant companion app (iOS/Android)

- Install the app
- Enter server address manually if not found

You can run the companion app on your Mac and it has sensors you can use for automation! It lets you add widgets and buttons to trigger actions that get sent to Home Assistant. See details here: [Getting started with the home assistant app for MAC os | JuanMTech](https://www.juanmtech.com/getting-started-with-the-home-assistant-app-for-macos/)

## Moving VM to a new Machine

Refer to installation guide here: 
[Run Home Assistant on macOS with a Debian 12 Virtual Machine – Siytek](https://siytek.com/home-assistant-macos-utm-debian-12/)

Original article I used replaced by above: [How To Install Home Assistant Supervised on Mac OS – Siytek](https://siytek.com/home-assistant-supervised-on-mac-os/)

### Install UTM

```brew install --cask utm```

[UTM | Virtual machines for Mac](https://mac.getutm.app/)
[macOS | UTM Documentation](https://docs.getutm.app/installation/macos/)

### Set up virtual machine

Start UTM
Drag VM image into UTM interface

### Set up networking

see info in this article here [Configuring Bridged Mode Networking](https://siytek.com/home-assistant-macos-utm-debian-12/#configuring-bridged-mode-networking)

This is likely already configured for the VM as it’s a he VM file. It should be set to "Bridged (Advanced)."

Make sure it's on the right Ethernet interview. You can find them listed running this command
```networksetup -listallhardwareports```

Check the vm's ip address with
`hostname -I` or
`ip addr | more` -- give more info on IP address

### Test locally

go to http://<ipaddress>:8123 in browser
login with homeassistant login
it will take some time for Homeassistant to start up again

### [Set up remote access](## Set up remote access)

see section below on Cloudflare setup
it should automatically come up

### Set up UTM to run on start up

[Remote Control | UTM Documentation](https://docs.getutm.app/advanced/remote-control/).

1. Find or create a shortcut to start the vm. I have one named "Home Assistant" which is my VM name already.
2. Select add to dock
3. Show in Finder
4. Drag the item to the login items in system preferences

### To disable Home Assistant on Mac

1. shutdown the home assistant server
2. remove the login item shortcut from system preferences.

## Common Linux Commands

As root

```reboot now``` - reboot vm
```shutdown``` - shutdown

## Configure

[Getting started with the home assistant app for MAC os | JuanMTech](https://www.juanmtech.com/getting-started-with-the-home-assistant-app-for-macos/)
[(838) HOW TO Connect Home Assistant to Apple Homekit - YouTube](https://www.youtube.com/watch?v=3tutxHO0J78)

Important security setup recommendations.
[5 ESSENTIAL Tips for Security on Home Assistant - YouTube](https://www.youtube.com/watch?v=AXKPIF3aJ6U)

Devices to configure
- Tesla Powerwall
- Honeywell Thermostat
- Samsung TV
- Vizio TV - note working yet; see info in [VIZIO SmartCast - Home Assistant](https://www.home-assistant.io/integrations/vizio) and [raman325/pyvizio: Python client for Vizio SmartCast](https://github.com/raman325/pyvizio)
- Xbox - see [Xbox - Home Assistant](https://www.home-assistant.io/integrations/xbox/)
- [Google Cast - Home Assistant](https://www.home-assistant.io/integrations/cast)


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

## Automatically Backing up Home Assistant

Great article outlining options: [Home Assistant Backup Methods & Best Practices - SmartHomeScene](https://smarthomescene.com/guides/home-assistant-backup-methods-and-best-practices/)

For me it's OneDrive using [lavinir/hassio-onedrive-backup](https://github.com/lavinir/hassio-onedrive-backup)

- Navigate to Settings > Add-ons > Add-on Store
- Click the three dots in the top right corner and select Repositories
- Add the following repo: https://github.com/lavinir/hassio-onedrive-backup
- Click Add than Close

Other info: [How do I back-up Home Assistant? – Maartendamen.com](https://maartendamen.com/how-do-i-back-up-home-assistant/#:~:text=Here%20it%20the%20quick%20basic%20answer%20to%20the,put%20your%20snapshot%20away%20in%20a%20secure%20place.)

## Set up remote access

Cloudflare tunnel approach
[The Easiest Free Way To Do Home Assistant Remote Access! - YouTube](https://www.youtube.com/watch?v=xXAwT9N-7Hw)
[brenner-tobias/ha-addons: Repository for Home Assistant Add-Ons](https://github.com/brenner-tobias/ha-addons)
[How tos · brenner-tobias/addon-cloudflared Wiki](https://github.com/brenner-tobias/addon-cloudflared/wiki/How-tos)

General tunnel creation instructions
- [You Need to Learn This! Cloudflare Tunnel Easy Tutorial - YouTube](https://www.youtube.com/watch?v=ZvIdFs3M5ic)
- [How to use Cloudflare Tunnel in your Homelab (even with Traefik) - YouTube](https://www.youtube.com/watch?v=yMmxw-DZ5Ec)

Great additional advice on the risks of Cloudflare tunnels
- [You should NOT use Cloudflare Tunnel (if you do this...) - YouTube](https://www.youtube.com/watch?v=oqy3krzmSMA)

TODO: look into stronger authentication approaches for the tunnel.

Dynamic DNS + port forwarding approach (not recommended)
[Home Assistant Remote Access for FREE - DuckDNS + LetsEncrypt + Single URL - YouTube](https://www.youtube.com/watch?v=AK5E2T5tWyM&list=WL&index=5)
[Home Assistant 101: Setting up Remote Access - YouTube](https://www.youtube.com/watch?v=EQEpue7GhdI&t=675s)

## Dashboard configuration

Great video on creating a dashboard - easy vs hard
- [Creating a Beautiful Home Assistant Mobile Dashboard Easily! - YouTube](https://www.youtube.com/watch?v=gouMnPxYHDc)

## Automation approaches

Tutorials and info
[Create a Basic Automation in Home Assistant](https://theprivatesmarthome.com/how-to/create-basic-automation-home-assistant/#:~:text=Create%20a%20Basic%20Automation%20in%20Home%20Assistant%201,next%20year%21%20...%204%20Deleting%20the%20Automation%20)
[Easy home Assistant Notifications using Alerts! - YouTube](https://www.youtube.com/watch?v=uQwIusogTZE&t=9s)
[I was wrong about Home Assistant Automations - YouTube](https://www.youtube.com/watch?v=7xfHiD4AuXM)
[5 Home Assistant Built-In Integrations You Probably Should be Using - YouTube](https://www.youtube.com/watch?v=QZB_o62AuV0)
[Easy Notifications with Alerts — Slacker Labs](https://www.slacker-labs.com/blog/2022/04/13/home-assistant-alerts)
[HOW TO Connect Home Assistant to Apple Homekit - YouTube](https://www.youtube.com/watch?v=3tutxHO0J78)
[Getting started with the home assistant app for MAC os | JuanMTech](https://www.juanmtech.com/getting-started-with-the-home-assistant-app-for-macos/)
See types of triggers at [Automation Trigger - Home Assistant](https://www.home-assistant.io/docs/automation/trigger/)

## Useful tips

Running automation every time period - use time pattern - [How Do Time Patterns Work in Home Assistant - Home Automation Insider](https://homeautomationinsider.com/how-do-time-patterns-work-in-home-assistant/)
- "/30" is every half hour; must be like cron patterns - [Time_pattern every full and half hour - Configuration - Home Assistant Community](https://community.home-assistant.io/t/time-pattern-every-full-and-half-hour/147263/2)
- Use template editor in dev tools - [Add sensor value to notification message - Share your Projects! / Dashboards & Frontend - Home Assistant Community](https://community.home-assistant.io/t/add-sensor-value-to-notification-message/117661/3)

Finding your variable - use dev tools and look at states. You can test code in Templates. Example here is the powerwall charge state class. Call its state to get the charing percentage.
See [State Objects - Home Assistant](https://www.home-assistant.io/docs/configuration/state_object/) for attributes.
{{states.sensor.**sensor-name**.state}}
{{states.sensor.powerwall_charge}}
{{states.sensor.powerwall_charge.state}}

Example:
{{states.sensor.powerwall_charge.name}} is at {{states.sensor.powerwall_charge.state}} {{states.sensor.powerwall_charge.attributes.unit_of_measurement}}
{{states.binary_sensor.powerwall_charging.name}} is {{states.binary_sensor.powerwall_charging.state}}
({{states.sensor.powerwall_battery_now.state}} {{states.sensor.powerwall_battery_now.attributes.unit_of_measurement}})
Result:
Powerwall Charge is at 58 %
Powerwall Charging is on
 (-2.29 kW)

## Raycast plugin

The [Raycast Store: Home Assistant](https://www.raycast.com/tonka3000/homeassistant) plugin allos you to control Home Assistant from the Raycast  app. It provides a clean interface to view entities, trigger automations, and more.

It is extremely slow loading via the extrenal URL, so configure access via the local URL. Otherwise follow the instructions included with the plugin.

You can search entities and even change them. For example I can increase or decrease the thermostat by 0.5 degrees.

## Tesla Configuration info

When configuring any energy cards with Tesla sensors these mean the following:
- Now - current energy usage (+ or -)
- Export - energy the device is outputting
- Import - energy the device is consuming

- Powerwall Battery = battery
- Powerwall Solar = solar
- Powerwall Site = grid (i.e. energy using or exporting to the grid)
- Powerwall Load = Home (i.e. the load from your home)

battery:
    entity: sensor.powerwall_battery_now
    state_of_charge: sensor.powerwall_charge
    display_state: two_way
grid:
    entity: sensor.powerwall_site_now
solar:
    entity: sensor.powerwall_solar_now
    display_zero_state: true
home:
    entity: sensor.powerwall_load_now

From [Using Tesla Powerwall Data on the HA Energy Dashboard - Third party integrations - Home Assistant Community](https://community.home-assistant.io/t/using-tesla-powerwall-data-on-the-ha-energy-dashboard/333357)
Here’s what I did after upgrading to Home Assistant 2019.9 45

- Grid Consumption: Powerwall Site Import
- Return to grid: Powerwall Site Export
- Solar Production: Powerwall Solar Export
- Home Battery Storage:
    - Energy going in to the battery (kWh): Powerwall Battery Import
    - Energy coming out of the battery (kWh): Powerwall Battery Export

 More info on Powerwall
- [Tesla Powerwall - Home Assistant](https://www.home-assistant.io/integrations/powerwall)
- [Tesla Powerwall and Home Energy Management - Configuration - Home Assistant Community](https://community.home-assistant.io/t/tesla-powerwall-and-home-energy-management/335228)
- [Solar battery run time till empty - Configuration - Home Assistant Community](https://community.home-assistant.io/t/solar-battery-run-time-till-empty/408778)
- [Search results for 'powerwall' - Home Assistant Community](https://community.home-assistant.io/search?q=powerwall)

Best power distribution card I've found. Requires HACS.
[ulic75/power-flow-card: A power distribution card inspired by the official Energy Distribution card for Home Assistant](https://github.com/ulic75/power-flow-card/)

## Forecast Solar configuration
[Forecast.Solar - Home Assistant](https://www.home-assistant.io/integrations/forecast_solar)

- Put in the kW capacity of your solar system in watts.
- To calculate your azimuth see - [find_your_azimuth \[Forecast.Solar\]](https://doc.forecast.solar/find_your_azimuth)
    - suncalc.org azimuth for me is 66.88
    - Openstreet Maps azimuth for me is 303 but I think I did this wrong
- declination - got from my Tesla plans - 18

## Weather

Recommend National Weather Service
Use any number for the API key - reference: [NWS Integration API Key - Where to obtain ley? - Configuration - Home Assistant Community](https://community.home-assistant.io/t/nws-integration-api-key-where-to-obtain-ley/252913/2)

## Mushroom dashboard Cards

Take a look at the additional cards here: [lovelace-mushroom/docs/cards/template.md at main · piitaya/lovelace-mushroom](https://github.com/piitaya/lovelace-mushroom/blob/main/docs/cards/template.md)

### More automation tutorials

- [How to theme home assistant | JuanMTech](https://www.juanmtech.com/how-to-theme-home-assistant/)
- [Install hacs in home assistant for themes and custom cards | JuanMTech](https://www.juanmtech.com/install-hacs-in-home-assistant-for-themes-and-custom-cards/)
    - [Home Assistant Community Store | HACS](https://hacs.xyz/)
- [Set up an alarm system with home assistant and alarmo | JuanMTech](https://www.juanmtech.com/set-up-an-alarm-system-with-home-assistant-and-alarmo/)

## Potential Automations

Automations to explore

- [Howto: Notify me when users arrive or depart my Home zone - Configuration - Home Assistant Community](https://community.home-assistant.io/t/howto-notify-me-when-users-arrive-or-depart-my-home-zone/332702)
- 


## Notification options

- To your mobile device if the companion app is installed
- [SendGrid - Home Assistant](https://www.home-assistant.io/integrations/sendgrid) - free 100 mails/day
- in browser - [HTML5 Push Notifications - Home Assistant](https://www.home-assistant.io/integrations/html5)
- Email SMTP server - [Can Home Assistant Send Email? – Siytek](https://siytek.com/can-home-assistant-send-email/#:~:text=Can%20Home%20Assistant%20Send%20Email%3F%201%20Setting%20up,service%20to%20Home%20Assistant.%20...%203%20Conclusion%20)
- [ClickSend SMS - Home Assistant](https://www.home-assistant.io/integrations/clicksend/)

sensor.powerwall_charge

## Nintendo Switch integration

There is no official integration for Nintendo Switch but these seem promising/interesting.

- [New Integration: Nintendo Switch - Feature Requests - Home Assistant Community](https://community.home-assistant.io/t/new-integration-nintendo-switch/564797)
- [Nintendo Switch App Sensor - Track for example your Ring Fit Activity - Share your Projects! - Home Assistant Community](https://community.home-assistant.io/t/nintendo-switch-app-sensor-track-for-example-your-ring-fit-activity/308280/10)
- [Samuel Elliott / Nintendo Switch app APIs · GitLab](https://gitlab.com/samuelthomas2774/nxapi)

## Advice on Templates

[Mastering Home Assistant Templates: A Beginner's Guide - YouTube](https://www.youtube.com/watch?v=m1aqyX6LXlo)
[Mastering Home Assistant Templates: Intro to Date and Time - YouTube](https://www.youtube.com/watch?v=2WIi5xq0iHI)

## References

- Great tutorials are here: [Home Assistant – Siytek](https://siytek.com/category/smart-home-tek/home-assistant/)
- [Home Assistant Beginner’s Guide: Setting up Home Assistant](https://home-assistant-guide.com/guide/the-home-assistant-beginners-guide-part-1-setting-up-hass-io/#:~:text=The%20Home%20Assistant%20Supervisor%20allows%20you%2C%20the%20user%2C,Make%20and%20restore%20backups%20Add-ons%20Unified%20audio%20system) - Explains different Home Assistant parts
- [Home Assistant COMPLETE Beginners Guide 2023 - YouTube](https://www.youtube.com/watch?v=LI3lhgOiZ-8)

- [Tesla Powerwall and Home Energy Management - Configuration - Home Assistant Community](https://community.home-assistant.io/t/tesla-powerwall-and-home-energy-management/335228/7)
- [Solar battery run time till empty - Configuration - Home Assistant Community](https://community.home-assistant.io/t/solar-battery-run-time-till-empty/408778/12)
- [Search results for 'powerwall' - Home Assistant Community](https://community.home-assistant.io/search?q=powerwall)
- [Overview – Home Assistant](http://192.168.64.2:8123/lovelace/0)

# [Homekit and Homebridge](Homekit-and-homebridge.md)