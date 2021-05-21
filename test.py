#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import tkinter as tk

import tkicon


def main():
    ui = tk.Tk()
    ui.title('Hello World')
    tkicon.use(ui.iconbitmap)
    ui.mainloop()


if __name__ == '__main__':
    main()
