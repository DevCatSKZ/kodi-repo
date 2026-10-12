# AGENTS.md – Hinweise für Agenten/Sessions

## Repo-Status (Stand: letzter Devin-Commit)

- `addons.xml` enthält 4 Addons: `repository.devcatskz`, `service.nconnect`,
  `plugin.nconnect.status`, `script.nconnect.bundle`.
- `tools/build_repo.py` erzeugt `addons.xml`, `addons.xml.md5` und `.sha256`-Dateien.
  Nie `addons.xml` von Hand editieren – immer das Tool laufen lassen.

## WICHTIG: Repo wurde gelöscht und neu angelegt

Das GitHub-Repo `DevCatSKZ/kodi-repo` wurde komplett gelöscht und neu
angelegt, weil eine private IPTV-Playlist des Nutzers
(`livetv/playlist.m3u`) versehentlich committet worden war und GitHub
alte Commit-Objekte weiterhin auslieferte. Alle `livetv/`-,
`service.livetv.*`-Pfade und LiveTV-Beschreibungen sind aus der
gesamten Historie entfernt.

**Konsequenz für andere Clones:**
- Jeder bestehende Clone ist veraltet – NICHT per `git pull` mergen.
- Stattdessen: `git fetch origin && git reset --hard origin/main`
  oder frisch klonen.

## Regeln für dieses Repo

- **Keine User-Daten committen**: keine Playlists, M3Us, Senderlisten,
  IP-Adressen oder sonstige private Inhalte des Nutzers. LiveTV-/EPG-
  Tooling bleibt lokal auf dem Gerät des Nutzers.
- Addon-ZIPs gehören nach `<addon-id>/<addon-id>-<version>.zip`,
  dann `python tools/build_repo.py`, commit, push.
- `KEEP = 2` in `build_repo.py` – alte Versionen werden automatisch gelöscht.

## N-Connect-Addons (von Devin erstellt)

- `plugin.nconnect.status`: Skin-Widget für verbundene Controller
  (Name, Akku, Ladestatus, Spieler). Liest `status.json` von
  `service.nconnect`, sendet Befehle via `NotifyAll(service.nconnect, ...)`.
  Unterstützt Aeon-Nox-Silvo-Integration (skinshortcuts labelID =
  `service.nconnect`).
- `script.nconnect.bundle`: Offline-Installer, der beide Addons aus
  eingebetteten ZIPs entpackt und die Silvo-Menü/Widget-Einbindung setzt.
  Quellcode: `C:\Users\Skittelz\Downloads\script.nconnect.bundle\`.

## Kontext Gerät

- RPi4, LibreELEC 12.2.1, IP `192.168.0.218` (SSH: root).
- Kodi-JSON-RPC: `http://kodirpi4:****@192.168.0.218:8080/jsonrpc`
  (Passwort in der lokalen Session bekannt, nicht ins Repo schreiben).
- Skin: `skin.aeon.nox.silvo`; N-Connect-Widget läuft über Container 801110.
