#What is your terminal display "path"? (type/paste as text into the .py file)
# @J-CYN ➜ /workspaces/daytwostuff (main) $

#Should you include the environment in your repo or not?
# No, as the environment will differ depending on the person's system, and can easily be recreated. It is better to not include it in the repo to allow others to create their own which is created with their device and OS in mind.

#Now what is your terminal display "path"? Is it different?
# (.venv) (base) @J-CYN ➜ /workspaces/daytwostuff (main) $

#What do you notice about the extension menu?
# There is a local installed section and a codespaces install section that are separate and include different extensions

#What are three useful elements of Data Wrangler?
#It shows the number of missing info in each column, gives simple count graphs for certain columns, and shows distinct variables for others.

#Why do we use a requirements.txt file?
#It allows others to be able to use the same libraries and versions of those libraries as us when they make their own virtual environment. It also allows for easy and quick downloads.

import numpy as np
import pandas as pd

df=pd.read_csv("Runways.csv")

print(df)

# Step by step recipe for creating a new working project environment

# First create a new repo inside your github
# Second click on the code button on the top right of the repository
# Third press "Create codespace on main"
# This will open another tab with a virtual environment for your VScode, however, you can run it locally too using the extension as mentioned above.
# To access on your local VS Code. In this tabbed virtual environment, click on the three bars on the top left. Select "Open in VS Code Desktop"
# Now, we can create a requirements.txt file. Put all the libraries we think we will need in there.
# Final step, create a virtual environment. On the linux virtual machine, which is the machine I'm using, the commands to input are "python3 -m venv .venv" for initializing it, "source .venv/bin/activate" for activating it, and "pip install -r requirements.txt" for downloading the requirement.txt libraries within it. All of these bash lines are typed into the terminal below accessed by the buttons to the left of the minimize button in VS Code.
# After this, you've accomplished the first steps. Feel free to create new packages, load in data, or analyze data, but otherwise that's a step by step to get to this point. So whoooooo!


