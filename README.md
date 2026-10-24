<p align="center"><img src="repository.devcatskz/icon.png" width="120" alt="DevCatSKZ"></p>

<h1 align="center">DevCatSKZ Repository</h1>

<p align="center">Kodi-Add-ons mit automatischen Updates.<br>
<i>Kodi add-ons with automatic updates.</i></p>

<p align="center"><a href="https://github.com/DevCatSKZ/kodi-repo/raw/main/repository.devcatskz.zip"><b>repository.devcatskz.zip</b></a></p>

## Add-ons

| Add-on | Beschreibung · Description |
|---|---|
| **[SKZ Connect](https://github.com/DevCatSKZ/SKZ-Connect)** (`service.skzconnect`) | Switch-2-, Xbox-, PlayStation- und Wii-Controller per Bluetooth als Xbox-Controller für Kodi und RetroArch; Vibration, Akkuwarnung, Home-Widget. LibreELEC, Batocera, Windows. · *Bluetooth controllers as Xbox controllers for Kodi and RetroArch.* |
| SKZ Connect Status (`plugin.skzconnect.status`) | Widget-Quelle für Skins (`plugin://plugin.skzconnect.status/`). · *Widget source for skins.* |
| SKZ Connect Bundle (`script.skzconnect.bundle`) | Installiert beide SKZ Connect-Add-ons in einem Schritt und richtet den Menüpunkt in Aeon Nox Silvo ein. · *Installs both SKZ Connect add-ons in one step and adds the menu entry in Aeon Nox Silvo.* |
| **[Catnewz](https://devcatskz.github.io/Catnewz/)** (`plugin.program.catnewz`) | Katzen-News nach Stimmung sortiert, mit Lesemodus, Widgets und Aktualisierung im Hintergrund. Kodi 19–22, alle Systeme. · *Cat news sorted by mood, with reader mode, widgets and background updates. Kodi 19–22.* |
| **VeraCrypt Manager** (`script.service.veracrypt`) | VeraCrypt-Platten und -Container per Passwort einbinden; verschlüsselter Tresor und Auto-Mount nach Neustart. Für LibreELEC auf Raspberry Pi. · *Mount VeraCrypt drives and containers by password; encrypted vault and auto-mount. For LibreELEC on Raspberry Pi.* |
| **Sunshine Game Stream Host** (`service.sunshine`) | Streamt den Kodi-Desktop an Moonlight-Clients. Nur LibreELEC aarch64 (RPi 4/5). · *Streams the Kodi desktop to Moonlight clients. LibreELEC aarch64 (RPi 4/5) only.* |
| **Moonlight Stream Client** (`script.moonlight`) | Spielt Sunshine-/GameStream-Streams ab. Noch im Aufbau. · *Plays Sunshine/GameStream streams. Work in progress.* |
| **Steam Link** (`script.steamlink`) | Steam Link für LibreELEC: Spiele vom PC streamen, Steuerung auch per Fernbedienung (CEC) und Kore/Yatse. · *Steam Link for LibreELEC: stream games from your PC, control via TV remote (CEC) and Kore/Yatse.* |
| NewPipe MOD (`plugin.video.newpipe`) | YouTube ohne Konto. Fremd-Add-on: Original von Twilight0, MOD von @TrainAgain2. · *YouTube without an account. Third-party add-on by Twilight0, MOD by @TrainAgain2.* |
| YouTube (`plugin.video.youtube`) | YouTube-Add-on von anxdpanic, bromix und MoojMidge (inoffizieller Build, nur mitgehostet). · *YouTube add-on by anxdpanic, bromix and MoojMidge (unofficial build, hosted here for convenience).* |

Getestet auf Raspberry Pi 4 (LibreELEC 12.2) und Kodi 21 unter Windows; andere Geräte sind ungetestet.
*Tested on Raspberry Pi 4 (LibreELEC 12.2) and Kodi 21 on Windows; other devices are untested.*

## Installation

1. *Einstellungen › System › Add-ons*: **Unbekannte Quellen** einschalten.
2. [repository.devcatskz.zip](https://github.com/DevCatSKZ/kodi-repo/raw/main/repository.devcatskz.zip) auf das Gerät
   kopieren – oder unter *Einstellungen › Dateimanager › Quelle hinzufügen* die Adresse
   `https://devcatskz.github.io/kodi-repo/` eintragen.
3. *Add-ons › Aus ZIP-Datei installieren* › `repository.devcatskz.zip` wählen.
4. *Add-ons › Aus Repository installieren › DevCatSKZ Repository* › Add-on installieren.

*English:* enable **Unknown sources** (*Settings › System › Add-ons*), add `https://devcatskz.github.io/kodi-repo/`
as a file-manager source or copy the zip to the device, then *Install from zip file* and
*Install from repository › DevCatSKZ Repository*.

Einzelne ZIPs je Gerät (ohne automatische Updates) liegen unter [`downloads/`](downloads/) und an den
[SKZ-Connect-Releases](https://github.com/DevCatSKZ/SKZ-Connect/releases/latest). · *Single ZIPs per device without
automatic updates are in `downloads/` and on the SKZ Connect releases page.*

## Für Entwickler · For developers

Der Quellcode der SKZ Connect-Add-ons liegt im [SKZ-Connect-Repository](https://github.com/DevCatSKZ/SKZ-Connect) unter
`linux/kodi/` (MIT). Catnewz ist proprietär (© DevCatSKZ, siehe dessen `addon.xml`); YouTube und NewPipe MOD gehören
den jeweiligen Projekten.

Inoffizielles Projekt ohne Verbindung zu Nintendo, Sony oder Microsoft.
