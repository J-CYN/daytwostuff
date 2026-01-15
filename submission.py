#What is your terminal display "path"? (type/paste as text into the .py file)
# @J-CYN ➜ /workspaces/daytwostuff (main) $

#Should you include the environment in your repo or not?
# No, as the environment will differ depending on the person's system, and can easily be recreated. It is better to not include it in the repo to allow others to create their own which is created with their device and OS in mind.

#Now what is your terminal display "path"? Is it different?
# (.venv) (base) @J-CYN ➜ /workspaces/daytwostuff (main) $

#What do you notice about the extension menu?
# There is a local installed section and a codespaces install section that are separate

#What are three useful elements of Data Wrangler?
#It shows the number of missing info in each column, gives simple count graphs for certain columns, and shows distinct variables for others.

#Why do we use a requirements.txt file?
#It allows others to be able to use the same libraries and versions of those libraries as us when they make their own virtual environment. It also allows for easy and quick downloads.

import numpy as np
import pandas as pd

df=pd.read_csv("Runways.csv")

print(df)


