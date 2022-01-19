# FileSplitter
You can use this little script to upload files of unlimited size to [github.com](https://github.com/)  
Just use this template directory and clone it locally  
Then copy your big files to directory named `source` and run `split.py`  
This will generate directory named `splitted` and that will contain all your files splitted by size of 980Mb  
You must tell git to ignore the `source` directory by adding source to `.gitignore`, I already did that  
Then you create a commit and upload your directory  
  
When somebody (probably you) downloads your repository, they must run `combine.py` to combine the files back together, the combined files will be located in directory named `source` (created if needed)  
