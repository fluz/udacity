# Intro to Data Analysis

The main objective in this course is elaborate a way to collect the data and how to obtain relevant information about the data. 

How to create questions and how obtain the answers for these questions.

The all execution will be made using the anaconda environment, usefull to install all tools used in data analysis.

The instructions of how to obtain the data was extracted from Udacity.

## Running Python Locally
In this course, we'll assume you have the ability to run Python locally. Whether you already have Python installed on your computer or not, we recommend downloading and installing Anaconda. This is a scientific Python installation that comes with a lot of libraries and tools we'll be using in this course, some of which are otherwise very difficult to install.
### Anaconda
* Navigate to http://continuum.io/downloads in your browser.
* Download the Python 2.7 installer. Make sure you don't select Python 3.4, as the course will not be compatible with other versions of Python.
* On a PC, click the Windows icon and select "Windows 64-Bit Python 2.7 Graphical Installer". You can also select the 32-bit installer if you have a 32-bit machine.
* On Mac or Linux, follow the same process but select the appropriate installer for your platform.
* Run the installer and follow the instructions on the screen.
If you already have Anaconda, make sure it is up to date by opening your Command Prompt or terminal (see below for instructions) and running the commands:
```
conda update conda
conda update anaconda
```

Since Anaconda can take a few minutes to download and install, you'll be able to follow along in the next few videos and exercises without it. We recommend starting the process now so that once you need it, you'll be ready to go.

### IPython Notebook
IPython notebooks are a powerful tool for data analysts, allowing you to combine code, plots, output, and descriptions in one easily readable document. 

We've provided starter code for the videos in an IPython notebook, and we recommend following along there. Whenever Caroline runs some code, run the same code in your notebook, and complete the exercises in the marked places. We'll also provide a notebook at the end of the lesson that contains solutions to all the exercises.

If you haven't used IPython notebook before, you can use the provided tutorial notebook to get familiar with it. To do this:
* Download the tutorial notebook from the data directory;
* Open your Command Prompt (PC) or terminal (Mac or Linux)
* On a PC click the Start button and search for "Command Prompt".

Learn more about basic terminal commands.

Run the command `jupyter notebook ipython_notebook_tutorial.ipynb` in your terminal. Do not close your terminal or command prompt.
The notebook should open in your default web browser. Read through the notebook and follow the instructions in it.

You can follow this same process to open other notebooks, such as the starter code for this lesson.
### Data Files
The data files are downloaded in `data` directory.
The files we'll be using in this lesson are:
    * enrollments.csv;
    * daily_engagement.csv
    * project_submissions.csv.
daily_engagement_full.csv contains more detailed data than daily_engagement.csv, but it's a larger file (about 500 MB), so using this file is optional. (I put in a local directory).

You should also download and read table_descriptions.txt, which describes what data is present in each file (or table) and what columns are present. The data has been anonymized, and contains a random selection of Data Analyst Nanodegree students who had completed the first project at the time the data was collected, as well as a random selection of students who had not. 