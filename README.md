# Home Monitoring

This is my home monitoring setup repo.

A few goals.

- Monitor Powerwall battery charging
    - Alert at certain levels
- Monitor my indoor thermostat temperature over time and compare to weather forecast
    - Optimize when to turn on the AC when there is enough solar to offset its use
    - Pre-cool the house

# Powerwall scripts and monitoring

see notes in obsidian://open?vault=Personal&file=Coding%20%26%20Hack%20Projects%2FTesla%20Solar%20Powerwall%20Monitoring

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
Site Name: My Home - Firmware: 23.12.1 7ca1b02c - DIN: 1538000-25-F--GF2220800001K3
System Uptime: 119h18m30.79789591s

Battery power level: 67%
Combined power metrics: {'site': -202, 'solar': 8739.7001953125, 'battery': -3680, 'load': 4960.1650390625}

Grid Power: -0.20kW
Solar Power: 8.74kW
Battery Power: -3.68kW
Home Power: 4.96kW
```

# Monitoring Thermostat

see obsidian://open?vault=Personal&file=Household%20and%20Home%2FMonitoring%20Thermostat%20and%20Smart%20Home

My thermostat can be registered with Samsung Smartthings

Trying Smartthings CLI to pull indoor temperature reading.
[SmartThingsCommunity/smartthings-cli: Command-line Interface for the SmartThings APIs.](https://github.com/SmartThingsCommunity/smartthings-cli)
docs: [Get Started With the SmartThings CLI | SmartThings Developers](https://developer.smartthings.com/docs/sdks/cli/introduction/)
configuration docs: [smartthings-cli/packages/cli/doc/configuration.md at main · SmartThingsCommunity/smartthings-cli](https://github.com/SmartThingsCommunity/smartthings-cli/blob/main/packages/cli/doc/configuration.md)
api docs: [API | SmartThings Developers](https://developer.smartthings.com/docs/api/public/)

## Smartthings CLI Install

To install

```bash
brew install smartthingscommunity/smartthings/smartthings
```

## Exmaple usage

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
