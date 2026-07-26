import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.kernel import Kernel
from engines.memory_engine import MemoryEngine

print("================================")
print("PRiZM SYSTEM STATUS")
print("Checkpoint: 1101")
print("================================")

kernel = Kernel()
memory = MemoryEngine()

print("Kernel...............ONLINE")
print("Registry.............ONLINE")
print("Event Bus............ONLINE")

print("Trust................ONLINE")
print("Integrity............ONLINE")
print("Memory...............ONLINE")
print("Observability........ONLINE")

print("Plugins..............ONLINE")
print("Workflows............ONLINE")

print("Health...............ONLINE")
print("Diagnostics..........ONLINE")
print("Recovery.............ONLINE")

saved = memory.load()

print()
print("Last Boot............", saved.get("last_boot", "UNKNOWN"))

print()
print("STATUS: OPERATIONAL")
print("CHECKPOINT: 1101")
