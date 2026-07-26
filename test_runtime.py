from runtime.lilith_runtime import LilithRuntime

lilith = LilithRuntime()

lilith.boot()
lilith.execute("scan system")
