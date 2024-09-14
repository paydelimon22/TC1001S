# TC1001S
Herramientas Computacionales: el arte de la programación

## Requirements

- `freegames` module installable with `pip`.
- `turtle` module.

### Installing `freegames`

The `freegames` module can be installed using `pip`, python's package manager
by entering

```shell
pip install freegames
```

In this repo, we've included a `requirements.txt` that can be used to install
dependencies in case the number were to grow. This could then be used to
install all dependencies at once with

```shell
pip install -r requirements.txt
```

### Installing `turtle`

If your installation of python does not contain the `turtle` module, don't
try to install it with `pip`. Instead, your package manager should provide
a package with `tkinter` (the parent module of the `turtle` module). The
`tkinter` module is usually included in most installations of `python`, but it
is sometimes skipped to save space.

However, this is uncommon, and most users should have no problem running

```
python3

>>> import turtle
```

in their shell.
