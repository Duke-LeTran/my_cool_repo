# I. Sync Local Repositories to github account

```{bash}
mkdir mycoolrepo # make a new local directory
cd mycoolrepo
vim myfile.txt # make a test file
```
## Set-up user profile, gitconfig
```{bash}
git config --global --edit
```

## Set-up GIT
```{bash}
git init
git status # check git status
git add myflie.txt # add the file
git commit -m "test, initial commit"
git commit --amend --reset-author # in case you need to reset author of commit
```

## Create corresponding git repository in cloud
* Now, you need to create a "cloud"
* IMPORTANT - it needs to be empty, do NOT add...
	* README
	* gitignore
	* license
	* etc

## Push from existing repository

```{bash}
git remote add origin git@github.com:Duke-LeTran/my_temp_repo.git
```

## Add the remote to your local git folder
* now add a remote
* call this remote repository "origin"
	* you can call this anything, 
	* a good practice is to call it"github, bitbucket, gitlab, etc"

```
git push -u origin master 
# the 'u' flag means it pushes everything, including tags, etc
#optional below, so you can just type 'git push'
# git push --set-upstream origin master
```


# II. Git Clone
```{bash}
git clone git@github.com:ucdavis-datalab-training/git_for_teams_fall_2019.git <name-of-new-folder>
```

# III. Branching
## GIT BRANCH
```{bash}
git branch # similar to git status, but for bracnhes
git checkout -b featureOne #created a new branch AND checkouts featureOne
```

* now try adding some files
```{bash}
vim charlie_chaplin.txt # add ascii art
subl floppy_disk.txt # add ascii art
```

* now try checkout the master to test

```{bash}
git checkout master # let's go to master branch
ls #check that new ascii art is not there
git checkout featureOne
```

## GIT MERGE
```{bash}
git checkout master
git merge featureOne # merge
 #
```

* very seldom should you delete a branch after
```{bash}
git branch -d featureOne
```
