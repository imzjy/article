Tracking others folk in Git
========

Our logic master repo is Hacker/master，Jerry and Lily folks this repo.

Someday，Lily added a new feature. Jerry want to tracking Lily’s changes, What do Jerry’s do?

### 1, fetch the changes from Lily

```shell
git remote add Lily [Lily’s repo address]
git fetch Lily
```

### 2, add a tracking branch named “track-Lily” to track the changes from Lily

```shell
git branch track-Lily –track Lily/master
```

### 3，switch working branch to “track-Lily”

```shell
git branch –a    #list all of branches
git checkout track-Lily     #switch the branch to Lily’s
```

After Jerry review the Lily’s code, then Jerry want to back to himself work, so:

### 4, switch back to Jerry’s branch

```shell
git checkout master
git branch -a
```
