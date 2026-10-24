# -*- coding: utf-8 -*-
"""
Holt die jeweils neuesten GitHub-Releases fremder Plugins ins Repository,
damit Kodi sie über repository.devcatskz selbst aktualisieren kann.

- plugin.video.youtube  – anxdpanic/plugin.video.youtube (das "+unofficial"-Asset für Kodi 19+)
- plugin.video.newpipe  – TrainAgain2/NewPipe-MOD

Ablauf: neueste Version je Plugin prüfen, fehlendes ZIP nach <id>/<id>-<version>.zip
ablegen. Danach tools/build_repo.py ausführen (addons.xml, md5, sha256, index.html).
Aufruf:  python tools/update_drittanbieter.py
"""
import json
import pathlib
import re
import sys
import urllib.request

API = 'https://api.github.com/repos/{}/releases/latest'

PLUGINS = {
    'plugin.video.youtube': (
        'anxdpanic/plugin.video.youtube',
        re.compile(r'plugin\.video\.youtube-[\d.]+%2Bunofficial\.[\d]+\.zip$')),
    'plugin.video.newpipe': (
        'TrainAgain2/NewPipe-MOD',
        re.compile(r'plugin\.video\.newpipe-[\d.]+\.zip$')),
}

ZEITRAHMEN = 20


def lade(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'kodi-repo-updater'})
    return urllib.request.urlopen(req, timeout=ZEITRAHMEN).read()


def main(repo):
    geaendert = False
    for plugin_id, (projekt, muster) in PLUGINS.items():
        try:
            release = json.loads(lade(API.format(projekt)).decode('utf-8'))
        except Exception as e:  # noqa: BLE001 – Netz/API-Limit
            print('{0}: Release-Abfrage fehlgeschlagen ({1}) – übersprungen'.format(plugin_id, e))
            continue
        ziel = None
        for asset in release.get('assets', []):
            name = asset.get('name', '')
            if muster.search(name.replace('+', '%2B')) or muster.search(name):
                ziel = asset['browser_download_url'], name
                break
        if not ziel:
            print('{0}: kein passendes Asset in Release {1}'.format(plugin_id, release.get('tag_name')))
            continue
        url, name = ziel
        # Dateiname muss <id>-<version>.zip entsprechen; urllib-quoted Namen auflösen
        name = name.replace('%2B', '+')
        datei = repo / plugin_id / name
        if datei.exists():
            print('{0}: {1} liegt bereits vor'.format(plugin_id, name))
            continue
        datei.parent.mkdir(exist_ok=True)
        print('{0}: lade {1} ...'.format(plugin_id, name))
        datei.write_bytes(lade(url))
        geaendert = True
        print('  -> {0}'.format(datei))
    print('fertig – bei Änderungen jetzt: python tools/build_repo.py')
    return geaendert


if __name__ == '__main__':
    main(pathlib.Path(__file__).resolve().parent.parent)
