from pathlib import Path
try:
    from runtime.trust.trust_engine import TrustEngine
except ModuleNotFoundError:
    from trust_engine import TrustEngine

class SentinelEngine:

    def __init__(self):
        self.name = "Sentinel Engine"
        self.version = "1.0"
        self.status = "ACTIVE"
        self.trust = TrustEngine()

    def scan_runtime(self):

        checks = {
            "runtime_directory": Path("runtime").exists(),
            "services_registry": Path(
                "runtime/services.json"
            ).exists(),
            "trust_status": self.trust.verify_checkpoint()
                == "VALID"
        }

        return checks


    def report(self):

        checks = self.scan_runtime()

        passed = all(
            checks.values()
        )

        return {
            "engine": self.name,
            "version": self.version,
            "status": self.status,
            "checks": checks,
            "sentinel_state":
                "SECURE" if passed else "WARNING"
        }


if __name__ == "__main__":

    sentinel = SentinelEngine()

    print(
        sentinel.report()
    )
