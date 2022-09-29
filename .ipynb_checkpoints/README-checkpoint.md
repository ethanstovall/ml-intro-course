## Setup for Virtual Environment
**Note: There are a few images in the images folder that you may find helpful, and they should be appropriately titled for what they
show. I'd only look there if you encounter any hiccups in this README. You will not need to do what's shown in a couple of them.
Also, in pip_install_reqs.PNG, the file name for you will be `requirements_latest.txt` (if not on the Raytheon network), not
`requirements2.txt`.**
1. Install [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
   - Download and run the file Windows x86-64 executable installer
   - I'd recommend adding Python to your PATH.
2. Create your virtual environment.
   - Open your command prompt and navigate to the src directory of the project.
   - Enter the command `python -m venv aces_ml_env`
   - This creates a new virtual environment named `aces_ml_env` for your project in the src directory.
3. Navigate to the directory `/.../ACES_ML_Project/src/aces_ml_env/Scripts` in the command Prompt.
   - Enter `activate` to start the virtual environment.
3. Install the packages for the project with pip (while your venv is activated).
   - Note that `requirements.txt` and `requirements_latest_full.txt` include the packages to work on the entire proposed ML project, the second part of which is based loosely on [this article](https://medium.com/swlh/end-to-end-machine-learning-from-data-collection-to-deployment-ce74f51ca203)
   - If you're on the Raytheon network, `requirements.txt` is the only one you'll be authorized to use. Package version
     conflicts will cause issues with installation, so I recommend working on a personal computer.
   - I don't plan to further develop the second part of the project, so I recommend just using `requirements_latest.txt`,
     which just includes the packages you'll need to try out the algorithms in the notes.
   - Navigate to the `/.../ACES_ML_Project/src/` folder.
   - Run the command `pip install -r requirements_latest.txt` to install all the necessary packages.
   - Enter `deactivate` in the `/.../ACES_ML_Project/src/aces_ml_env/Scripts` folder to deactivate the environment.
4. PyCharm Setup (can't be used on Raytheon network)
   - [Pycharm link](https://www.jetbrains.com/pycharm/download/#section=windows)
   - Open the ACES_ML_Project folder in PyCharm.
   - Go to `File` > `Settings` > `Project` > `Project interpreter`
   - Click the gear in the top-right corner, then `Add`
   - Select `venv environment` > `Existing environment` > Button on the right with `…`
   - Add a new environment by navigating to your `aces_ml_env` in the file browser that appears.  
   - Select the python file at `/.../ACES_ML_Project/aces_ml_env/Scripts/python.`
   - Select `OK` then `Apply`
   - This will allow your project to automatically use your virtual environment within PyCharm.
5. Jupyter Lab
   - This is probably going to be the most convenient way for you to work with these large sets of data without needing to rerun an entire
     program each time. Code is executed in cells that you determine so that you can, for instance, load a dataset,
     and then execute and change the following code without having to reload it.
   - Navigate to the directory `/.../aces_ml_env/Scripts` in the command Prompt.
   - Enter "activate" to start the virtual environment.
   - Then, while in the folder `ACES_ML_Project`, enter `jupyter lab` and it should open jupyter lab in your browser with the contents of `ACES_ML_Project`.
   - You should see several jupyter notebook files I've saved there. After reading `aces_ml_notes.pdf`, take a look at them to see some of the data 
     manipulation and algorithms you can try. The notebooks all have the file type `.ipynb`.