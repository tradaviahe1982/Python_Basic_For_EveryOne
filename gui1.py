from breezypythongui import EasyFrame
class LebelDemo (EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text="Lập trình GUI với Python 3!", row=5, column=5)
        self.setSize(500, 500)
        self.setTitle("Lập trình GUI")
def main():
    LebelDemo().mainloop()

if __name__ == "__main__":
    main()
