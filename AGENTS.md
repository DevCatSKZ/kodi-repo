# AGENTS.md – Hinweise für Agenten/Sessions

## Repo-Status

- `addons.xml` enthält 4 Addons: `repository.devcatskz`, `service.nconnect`,
  `plugin.nconnect.status`, `script.nconnect.bundle`.
- `tools/build_repo.py` erzeugt `addons.xml`, `addons.xml.md5`, `.sha256`-Dateien
  und die `index.html`-Verzeichnislisten (Dateimanager-Quelle über GitHub Pages,
  `https://devcatskz.github.io/kodi-repo/`).
  Nie `addons.xml` oder `index.html` von Hand editieren – immer das Tool laufen lassen.
- Die Quelle von `tools/build_repo.py` liegt im N-Connect-Repository unter
  `linux/kodi/repo-tools/` und wird beim Ablegen hierher kopiert.

## WICHTIG: Repo wurde gelöscht und neu angelegt

Das GitHub-Repo `DevCatSKZ/kodi-repo` wurde komplett gelöscht und neu
angelegt, weil versehentlich private Daten des Nutzers (unter `livetv/`)
committet worden waren und GitHub alte Commit-Objekte weiterhin
auslieferte. Alle `livetv/`- und
`service.livetv.*`-Pfade (Playlist, Add-on-ZIPs) sind aus der gesamten
Historie entfernt. Ältere Stände von `addons.xml` und `README.md` in der
Historie (Commits 14d8458 bis 874ca3e) enthalten aber noch
Beschreibungen und Einrichtungshinweise der LiveTV-Add-ons. Ob die
Historie weiter bereinigt wird, entscheidet der Nutzer.

**Konsequenz für andere Clones:**
- Jeder bestehende Clone ist veraltet – NICHT per `git pull` mergen.
- Stattdessen: `git fetch origin && git reset --hard origin/main`
  oder frisch klonen.

## Regeln für dieses Repo

- **Keine User-Daten committen**: keine Playlists, M3Us, Senderlisten,
  IP-Adressen, Zugangsdaten, Benutzernamen, lokale Pfade oder sonstige
  private Inhalte des Nutzers. Geräte- und Netzdaten gehören in lokale,
  nicht versionierte Notizen. LiveTV-/EPG-Tooling bleibt lokal auf dem
  Gerät des Nutzers.
- **Commits als `devcatskz <devcatskz@gmail.com>`**, ohne
  „Co-Authored-By“- und ohne „Generated with …“-Zeilen.
- Addon-ZIPs gehören nach `<addon-id>/<addon-id>-<version>.zip`,
  dann `python tools/build_repo.py`, commit, push.
- Eine schon veröffentlichte Version nie überschreiben – für ein Update
  die Version in der `addon.xml` erhöhen.
- `KEEP = 2` in `build_repo.py` – alte Versionen werden automatisch gelöscht.

## N-Connect-Addons

- Quellcode aller vier Add-ons: N-Connect-Repository
  (`github.com/DevCatSKZ/N-Connect`), Ordner `linux/kodi/`.
- Bauen und hier ablegen (beim Release, von Hand): im N-Connect-Ordner
  `linux/build-kodi-addon.ps1 -Repo -RepoDir <dieses Repository>` (prüft
  Versionen, legt ZIPs und `downloads/` ab, baut den Index), danach hier
  committen und pushen. Die CI von N-Connect schreibt nicht hierher
  (kein automatischer Zugang; Deploy-Keys sind in der Organisation
  abgeschaltet).
- `plugin.nconnect.status`: ältere Widget-Quelle für Skins; leitet an
  `plugin.py` von `service.nconnect` weiter. Unterstützt
  Aeon-Nox-Silvo-Integration (skinshortcuts labelID = `service.nconnect`).
- `script.nconnect.bundle`: Offline-Installer, der beide Addons aus
  eingebetteten ZIPs (jeweils die beim Bauen aktuelle Version) entpackt
  und die Silvo-Menü/Widget-Einbindung setzt. Bei jeder neuen
  `service.nconnect`- oder Plugin-Version auch die Bundle-Version erhöhen.
