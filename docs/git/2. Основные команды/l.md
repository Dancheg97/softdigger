# git stash

[Git stash](https://git-scm.com/docs/git-stash) - одна из самых полезных git команд которая используется для сохранения изменений в 'изоляции'. Нужна в тех сценариях, когда работая в определенной ветке  необходимо быстро переключиться на работу в другой, и текущие изменения необходимо сохранить.


---

Пример:

```bash
git stash
```


---

Параметры:

```bash
git stash list [<log-options>]
git stash show [-u|--include-untracked|--only-untracked] [<diff-options>] [<stash>]
git stash drop [-q|--quiet] [<stash>]
git stash ( pop | apply ) [--index] [-q|--quiet] [<stash>]
git stash branch <branchname> [<stash>]
git stash [push [-p|--patch] [-k|--[no-]keep-index] [-q|--quiet]
	     [-u|--include-untracked] [-a|--all] [-m|--message <message>]
	     [--pathspec-from-file=<file> [--pathspec-file-nul]]
	     [--] [<pathspec>…​]]
git stash clear
git stash create [<message>]
git stash store [-m|--message <message>] [-q|--quiet] <commit>
```