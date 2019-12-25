Title: Learning to debug with Git
Tags: git, software, debug
Date: 2016-11-19 12:20
HeaderImage: https://i.imgur.com/lCZe9cs.jpg
HeaderImageCaption: src: pixabay.com
author: Naveen Karippai
Category: Software
Summary: Debugging defects with Git

### TL;DR:

Git, the stupid content tracker, provides us a couple of tools to debug the issues in our project. It could be easier to find the author of a specific line of code, or search for the changeset that introduced a bug in the project by leveraging on git tools.

![memegenerator](https://miro.medium.com/max/480/1*go7UVRBQXo1GEnCgTA9uYg.jpeg)
{.adjust-width}

src: memegenerator
{.caption}

### Bottom line:

* **git grep** command can be used to search for a string, or a regular expression in the working directory (project)

* **git blame** command can be used to find the author of a specific line of code, or the commit (SHA-1) that introduced it

* **git bisect** tool can be used to find out the commit that introduced the bug in the project

*Tip of the day*: run $ man git [command] on terminal to see the manual of a specific git command

### Quick introduction on Git:

Git, the stupid content tracker, is a fast and scalable distributed version control system that is designed to manage projects with efficiency. It is free and open sourced.

For this post, we will be using Git on the command line (terminal). As an alternative, you can either checkout built-in git GUI tools for commiting [git gui] and browsing [gitk], or third-party git GUI clients [git cola].


### git grep

**When?** you want to find a string, or a regular expression in any of the files in the working directory (project).

**Why?** It can be efficient and faster with git grep to search in the project when we are running a machine with low specs. Also, it avoids searching through gitignore-d files, by default.

**How?** we can execute $ git grep [string|RegExp] on terminal to return the list of tracked files in the working directory, that contains our search keyword.

*Example*: $ git grep 'downloadImages'

![zsh](https://miro.medium.com/max/769/1*Y3-iR9vyaP7q81OaXHVGUg.png)
{.adjust-width}

Terminal: Z shell on GNU Linux
{.caption}

**Bonus**: we could use option -n, --line-number to show the line number of matching lines of code. Also, using option -i, --ignore-case would ignore case differences between search keyword and file.

*Example*: $ git grep -in 'John Lennon'

**An aside**: we can search for a keyword in a specific file by setting its file path while running git grep command. [EDIT] That said, “grep” stands for Globally search with Regular Expression and Print.

*Example*: $ git grep 'John Lennon' Music/TheBeatles.txt

### git blame

**When?** you want to find the commit (SHA-1) that introduced the specific line of code that causes a bug in the project. Also, you want to find the name of the author for a specific line of code, to ask for more information, or to blame ;)

**Why?** It shows you the name of the author for a specific line of code, to ask for further information, or to blame. By getting commit (SHA-1) for a specific line of code, you can show the changeset that introduced it, for getting additional information.

Example: run $ git show #SHA-1 to show the commit

**How?** we can run $ git blame filePath/fileName to show the annotation of a specific file, with commit (SHA-1) of each line of code in it, and what person authored each commit.

![zsh](https://miro.medium.com/max/881/1*EEnC6VNgC0bG2y8fQw5zQA.png)
{.adjust-width}

Terminal: Z shell on GNU Linux
{.caption}

**Bonus**: we could use the simple shell script in the code snippet below, to show the names of all contributors on a specific file in the project, along with the information on number of lines contributed by each of them. This would help us to identify the first person to go for more information on a specific file in the project.

<script src="https://gist.github.com/NaveenKarippai/31103b3572916436e48ae687d923be85.js"></script>

*Example*: $ git contr filepath/filename

**An aside**: use option -L to limit the output of git blame to specific lines of code. And, use option -C to see where the sections of code originally came from. Basically, it tells us the original author and commit (SHA-1) regardless of the refactoring done afterwards.

*Example*: $ git blame -LC 10,15 filepath/filename

## git bisect

**When?** you want to find the git commit that introduced the bug on a project, which contains (let us say) 100+ commits. Also, you don’t know what file in the project contains the bug.

**Why?** git bisect is essentially a binary search over the git commit tree to identify the first “bad” commit. This is (obviously) efficient and faster than trying to find “bad” commit manually by checking-out git commits in random.

**How?**

1. we can run the command $ git bisect start to initiate with binary search mode on git to find a bug.

2. we need to tag a “good” commit (bug-free commit) from git commit history. Therefore, we should log the git commit history to find a “good” commit. But, let us set the option --oneline on git log command to see only the name (subject) of git commits. For example: $ git log --oneline. Then, find a “good” commit (SHA-1), and run $ git bisect good #SHA-1 to inform git about the “good” commit.

3. we need to find the “bad” commit (bug-present commit) for git to do binary search between “good” and “bad” commits, and thereby find the bug. Since the latest commit has the bug, usually it can be assigned as the “bad” commit. For an example: $ git bisect bad #SHA-1.

4. repeat (2) and (3) while git walks us through git commit history and tag “good”/“bad” commits.

5. when we have successfully found out the first “bad” commit (source of bug), we can exit the git binary search mode by executing $ git bisect reset.

**Bonus**: you can automate git bisect by writing unit tests that identifies the bug, and running them automatically. The code snippet below should do the trick.

<script src="https://gist.github.com/NaveenKarippai/b34f73bd81a70987c14fa4e7102818fb.js"></script>

**An aside**: we should only search for a single bug in the process of running git bisect. If we need to find multiple bugs, then run git bisect separately for each of the bugs. Also, to get further information, or inspect a “bad” commit, we can run $ git show #SHA-1.

**Summary**: A good knowledge on git tools can help developers to debug the code with ease. This would make life happier.

Happy coding!!

#### Reference: 

This article was originally published on [medium](https://medium.com/@naveenkarippai/learning-to-debug-with-git-20bf13318164)

### Bonus:

Are you new to Linux and wants to do Linux Command Line? Get my Udemy course on "Linux Command Line for Beginners" at a discount price (limited offer) by clicking [here](https://www.udemy.com/linux-command-line-for-beginners-42/learn/v4/?couponCode=YELLOW-ELEPHANT).
