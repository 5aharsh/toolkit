# Toolkit for Windows

Command utility to get small things done. 

I had bunch of small programs doing this separately, so here is something clubbed into one as a CLI with the help Click.

## Setup

Clone repository

    git clone https://github.com/guywhogeek/toolkit.git

Create a virtual environment [Optional]

    virtualenv toolkit

Install requirements 

    pip install -r requirements.txt

Run `setup.py`

    pip install --editable .


## Commands

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

### Hash Files

Create Hash String for a file.

    Usage: toolkit hash FILENAME [OPTION]

```
Options:
  --type [MD5|SHA1]  Pick hashing type
  --help             Show this message and exit.
```

### Tasks Explorer

List all running processes.

    Usage: toolkit task [OPTIONS]

```
Options:
  --summary                       Show a short view of running processes
  --search TEXT                   Search a running process by name or ID
  --sort [name|id|session|memory]
                                  Sort results by
  --help                          Show this message and exit.
```
### Kill Running Task

Kill a running process.

    Usage: toolkit kill [OPTIONS]

```
Options:
  --id TEXT    Specify ID of process to be killed
  --name TEXT  Specify name of process to be killed
  --force      Forcefully kill the process
  --help       Show this message and exit.
```

### Download File

Download file on server.

    Usage: toolkit wget URL [FILENAME]

```
Options:
  --retries INTEGER  No. of retries if connection fails
  --help             Show this message and exit.
```

### Run Static Server

Create a static server.

    Usage: toolkit serve [OPTIONS]

```
Options:
  --port INTEGER  Port to run the server
  --help          Show this message and exit.
```

## Features
1. File Hashing
2. View running processes
3. Kill running processes
4. Download file from host (`wget`)
5. Run a static web server

