from engines.memory_engine import MemoryEngine

m = MemoryEngine()

m.save("last_boot", "1101")

print(m.load())
