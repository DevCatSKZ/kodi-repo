<p align="center"><img src="repository.devcatskz/icon.png" width="120" alt="DevCatSKZ"></p>

<h1 align="center">DevCatSKZ Repository</h1>

<p align="center">Kodi-Add-ons von DevCatSKZ mit automatischen Updates.<br>
<i>Kodi add-ons by DevCatSKZ with automatic updates.</i></p>

<p align="center"><a href="https://github.com/DevCatSKZ/kodi-repo/raw/main/repository.devcatskz.zip"><b>repository.devcatskz.zip</b></a></p>

## Add-ons

| Add-on | Beschreibung · Description |
|---|---|
| **[N-Connect](https://github.com/DevCatSKZ/N-Connect)** (`service.nconnect`) | Switch-2-Controller (Pro Controller 2, Joy-Con 2, GameCube) als Xbox-Controller für Kodi und RetroArch, mit Vibration, Akkuwarnung und Home-Widget. Läuft unter LibreELEC, Batocera und Linux; unter Kodi für Windows und Android zeigt es den Stand der N-Connect-App an. · *Switch 2 controllers as Xbox controllers for Kodi and RetroArch.* |
| N-Connect Status (`plugin.nconnect.status`) | Widget-Quelle für Skins mit dem älteren Pfad `plugin://plugin.nconnect.status/`. · *Widget source for skins using the older path.* |
| N-Connect Bundle (`script.nconnect.bundle`) | Installiert beide Add-ons und richtet im Skin Aeon Nox: Silvo einen Menüpunkt mit Widget ein. · *Installs both add-ons and adds a menu entry to Aeon Nox: Silvo.* |

Geprüft auf einem Raspberry Pi 4 mit LibreELEC 12.2; andere Geräte sind noch ungetestet.
*Tested on a Raspberry Pi 4 with LibreELEC 12.2; other devices are not tested yet.*

## Installation

1. *Einstellungen › System › Add-ons*: **Unbekannte Quellen** einschalten.
2. [repository.devcatskz.zip](https://github.com/DevCatSKZ/kodi-repo/raw/main/repository.devcatskz.zip) auf das Gerät
   kopieren – oder unter *Einstellungen › Dateimanager › Quelle hinzufügen* die Adresse
   `https://devcatskz.github.io/kodi-repo/` eintragen.
3. *Add-ons › Aus ZIP-Datei installieren* › `repository.devcatskz.zip` wählen.
4. *Add-ons › Aus Repository installieren › DevCatSKZ Repository* › Add-on installieren.

*English:* enable **Unknown sources** (*Settings › System › Add-ons*), copy the repository zip to the device or add
`https://devcatskz.github.io/kodi-repo/` as a file manager source, then *Install from zip file* and
*Install from repository › DevCatSKZ Repository*.

Einzelne ZIPs je Gerät (ohne automatische Updates) liegen unter [`downloads/`](downloads/) und an den
[N-Connect-Releases](https://github.com/DevCatSKZ/N-Connect/releases/latest). · *Single ZIPs per device are in
`downloads/` and on the N-Connect releases page.*

## Für Entwickler · For developers

Der Quellcode der N-Connect-Add-ons liegt im [N-Connect-Repository](https://github.com/DevCatSKZ/N-Connect) unter
`linux/kodi/`. Neue Versionen werden beim Release mit `linux/build-kodi-addon.ps1 -Repo -RepoDir <kodi-repo>` hier
abgelegt; der Index (`addons.xml`, `.md5`) entsteht mit `tools/build_repo.py`. Eine vorhandene Version wird nie
überschrieben.

Inoffizielles Projekt ohne Verbindung zu Nintendo, Sony oder Microsoft. · MIT-Lizenz
