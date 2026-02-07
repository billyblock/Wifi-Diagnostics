# Wifi Diagnostics

## Overview

The project outputs internet information to a CSV. This info is useful to determine issues with your internet connection at the click of a button!

## Features

The program will print the following information to a CSV.

- Max and Avg ping from your computer to Google.
- Download and Upload speed.
- Packet loss.
- Access point swapping.

## Example

``` 
packetsLost	maximumPing	averagePing	downloadSpeed	uploadSpeed	previousBSSID	currentBSSID	bssidChanged

0	37	28	40.01	26.03	**:**:**:**:**:**	**:**:**:**:**:**	True
```

## Running the Program

The program can only be run on Windows 10/11 devices.

It's python - just press run!

## Why I built this?

My internet at my new apartment was very slow and I could not do basic functions like zoom calls, gaming, or even browse the web at times. 

Using this script, I was able to diagnose that my computer kept on bouncing between Access Points. This cost delays in ping, packet loss, and an overall decrease in speeds. 

I later forwarded this information to my apartments landlord. They were able to fix the issue given this information.