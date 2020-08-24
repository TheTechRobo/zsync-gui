"""
Zsync-Curl-GUI
by: TheTechRobo
License: Dbad-Clean (http://github.com/thetechrobo/dbad-clean)
"""
from tkinter import *
import tkinter.filedialog as filedialog
import tkinter.messagebox as m

def chooseFile():
    print('getting filename')
    filename =  filedialog.askopenfilename(initialdir="/", title="Select input file",filetypes = (("all files","*.*"), ("all files", "*.*")))
    print("got filename")
    if filename == "":
        return
    return filename
def inputFileWrapper():
    global inputFilename
    inputFilename = chooseFile()
def outputFile():
    global outputFilename
    outputFilename = filedialog.asksaveasfilename(initialdir="/", title="Save as output file", filetypes=(("all files","*.*"), ("all files", "*.*")))
    if outputFilename == "":
        del outputFilename
        return
def ok():
    if not m.askyesno("AGGREMENT", "I have read and agree to the EULA."):
        import sys
        sys.exit(1)
    url = w.get()
    import subprocess
    try:
        subprocess.Popen(["zsync_curl", "-u", url, "-i", inputFile, "-o", outputFile], shell=False)
    except Exception as ename:
        m.showerror("ERROR","There was an error running zsync_curl. Is it installed?  (%s)")
        import sys;sys.exit(1)
    m.showinfo("Success!","Success!")
    import sys;sys.exit()
main = Tk()

Button(main, text="Select Input File", command=inputFileWrapper).pack()
Button(main, text="Select Output File", command=outputFile).pack()
Label(main, text="Select URL: ").pack(side=LEFT)
w = Entry(main)
w.pack(side=LEFT)
Button(main, text="OK",command=ok).pack()
mainloop()
