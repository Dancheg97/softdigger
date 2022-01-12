# git clone

[Git clone](https://git-scm.com/docs/git-clone) - это команда использующаяся для клонирования репозитория из определенного источника. В качестве источника может использоваться например ссылка на GitHub репозиторий.

Может использоваться как альтернатива git init если есть желание начать работать с уже существующим проектом.


---

Минимальный пример:

```bash
git clone git://git.kernel.org/pub/scm/.../linux.git my-linux
```

---

Параметры:

```bash
git clone [--template=<template_directory>]
    [-l] [-s] [--no-hardlinks] [-q] [-n] [--bare] [--mirror]
    [-o <name>] [-b <name>] [-u <upload-pack>] [--reference <repository>]
    [--dissociate] [--separate-git-dir <git dir>]
    [--depth <depth>] [--[no-]single-branch] [--no-tags]
    [--recurse-submodules[=<pathspec>]] [--[no-]shallow-submodules]
    [--[no-]remote-submodules] [--jobs <n>] [--sparse] [--[no-]reject-shallow]
    [--filter=<filter>] [--] <repository>
    [<directory>]
```
