from breezypythongui import EasyFrame
#
class ButtonDemo (EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.label = self.addLabel(text="Xin chào các bạn đến với lập trình GUI!",
                                   row = 0,
                                   column=0,
                                   columnspan=2,
                                   sticky="NSEW")
        #
        self.clearBtn = self.addButton(text="Xóa", row=1, column=0, command=self.clear)
        #
        self.restoreBtn = self.addButton(text="Hiển thị", row=1, column=1, state="disabled", command=self.restore)
        #
        self.setSize(500, 500)
        self.setTitle("Lập trình GUI")
        #
    def clear(self):
        self.label["text"] = ""
        self.clearBtn["state"] = "disabled"
        self.restoreBtn["state"] = "normal"
    #
    def restore(self):
        self.label["text"] = "Xin chào các bạn đến với lập trình GUI!"
        self.clearBtn["state"] = "normal"
        self.restoreBtn["state"] = "disabled"

def main():
    ButtonDemo().mainloop()

if __name__ == "__main__":
    main()