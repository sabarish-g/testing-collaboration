# An attempt to mock some git functionalities and how projects would work.
## Step 1:
Create a main branch. Don't directly work here. The SDEs would work on the main which is basically deployed into prod.

## Step 2:
Clone the main repository
git clone <folder on the machine>
Create a new branch like: <yourname>_develop
git checkout -b <new_branch> 
git add
git commit -m "message"
git push -u origin <new_branch>

## Step 3:
Create a pull request for them to review.