#Starting code bundle
Unfinished as of 02/03/2017.

TODO:  
-all the stuff in issues  
-generate physically accurate particles  
-improve reconstruction (finish creating modules first)  
-improve build_datasets.py  
-create a run.py that produces solutions given datasets?  

Overview of the project can be seen in README.ipynb

Generation - module containing event generation methods  
Reconstruction - module containing track reconstruction methods  
Analysis - ?

#Creating datasets
Currently in its infancy, build_datasets.py is a program that takes command line arguments to create datasets.  
Example run looks like this:  
yourshell$ python2.7 build_datasets.py --output-dir results --num-events 5 --hits-per-event 5000  
yourshell$ ls results/dataset_trackml/  
hits.csv        tracks.csv      tracks_soln.csv  

Feel free to modify it and add to it.

Please do not commit data files to the repo. 
Please add to your .gitignore:

*~
.*
*.csv
*.pyc
*.txt
*.zip



