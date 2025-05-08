import subprocess
from datetime import datetime

# Liste des identifiants winget des applications à installer
libraries = [
    'Adobe.Acrobat.Reader.64-bit',
    'Microsoft.Office',
    'RARLab.WinRAR',
    'Google.Chrome'
]

LOG_FILE = 'install_log.txt'

def log(message: str):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")


def install_dependencies():
    for app in libraries:
        print(f"\n🔧 Installation de {app}...")
        log(f"Démarrage de l'installation de {app}")
        try:
            result = subprocess.run(
                ['winget', 'install', '--id', app, '--silent', '--accept-package-agreements', '--accept-source-agreements'],
                check=True,
                capture_output=True,
                text=True
            )
            print(f"✅ {app} installé avec succès.")
            log(f"Succès : {app} installé.\nSortie : {result.stdout.strip()}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Échec de l'installation de {app}.")
            log(f"Échec : {app} non installé.\nErreur : {e.stderr.strip() if e.stderr else str(e)}")


def install_update_module():
    print("\n📦 Installation du module PSWindowsUpdate...")
    log("Installation du module PSWindowsUpdate")
    try:
        subprocess.run([
            'powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command',
            'Install-Module -Name PSWindowsUpdate -Force -Confirm:$false -Scope AllUsers'
        ],
        check=True,
        capture_output=True,
        text=True)
        log("Succès : Module PSWindowsUpdate installé.")
    except subprocess.CalledProcessError as e:
        log(f"Échec de l'installation du module : {e.stderr.strip() if e.stderr else str(e)}")


def install_updates():
    print("\n🛠️ Installation des mises à jour Windows...")
    log("Démarrage des mises à jour Windows")
    try:
        subprocess.run([
            'powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-Command',
            'Import-Module PSWindowsUpdate; Install-WindowsUpdate -AcceptAll -AutoReboot -Confirm:$false'
        ],
        check=True,
        capture_output=True,
        text=True)
        log("Succès : Mises à jour installées.")
    except subprocess.CalledProcessError as e:
        log(f"Échec de l'installation des mises à jour : {e.stderr.strip() if e.stderr else str(e)}")


if __name__ == '__main__':
    log("=== Début de l'installation des applications ===")
    install_dependencies()
    install_update_module()
    install_updates()
    log("=== Fin de l'installation ===\n")