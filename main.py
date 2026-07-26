from core.kernel import Kernel
from runtime.lilith_runtime import LilithRuntime


def main():

    print("================================")
    print("PRiZM v1.2")
    print("Checkpoint: 1101")
    print("================================")

    kernel = Kernel()
    kernel.boot()

    print()

    lilith = LilithRuntime()
    lilith.boot()

    print()
    print("STATUS: OPERATIONAL")
    print("CHECKPOINT: 1101")


if __name__ == "__main__":
    main()
