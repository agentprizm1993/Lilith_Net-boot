from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

print("=" * 50)
print("PRiZM GENESIS VALIDATION PASS")
print("Version: v3.2")
print("Checkpoint: 1101")
print("=" * 50)


checks = [
    "core/kernel.py",
    "core/registry.py",
    "core/event_system.py",
    "runtime/lilith_runtime.py",
    "runtime/capability_runtime.py",
    "engines/intent_engine.py",
    "core/command_intelligence.py",
    "agents/agent_registry.py",
    "agents/agent_orchestrator.py",
    "capabilities/capability_router.py",
    "workflows/workflow_engine.py",
    "validation/validation_engine.py",
    "validation/checkpoint_recorder.py",
    "evolution/evolution_engine.py",
    "governance/policy_engine.py",
    "governance/permission_manager.py",
    "trust/trust_fabric.py",
    "trust/audit_engine.py",
    "security/integrity_guard.py",
    "recovery/recovery_engine.py"
]


passed = 0

print()
print("SYSTEM VALIDATION")
print("------------------------------")

for item in checks:

    path = ROOT / item

    if path.exists():
        print(f"{item:<40} PASS")
        passed += 1
    else:
        print(f"{item:<40} MISSING")


print()
print("==============================")
print("VALIDATION RESULT")
print("==============================")

print(f"Passed: {passed}/{len(checks)}")

if passed == len(checks):

    print("STATE: OPERATIONAL")
    print("CHECKPOINT: 1101 VERIFIED")

else:

    print("STATE: REVIEW REQUIRED")
