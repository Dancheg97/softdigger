# git search

[Git grep](https://git-scm.com/docs/git-grep) - позволяет выполнить поиск на регулярках в системе контроля версий. Очень полезная команда которая позволяет найти как изменения по комментариям/тагам так и по изменениям в файлах.


---

Пример:
```bash
git grep "mes"
```

---

Параметры:

```bash
git grep [-a | --text] [-I] [--textconv] [-i | --ignore-case] [-w | --word-regexp]
	   [-v | --invert-match] [-h|-H] [--full-name]
	   [-E | --extended-regexp] [-G | --basic-regexp]
	   [-P | --perl-regexp]
	   [-F | --fixed-strings] [-n | --line-number] [--column]
	   [-l | --files-with-matches] [-L | --files-without-match]
	   [(-O | --open-files-in-pager) [<pager>]]
	   [-z | --null]
	   [ -o | --only-matching ] [-c | --count] [--all-match] [-q | --quiet]
	   [--max-depth <depth>] [--[no-]recursive]
	   [--color[=<when>] | --no-color]
	   [--break] [--heading] [-p | --show-function]
	   [-A <post-context>] [-B <pre-context>] [-C <context>]
	   [-W | --function-context]
	   [--threads <num>]
	   [-f <file>] [-e] <pattern>
	   [--and|--or|--not|(|)|-e <pattern>…​]
	   [--recurse-submodules] [--parent-basename <basename>]
	   [ [--[no-]exclude-standard] [--cached | --no-index | --untracked] | <tree>…​]
	   [--] [<pathspec>…​]
```