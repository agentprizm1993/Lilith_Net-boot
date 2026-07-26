from pathlib import Path
import shutil
from datetime import datetime


class Rollback:

    BACKUP_DIR = Path("backups")

    @staticmethod
    def initialize():
        Rollback.BACKUP_DIR.mkdir(exist_ok=True)

    @staticmethod
    def backup(source):

        Rollback.initialize()

        source_path = Path(source)

        if not source_path.exists():
            print(f"[SKIP] Missing: {source}")
            return False

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = Rollback.BACKUP_DIR / f"{source_path.name}_{timestamp}"

        if source_path.is_dir():
            shutil.copytree(source_path, backup_path)
        else:
            shutil.copy2(source_path, backup_path)

        print(f"[BACKUP] {source} -> {backup_path}")
        return True

    @staticmethod
    def restore(backup, destination):

        backup_path = Path(backup)
        destination_path = Path(destination)

        if not backup_path.exists():
            print("[ERROR] Backup not found")
            return False

        if backup_path.is_dir():
            shutil.copytree(
                backup_path,
                destination_path,
                dirs_exist_ok=True
            )
        else:
            shutil.copy2(
                backup_path,
                destination_path
            )

        print(f"[RESTORE] {backup} -> {destination}")
        return True


if __name__ == "__main__":
    print("Rollback Engine ONLINE")
