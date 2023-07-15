#!/usr/bin/env python3

import pypowerwall
import powerwallconfig


# Optional: Turn on Debug Mode
# pypowerwall.set_debug(True)

# Credentials for your Powerwall - Customer Login Data
password =powerwallconfig.password
email =powerwallconfig.email
host = powerwallconfig.host               # Address of your Powerwall Gateway
timezone = powerwallconfig.timezone  # Your local timezone

# Connect to Powerwall
pw = pypowerwall.Powerwall(host,password,email,timezone)

# Some System Info
print("Site Name: %s - Firmware: %s - DIN: %s" % (pw.site_name(), pw.version(), pw.din()))
print("System Uptime: %s\n" % pw.uptime())

# Pull Sensor Power Data
grid = pw.grid()
solar = pw.solar()
battery = pw.battery()
home = pw.home()

# Display Data
print("Battery power level: %0.0f%%" % pw.level())
print("Combined power metrics: %r" % pw.power())
print("")

# Display Power in kW
print("Grid Power: %0.2fkW" % (float(grid)/1000.0))
print("Solar Power: %0.2fkW" % (float(solar)/1000.0))
print("Battery Power: %0.2fkW" % (float(battery)/1000.0))
print("Home Power: %0.2fkW" % (float(home)/1000.0))
print("")

# Raw JSON Payload Examples
#print("Grid raw: %r\n" % pw.grid(verbose=True))
#print("Solar raw: %r\n" % pw.solar(verbose=True))

# Display Device Vitals
#print("Vitals: %r\n" % pw.vitals())

# Display String Data
#print("String Data: %r\n" % pw.strings())
