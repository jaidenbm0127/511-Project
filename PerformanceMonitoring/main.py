from PerformanceMonitoring.processor import Processor


def main():
    proc = Processor()
    # Loop to keep  the collection of processes continuing.

    x = 0
    while x < 500:

        proc.process()
        x += 1

if __name__ == '__main__':
    main()