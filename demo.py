print("Test1")
print("Sometimese1")
from threading import Event

exit = Event()

def main():
    while not exit.is_set():
      # do_my_thing()
      print(1)
      exit.wait(1)

    print("All done!")
    # perform any cleanup here

def quit(signo, _frame):
    print("Interrupted by %d, shutting down" % signo)
    exit.set()

if __name__ == '__main__':

    import signal
    for sig in ('TERM','INT'):
        signal.signal(getattr(signal, 'SIG'+sig), quit);

    main()