<p align="center"><img src="repository.devcatskz/icon.png" width="120" alt="DevCatSKZ"></p>

<h1 align="center">DevCatSKZ Repository</h1>

<p align="center">Alle Kodi-Plugins von DevCatSKZ an einem Ort – mit automatischen Updates.<br>
<i>All Kodi plugins by DevCatSKZ in one place – with automatic updates.</i></p>

<p align="center"><a href="https://github.com/DevCatSKZ/kodi-repo/raw/main/repository.devcatskz.zip"><b>⬇ repository.devcatskz.zip</b></a></p>

---

## Plugins

| Plugin | Beschreibung | Systeme |
|---|---|---|
| **[N-Connect](https://github.com/DevCatSKZ/N-Connect)** (`service.nconnect`) | Nintendo-Switch-2-Controller (Joy-Con 2, Pro Controller 2, GameCube) per Bluetooth – jeder Controller wird ein Xbox-Controller für Kodi, RetroArch und Spiele. Koppelt außerdem Xbox-, PlayStation-, Switch-1- und 8BitDo-Controller automatisch. Vibration, Akku-Warnung, Controller-Tasten für Kodi-Aktionen, 12 Sprachen. | LibreELEC / Linux: Raspberry Pi 2–5, 64-Bit-Boxen, PC |
| **N-Connect Status** (`plugin.nconnect.status`) | Widget-Plugin für Skins: zeigt verbundene Controller mit Name, Akku, Ladestatus und Spieler-Nr. als Liste. Klick auf einen Controller öffnet sein Untermenü (Trennen / Details / Vergessen) über den N-Connect-Kommando-Kanal. | Alle Kodi-Geräte mit `service.nconnect` |
| **N-Connect Bundle Installer** (`script.nconnect.bundle`) | All-in-One-Installer: installiert `service.nconnect` + `plugin.nconnect.status` aus eingebetteten ZIPs und richtet im Aeon-Nox-Silvo-Skin automatisch den N-CONNECT-Hauptmenüpunkt mit Controller-Widget ein. Danach Kodi neu starten. | LibreELEC / Linux |
| **LiveTV EPG Manager** (`service.livetv.epg`) | Richtet `pvr.iptvsimple` automatisch ein und hält das TV-Programm aktuell: täglicher Merge aus michazepg + epgshare01 (DE/AT/CH/UK/NL/PL/FR/IT/RO). Playlist wird aus `livetv/` geladen (URL in den Einstellungen änderbar). | Alle Kodi-Geräte mit `pvr.iptvsimple` |
| **LiveTV Komplettpaket** (`service.livetv.bundle`) | Wie LiveTV EPG Manager, aber mit eingebetteter Playlist und Icon – funktioniert nach der Installation komplett offline. | Alle Kodi-Geräte mit `pvr.iptvsimple` |

## LiveTV-Setup – aktueller Stand

| Komponente | Aktualisierung |
|---|---|
| **EPG (TV-Programm)** | Täglich automatisch. Auf dem RPi4 per Cron (`/storage/epg/update_epg.py`, 04:30 Uhr); in den Addons durch den eingebauten Service-Loop (einstellbar). |
| **Stream-URLs (Vavoo, Joyn)** | Selbstheilend: die Einträge nutzen `plugin.video.vavooto`- bzw. `plugin.video.joyn`-Pfade, das jeweilige Addon löst den Stream beim Abspielen auf. |
| **Radio-Streams** | Feste URLs, ändern sich praktisch nie. |
| **Senderliste (`livetv/playlist.m3u`)** | **Manuell / Snapshot.** Wird von `build_epg.py` aus den Quell-Playlists + epgshare01-IDs + kodinerds-Logos gebaut und hier gepusht. Der RPi4 zieht sie täglich 04:35 Uhr per `/storage/epg/update_playlist.py` und lädt IPTV Simple bei Änderung neu. Neue/entfernte Kanäle erfordern einen neuen Build + Push. |

Auf dem RPi4 laufen die Updates ohne Addon über Cron in `/storage/epg/` – auf anderen Geräten übernimmt das `service.livetv.epg`-Addon. Beide Varianten nicht gleichzeitig installieren, sonst entstehen doppelte Sender.

### N-Connect einzeln herunterladen (ohne Repository) · Single download

| System / Gerät · Device | Datei · File |
|---|---|
| **LibreELEC – alle Geräte (empfohlen)** · all devices (recommended) | [N-Connect-Kodi-LibreELEC-alle-Geraete.zip](https://github.com/DevCatSKZ/kodi-repo/raw/main/downloads/N-Connect-Kodi-LibreELEC-alle-Geraete.zip) |
| LibreELEC – Raspberry Pi 4 / 5, 64-Bit-Boxen (Amlogic, Rockchip …) | [N-Connect-Kodi-LibreELEC-RPi4-RPi5-arm64.zip](https://github.com/DevCatSKZ/kodi-repo/raw/main/downloads/N-Connect-Kodi-LibreELEC-RPi4-RPi5-arm64.zip) |
| LibreELEC – Raspberry Pi 2 / 3 (32 Bit) | [N-Connect-Kodi-LibreELEC-RPi2-RPi3-arm.zip](https://github.com/DevCatSKZ/kodi-repo/raw/main/downloads/N-Connect-Kodi-LibreELEC-RPi2-RPi3-arm.zip) |
| LibreELEC – PC / Mini-PC (Generic, x86_64) | [N-Connect-Kodi-LibreELEC-PC-x86_64.zip](https://github.com/DevCatSKZ/kodi-repo/raw/main/downloads/N-Connect-Kodi-LibreELEC-PC-x86_64.zip) |
| Kodi unter Windows · Kodi on Windows | [N-Connect für Windows](https://github.com/DevCatSKZ/N-Connect/releases/latest) installieren – Kodi erkennt die Controller automatisch |

Über das Repository bekommt jedes Gerät automatisch die passende Version. · Via the repository every device gets the right version automatically.

## Installation (Deutsch)

1. Kodi > **Einstellungen > System > Add-ons**: „**Unbekannte Quellen**“ einschalten.
2. **[repository.devcatskz.zip](https://github.com/DevCatSKZ/kodi-repo/raw/main/repository.devcatskz.zip)** herunterladen und auf das Gerät kopieren
   (z. B. per Samba in den Ordner „Downloads“) – oder in Kodi unter **Einstellungen > Dateimanager > Quelle hinzufügen**
   die Adresse `https://raw.githubusercontent.com/DevCatSKZ/kodi-repo/main/` eintragen.
3. **Add-ons > Paket-Symbol > Aus ZIP-Datei installieren** > `repository.devcatskz.zip`.
4. **Add-ons > Paket-Symbol > Aus Repository installieren > DevCatSKZ Repository** > Plugin auswählen > **Installieren**.

Ab jetzt hält Kodi alle Plugins aus diesem Repository automatisch aktuell. Jedes Plugin lässt sich auch einzeln
installieren: Die ZIP-Dateien liegen in den Ordnern dieses Repositorys (z. B. [`service.nconnect/`](service.nconnect/)).

## Installation (English)

1. Kodi > **Settings > System > Add-ons**: enable "**Unknown sources**".
2. Download **[repository.devcatskz.zip](https://github.com/DevCatSKZ/kodi-repo/raw/main/repository.devcatskz.zip)** and copy it to the device
   (e.g. via Samba into "Downloads") – or add `https://raw.githubusercontent.com/DevCatSKZ/kodi-repo/main/` as a source
   under **Settings > File manager > Add source**.
3. **Add-ons > package icon > Install from zip file** > `repository.devcatskz.zip`.
4. **Add-ons > package icon > Install from repository > DevCatSKZ Repository** > choose a plugin > **Install**.

From now on Kodi keeps all plugins from this repository up to date. Every plugin can also be installed on its own:
the zip files are in the folders of this repository (e.g. [`service.nconnect/`](service.nconnect/)).

## Für Entwickler / For developers

```
<addon-id>/<addon-id>-<version>.zip     Add-on-ZIPs (die zwei neuesten Versionen bleiben erhalten)
addons.xml, addons.xml.md5               Index für Kodi – erzeugt von tools/build_repo.py
repository.devcatskz.zip                 aktuelle Repository-ZIP zum direkten Herunterladen
```

Neues Plugin oder Update: ZIP nach `<addon-id>/` kopieren, `python tools/build_repo.py` ausführen, committen.
N-Connect wird mit `linux/build-kodi-addon.ps1 -Repo` aus dem N-Connect-Quellcode gebaut und hier abgelegt.

Kein offizielles Produkt von Nintendo, Microsoft oder Sony. · Not an official Nintendo, Microsoft or Sony product. · MIT-Lizenz
