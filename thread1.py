from threading import Thread
#
class MyThread (Thread):
    def __init__(self, name):
        Thread.__init__(self, name=name)
    def run(self):
        print(self.getName())

def main():
    process = MyThread("Xin chào bạn Nguyễn Việt Anh")
    process.start()

if __name__ == "__main__":
    main()

