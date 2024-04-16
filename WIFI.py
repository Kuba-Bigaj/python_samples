import os
import socket
import time

def showAvailableWiFiNetworks():
    command = "netsh wlan show networks interface=Wi-Fi"
    os.system(command)


def connectToWiFiNetwork(name, SSID):
    command = "netsh wlan connect name=\"" + name + "\" ssid=\"" + SSID + "\" interface=Wi-Fi"
    os.system(command)
    print("Połączono do sieci! ")
    command = "arp -a 192.168.1.1"
    os.system(command)


def createNewConnection(name, SSID):
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>""" + name + """</name>
    <SSIDConfig>
        <SSID>
            <name>""" + SSID + """</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>open</authentication>
                <encryption>none</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
        </security>
    </MSM>
</WLANProfile>"""
    command = "netsh wlan add profile filename=\"" + name + ".xml\"" + " interface=Wi-Fi"
    with open(name + ".xml", 'w') as file:
        file.write(config)
    os.system(command)


def enableWiFiCard():
    command = "netsh interface set interface Wi-Fi enable"
    os.system(command)


def disableWiFiCard():
    command = "netsh interface set interface Wi-Fi disable"
    os.system(command)


if __name__ == '__main__':
    disableWiFiCard()
    enableWiFiCard()
    showAvailableWiFiNetworks()
    name = input("Podaj nazwe sieci (SSID): ")
    createNewConnection(name, name)
    connectToWiFiNetwork(name, name)

