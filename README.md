![preview](images/image.png)

Apparently A1111 can import webp pictures, so this was an exercise in futility. haha.

# What does it do?
Drag webp files from explorer into the gui and convert them to png. Supports multiple files at once.
Was made primarily for downloading images off of Reddit and using them in AUTOMATIC1111 for img2img-ing.
I'd eventually like to make an extension for A1111 with this in it, but that's a tomorrow project lol.

Requires ffmpeg and QtPy5, but the install should take care of that (hopefully lol)

# How to do.
Clone the repo
Install with ```pip install -r requirements.txt```
Run with ```python main.py```
Drag files into the gui.

Or if you're feeling spicy, just use the ```run.bat```. I think it works....

There might be a problem if you uncheck the "Automatically confirm overwrites", so probably just leave that checked. lol.

### This was made entirely with ChatGPT.
I "curated" the code, but I mostly just fed errors back into it until it worked.

The starting prompt I gave to ChatGPT was,
"can you write me a python script with a gui that has a window i can drag and drop webp pictures into from the windows file explorer? it will convert them to png using ffmpeg and put the new png in the same folder as the input image with the same name but "converted" at the end of it.
put your response in a code block."

It produced an error or two with the first bit of code and ChatGPT was used to debug it. Didn't save those additional prompts.
Yeah, I didn't capatalize anything in my prompt. Don't @ me.

If you think of something else it should have, let me know.
I had another version that let you select an entire directory but it was rather cumbersome. Dragging and dropping is easy peasy and works way better.