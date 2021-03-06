# git add

[Git add](https://git-scm.com/docs/git-add) - минимальная команда использующаяся для добавления файлов/папок в систему контроля версий. Как правило используется `git add .` (ps точка означает добавление всех файлов в текущей директории).


---

Минимальный пример:

```bash
git add .
```

---

Параметры:

```bash
git add [--verbose | -v] [--dry-run | -n] [--force | -f] [--interactive | -i] [--patch | -p]
	  [--edit | -e] [--[no-]all | --[no-]ignore-removal | [--update | -u]] [--sparse]
	  [--intent-to-add | -N] [--refresh] [--ignore-errors] [--ignore-missing] [--renormalize]
	  [--chmod=(+|-)x] [--pathspec-from-file=<file> [--pathspec-file-nul]]
	  [--] [<pathspec>…​]
```
