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
| **Moonlight Stream Client** (`script.moonlight.devcat`) | Spiele vom PC (Sunshine/GameStream) auf den Fernseher streamen; HEVC per Hardware (1080p mit 120 fps bei ~0,3 CPU-Kernen auf dem Pi 4), Bildrate passend zum TV bis 120 Hz, Pairing per PIN, Steuerung per Controller, TV-Fernbedienung (CEC, mit Maus-Modus für den PC-Desktop) und Remote-Apps inkl. Texteingabe. Nur LibreELEC aarch64 (RPi 4/5). · *Stream games from a PC (Sunshine/GameStream) to your TV; hardware HEVC decoding (1080p at 120 fps with ~0.3 CPU cores on a Pi 4), frame rate matched to the TV up to 120 Hz, PIN pairing, control via controller, TV remote (CEC, with a mouse mode for the PC desktop) and remote apps incl. text input. LibreELEC aarch64 (RPi 4/5) only.* |
| **Steam Link** (`script.steamlink`) | Steam Link für LibreELEC: Spiele vom PC streamen, Hardware-Dekodierung, Bildmodus und Bildrate bis 1080p@120, Steuerung auch per Fernbedienung (CEC) und Kore/Yatse. · *Steam Link for LibreELEC: stream games from your PC, hardware decoding, display mode and frame rate up to 1080p@120, control via TV remote (CEC) and Kore/Yatse.* |
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

## Einzelne ZIPs · Single ZIPs

Zum Installieren ohne Repository (*Add-ons › Aus ZIP-Datei installieren*), immer die aktuelle Version – aber ohne
automatische Updates. · *For installing without the repository (Install from zip file), always the current version –
but without automatic updates.*

| Add-on | Download |
|---|---|
| SKZ Connect | [alle Geräte · all devices](https://github.com/DevCatSKZ/kodi-repo/raw/main/downloads/SKZ-Connect-Kodi-LibreELEC-alle-Geraete.zip) · [RPi 4/5](https://github.com/DevCatSKZ/kodi-repo/raw/main/downloads/SKZ-Connect-Kodi-LibreELEC-RPi4-RPi5-arm64.zip) · [RPi 2/3](https://github.com/DevCatSKZ/kodi-repo/raw/main/downloads/SKZ-Connect-Kodi-LibreELEC-RPi2-RPi3-arm.zip) · [PC x86_64](https://github.com/DevCatSKZ/kodi-repo/raw/main/downloads/SKZ-Connect-Kodi-LibreELEC-PC-x86_64.zip) – auch an den [SKZ-Connect-Releases](https://github.com/DevCatSKZ/SKZ-Connect/releases/latest) |
| Catnewz | [alle Geräte · all devices](https://github.com/DevCatSKZ/kodi-repo/raw/main/downloads/Catnewz-Kodi-alle-Geraete.zip) |
| VeraCrypt Manager | [LibreELEC, Raspberry Pi](https://github.com/DevCatSKZ/kodi-repo/raw/main/downloads/VeraCrypt-Manager-Kodi-LibreELEC-RPi.zip) |
| Moonlight Stream Client | [LibreELEC, RPi 4/5](https://github.com/DevCatSKZ/kodi-repo/raw/main/downloads/Moonlight-Kodi-LibreELEC-RPi4-RPi5.zip) |
| Steam Link | [LibreELEC, Raspberry Pi](https://github.com/DevCatSKZ/kodi-repo/raw/main/downloads/Steam-Link-Kodi-LibreELEC-RPi.zip) |

Alle Dateien: [`downloads/`](downloads/) · *All files: `downloads/`*

## Für Entwickler · For developers

Der Quellcode der SKZ Connect-Add-ons liegt im [SKZ-Connect-Repository](https://github.com/DevCatSKZ/SKZ-Connect) unter
`linux/kodi/` (MIT). Catnewz ist proprietär (© DevCatSKZ, siehe dessen `addon.xml`); YouTube und NewPipe MOD gehören
den jeweiligen Projekten.

Moonlight Stream Client, Steam Link und VeraCrypt Manager sind Python-Add-ons, ihr Code liegt vollständig in den ZIPs.
Moonlight bringt [moonlight-embedded](https://github.com/moonlight-stream/moonlight-embedded) (GPLv3) mit einem
Raspberry-Pi-Patch mit; Patch und Quellhinweis liegen im Add-on unter `resources/source/`. Steam Link lädt Valves App
beim Einrichten direkt von Valve, das Add-on selbst enthält keinen Valve-Code.

Inoffizielles Projekt ohne Verbindung zu Nintendo, Sony oder Microsoft.
