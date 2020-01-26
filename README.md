# Silicon_package
**Package for Read all files from any directory** 
created by scipy library and os.
Consisting of 2 functions 

1. read function 
get type of file type you want to read and path
filetype by default is image and path is os.getcwd()
`    read(filetype="image",path=os.getcwd()):
`
filetype also can be` ['sound','voice','wav','mp3']` for .wavs
or` ['image','photo','picture']` for image
2. display function 
get the index of list you want to display by default 0
`display(index=0)`
