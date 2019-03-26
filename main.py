import juliaset
import time


def main():
    begin = time.time()
    juliaset.plot(complex(-0.8, 0.156), 100, 5000, 5000)
    end = time.time()
    print("Elapsed %f, sec" % (end - begin))
    # Elapsed 139.403984 sec


if __name__ == "__main__":
    main()
