from PerformanceMonitoring.processor import Processor


def main():
    proc = Processor()
    x = 0
    # Loop to keep  the collection of processes continuing.
    while x < 500:
        proc.process()
        x += 1

    proc.save()


if __name__ == '__main__':
    main()
