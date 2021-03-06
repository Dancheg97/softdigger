# git config

[Git config](https://git-scm.com/docs/git-config) - это командка которая исопльзуется для назначения и получения конфигурационной информации. Как правило используется для утсновки имени/фамилии/email/ различных токенов для доступов и др.

---

Пример:

```bash
git config --global user.name "FIRST_NAME LAST_NAME"
```


---

Параметры:


```bash
git config [<file-option>] [--type=<type>] [--fixed-value] [--show-origin] [--show-scope] [-z|--null] name [value [value-pattern]]
git config [<file-option>] [--type=<type>] --add name value
git config [<file-option>] [--type=<type>] [--fixed-value] --replace-all name value [value-pattern]
git config [<file-option>] [--type=<type>] [--show-origin] [--show-scope] [-z|--null] [--fixed-value] --get name [value-pattern]
git config [<file-option>] [--type=<type>] [--show-origin] [--show-scope] [-z|--null] [--fixed-value] --get-all name [value-pattern]
git config [<file-option>] [--type=<type>] [--show-origin] [--show-scope] [-z|--null] [--fixed-value] [--name-only] --get-regexp name_regex [value-pattern]
git config [<file-option>] [--type=<type>] [-z|--null] --get-urlmatch name URL
git config [<file-option>] [--fixed-value] --unset name [value-pattern]
git config [<file-option>] [--fixed-value] --unset-all name [value-pattern]
git config [<file-option>] --rename-section old_name new_name
git config [<file-option>] --remove-section name
git config [<file-option>] [--show-origin] [--show-scope] [-z|--null] [--name-only] -l | --list
git config [<file-option>] --get-color name [default]
git config [<file-option>] --get-colorbool name [stdout-is-tty]
git config [<file-option>] -e | --edit
```
