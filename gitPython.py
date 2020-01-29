# this is the function library for git Python

import os
import git

os.chdir(r'C:\EE2020\afva_virttesting')
repo = git.Repo(os.getcwd())
repo = git.Repo(r'C:\EE2020\afva_virttesting')
repo = git.Repo(r'C:\EE2020\afva_virttesting\.git')

git.Repo.clone_from(r'C:\EE2020\afva_virttesting\.git' ,r'C:\EE2020\new_local_repo')

# all branches
repo.branches
repo.config_reader().get_value("user", "email")
repo.config_reader().get_value("user", "name")

# change to branch xxx
repo.git.checkout('branchname')

oCurrentBranch = repo.head.reference

# name of the master branch
print(oCurrentBranch.name)          # the same as
print(repo.head.reference.name)     

# message of the last commit
print(oCurrentBranch.commit.message)

# Name of the last commit author
print(oCurrentBranch.commit.author.name)

# get information from Remotes
print(repo.remotes.origin.name)
print(repo.remotes.origin.url)
repo.remotes.origin.pull()

# all branches from remotes
repo.remotes.origin.refs

oRemoteBranch = repo.remotes.origin.refs[0]

print(repo.remotes.origin.refs[0].name)
print(repo.remotes.origin.refs[0].commit.message)          # the same as
print(oRemoteBranch.name)



# to be tested
# repo.config_writer().set_value("user", "name", "myusername").release()
# repo.config_writer().set_value("user", "email", "myemail").release()


