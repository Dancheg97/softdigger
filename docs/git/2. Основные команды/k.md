# git merge

[Git merge](https://git-scm.com/docs/git-merge) - команда которая используется для слияния определенных веток.

Есть ветка которая отдает, и есть ветка которая принимает. Изменения после слияния являются актуальными для принимающей ветки, а отдающая ветка сохраняется в истории.

---


Пример:
```bash
git merge feature3245
```

---

Параметры:

```bash
git merge [-n] [--stat] [--no-commit] [--squash] [--[no-]edit]
	[--no-verify] [-s <strategy>] [-X <strategy-option>] [-S[<keyid>]]
	[--[no-]allow-unrelated-histories]
	[--[no-]rerere-autoupdate] [-m <msg>] [-F <file>] [<commit>…​]
git merge (--continue | --abort | --quit)
```
