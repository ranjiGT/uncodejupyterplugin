# UNCode JupyterHub plugin
A JupyterHub extension for submitting notebook files to UNCode. This project is a future work from [here](https://github.com/CSSPLICE/webcatjupyterplugin) which was originally designed for Jupyter Notebook. This respository is capable of having a front-end extension to JupyterHub. 

# Requirements

1. Python 3.5+
2. pip
3. JupyterHub

# Directions

## Linux / macOS

##### With Anaconda:
Follow these steps if you are running Jupyter Notebooks through Anaconda:

1. conda install git pip
2. pip install git+https://github.com/ranjiGT/uncodejupyterplugin
3. jupyter serverextension enable --py uncodejupyterplugin
4. jupyter nbextension install --user --py uncodejupyterplugin
5. jupyter nbextension enable --user --py uncodejupyterplugin
7. Download the file env.sh or clone the repository and run the command below
8. sh env.sh

You can skip the 7<sup>th</sup> and 8<sup>th</sup> steps and manually run the following commands:
1. jupyterhub --generate-config
2. Add the following line at the end of ~/.jupyter/jupyterhub_config.py
    - c.NotebookApp.disable_check_xsrf = True 
    
##### With pip:

If you are not using Anaconda, use the following commands:

1. pip3 install git+https://github.com/ranjiGT/uncodejupyterplugin
2. jupyter serverextension enable --py uncodejupyterplugin
3. jupyter nbextension install --user --py uncodejupyterplugin
4. jupyter nbextension enable --user --py uncodejupyterplugin
5. Download the file env.sh or clone the repository and run the command below
6. sh env.sh


You can skip the 5<sup>th</sup> and 6<sup>th</sup> steps and manually run the following commands:
1. jupyterhub --generate-config
2. Add the following line at the end of ~/.jupyter/jupyterhub_config.py
    - c.NotebookApp.disable_check_xsrf = True 
    
## Windows

If you have Windows operating system, follow these steps:

1. Install Anaconda
2. Open Anaconda Prompt and run these commands:
3. conda install git pip
4. pip install git+https://github.com/ranjiGT/uncodejupyterplugin
5. jupyter serverextension enable --py uncodejupyterplugin
6. jupyter nbextension install --user --py uncodejupyterplugin
7. jupyter nbextension enable --user --py uncodejupyterplugin
8. jupyterhub --generate-config

This will generate a default config file and you will get the output like "Writing default config to: C:\Users\UserName\\.jupyter\jupyterhub_config.py"

Run the following command but make sure to change the path to the ones returned by the above command

9. echo c.NotebookApp.disable_check_xsrf = True >> C:\Users\UserName\\.jupyter\jupyterhub_config.py



# Assignment Indentification

The UNCode assignment indetification parameters are fetched from the first cell. Paste the following comments in the first cell and change the values with your assignment parameters.

    # Do not edit this cell

    # course: 123
    # a: Assignment 1
    # d: HPI

# To uninstall this plugin

```
pip uninstall uncodejupyterplugin
```

# Screenshots

#### Submit to UNCode button on JupyterHub
!["Submit to UNCode button"](screens/submit_button.jpeg "Submit to UNCode button")

# References

```
@inproceedings{Manzoor2020,
   abstract = {Jupyter Notebooks are becoming more widely used, both for data science applications and as a convenient environment for learning Python. Currently, grading of assignments done in Jupyter Notebooks is typically done manually. Manual grading results in students receiving feedback only long after the assignment is complete. We implemented support for auto-grading programs written in Jupyter Notebooks within the Web-CAT auto-grading system. Scores received are directly reported to the Canvas gradebook. A Jupyter notebook extension allows students to upload their notebook files to Web-CAT directly. Survey results from class use show that 80% of students believe that getting immediate feedback from Web-CAT improved their performance. Instructors report that this implementation has significantly reduced their workload.},
   author = {Hamza Manzoor and Amit Naik and Clifford A. Shaffer and Chris North and Stephen H. Edwards},
   doi = {10.1145/3328778.3366947},
   isbn = {9781450367936},
   journal = {SIGCSE 2020 - Proceedings of the 51st ACM Technical Symposium on Computer Science Education},
   keywords = {Auto-grading,Jupyter notebooks,Learning tools interoperability,Python},
   month = {2},
   pages = {1139-1144},
   title = {Auto-grading jupyter notebooks},
   year = {2020},
}

```
