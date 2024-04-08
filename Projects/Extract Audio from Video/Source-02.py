import moviepy
import moviepy.editor as mvd

# Visual
import tkinter
from tkinter.filedialog import asksaveasfilename, askopenfilename

# Create a fnciton to open video file 
def fileopen():
    global open_file
    open_file = askopenfilename(filetypes=[("All files","*.*")])
    if not open_file :
        return open_path.insert(0, open_file)
    
# Create a function to save the audio file
def filesave():
    global save_file
    save_file = (asksaveasfilename(filetypes=[("audio file", '*.MP3'),("All files", '*.*')]) + ".mp3")
    if not save_file :
        return open_path.insert(0, save_file)
    
# Create a converter function
def fileconvert(video_file,audio_file):
    video = mvd.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file)
    popwid = tkinter.Toplevel()
    popwid.title("Successfully Compeleted")
    popwidtxt = tkinter.Label(popwid, text="sucessfully converted and saved to your location",height=10).pack(side=tkinter.TOP,anchor='nw')
    popwid.mainloop()
    

# Now main root
root = tkinter.Tk()
root.title("Audio Extracter")
frame = tkinter.Frame(root, height=20,width=80).pack(side=tkinter.TOP, fill=tkinter.BOTH)
open_label = tkinter.Label(frame, text="enter the path of the video file to be converted:").pack(side=tkinter.TOP ,anchor='w')
open_path = tkinter.Entry(frame, width=50)  # Entry for video file path.
open_path.pack(side=tkinter.TOP, fill=tkinter.BOTH)
open_Button = tkinter.Button(frame, text="Browse..",bg="sky Blue",command = lambda:fileopen()).pack(side=tkinter.TOP, anchor='e')  # Button to locate video file.
empty_space = tkinter.Label(frame, height=3).pack(side=tkinter.TOP,fill=tkinter.BOTH)  # Empty Label for good look.
save_label = tkinter.Label(frame, text="enter the path for the converted audio file to be saved:",height=1).pack(side=tkinter.TOP ,anchor='w')
save_path = tkinter.Entry(frame, width=50)   # Entry for audio file path.
save_path.pack(side=tkinter.TOP, fill=tkinter.BOTH)
save_button = tkinter.Button(frame, text="Browse..",bg="sky Blue", command=lambda:filesave()).pack(side=tkinter.TOP, anchor='e')  # Button to locate audio file to be saved.
empty_space2 = tkinter.Label(root, text="______________________________________________________________________",height=2,fg="green")
empty_space2.pack(side=tkinter.TOP,fill=tkinter.BOTH,anchor='s')   # Empty Label for good look.
second_frame = tkinter.Frame(root,width=100).pack(side=tkinter.TOP)   # A second frame which holds cancel and convert Buttons.
convert_button = tkinter.Button(second_frame, text="convert",bg="pink",borderwidth=4,command=lambda:[fileconvert(open_file,save_file)])
convert_button.pack(side=tkinter.RIGHT, anchor='ne', padx=5,pady=5)  # The convert Button.
# cancel Button.
cancel_Button = tkinter.Button(second_frame, text="cancel",bg="pink",borderwidth=4,command=lambda:root.destroy()).pack(side=tkinter.RIGHT, anchor='ne',padx=5, pady=5)
root.mainloop()