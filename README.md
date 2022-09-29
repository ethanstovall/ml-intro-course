## Setup for Virtual Environment
**Note: There are a few images in the images folder that you may find helpful, and they should be appropriately titled for what they
show. I'd only look there if you encounter any hiccups in this README. You will not need to do what's shown in a couple of them.
Also, in pip_install_reqs.PNG, the file name for you will be `requirements_latest.txt`, not
`requirements2.txt`.**
1. Install [Python 3.8.5](https://www.python.org/downloads/release/python-385/)
   - Download and run the file Windows x86-64 executable installer
   - I'd recommend adding Python to your PATH.
2. Create your virtual environment.
   - Open your command prompt and navigate to an environments directory outside of your project. This can be anywhere, named anything.
     It is just better to make sure your packages aren't included in the project directory in case you want to zip and send it, or
     push it to a remote repository. I used C:/Users/<my_username>/py3_envs.
   - Enter the command `python -m venv cs229_env`
   - This creates a new virtual environment named `cs229_env` for your project in that directory.
3. Navigate to the directory `<your_envs_dir_path>/cs229_env/Scripts` in the command Prompt.
   - Enter `activate` to start the virtual environment.
3. Install the packages for the project with pip (while your venv is activated).
   - Note that`requirements_latest_full.txt` includes the packages to work on the entire proposed ML project, the second part of which is based loosely on [this article](https://medium.com/swlh/end-to-end-machine-learning-from-data-collection-to-deployment-ce74f51ca203)
   - I don't plan to further develop the second part of the project, so I recommend just using `requirements_latest.txt`,
     which just includes the packages you'll need to try out the algorithms in the notes.
   - Navigate to the `/.../Stanford_CS229_CrashCourse/src/` folder.
   - Run the command `pip install -r requirements_latest.txt` to install all the necessary packages.
   - Enter `deactivate` to deactivate the environment.
4. PyCharm Setup
   - [Pycharm link](https://www.jetbrains.com/pycharm/download/#section=windows)
   - Open the Stanford_CS229_CrashCourse folder in PyCharm.
   - Go to `File` > `Settings` > `Project` > `Project interpreter`
   - Click the gear in the top-right corner, then `Add`
   - Select `venv environment` > `Existing environment` > Button on the right with `…`
   - Add a new environment by navigating to your `aces_ml_env` in the file browser that appears.  
   - Select the python file at `/.../Stanford_CS229_CrashCourse/aces_ml_env/Scripts/python.`
   - Select `OK` then `Apply`
   - This will allow your project to automatically use your virtual environment within PyCharm.
5. Jupyter Lab
   - This is probably going to be the most convenient way for you to work with these large sets of data without needing to rerun an entire
     program each time. Code is executed in cells that you determine so that you can, for instance, load a dataset,
     and then execute and change the following code without having to reload it.
   - Navigate to the directory `<your_envs_dir_path>/cs229_env/Scripts` in the command Prompt.
   - Enter `activate` to start the virtual environment.
   - Then, while in the folder `Stanford_CS229_CrashCourse`, enter `jupyter lab` and it should open jupyter lab in your browser with the contents of `Stanford_CS229_CrashCourse`.
   - You should see several jupyter notebook files I've saved there. After reading `crash_course_notes.pdf`, take a look at them to see some of the data 
     manipulation and algorithms you can try. The notebooks all have the file type `.ipynb`.