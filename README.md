# Toolkit for Windows

Command utility to get small things done. 

I had bunch of small programs doing this separately, so here is something clubbed into one as a CLI with the help Click.

### Setup

Clone repository

    git clone https://github.com/guywhogeek/toolkit.git

Create a virtual environment [Optional]

    virtualenv toolkit

Install requirements 

    pip install -r requirements.txt

Run `setup.py`

    pip install --editable .


### `help` command

```
(toolkit) PS E:\Project\toolkit> toolkit --help
Usage: toolkit [OPTIONS] COMMAND [ARGS]...

  The missing CLI utility from Windows

Options:
  --help  Show this message and exit.

Commands:
  hash   Create Hash String for a file.
  kill   Kill a running process.
  serve  Create a static server.
  task   List all running processes.
  wget   Download file through server.
```

### Features
1. File Hashing
2. View running processes
3. Kill running processes
4. Download file from host (`wget`)

