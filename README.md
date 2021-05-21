# tkicon
Fast change default icon of `tkinter export GUI` with one file!

## Usage
1. copy `tkicon.py` to your project dirs.
2. run `tkicon.py` with .ico file, the .ico data will write into the `tkicon.py` as a varible.
    > tkincon.py \<icofile\>
3. just import `tkicon.py`, without other dependencies.
    ```
    import tkicon
    
    ui = tk.Tk()
    tkicon.use(ui.iconbitmap)
    ```
