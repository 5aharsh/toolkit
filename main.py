from modules.hash import Hash
from modules.tasks import Tasks
from modules.wget import WGet
from modules.server import Server
import click, os

@click.group()
def toolkit():
    '''
    The missing CLI utility from Windows
    '''
    pass


@toolkit.command()
@click.argument('filename', required=True, type=str)
@click.option('--type', help="Pick hashing type", default='MD5', type=click.Choice(['MD5', 'SHA1'], case_sensitive=False))
def hash(filename, type):
    '''
    Create Hash String for a file.\n
    Usage: toolkit hash FILENAME [OPTION]
    '''
    h = Hash(filename)
    if (type=='SHA1'):
        print(h.sha1_hash())
    else:
        print(h.md5_hash())


@toolkit.command()
@click.option("--summary", help="Show a short view of running processes", is_flag=True)
@click.option("--search", help="Search a running process by name or ID", type=str, default=False)
@click.option("--sort", help="Sort results by", type=click.Choice(['name', 'id', 'session', 'memory'], case_sensitive=False))
def task(summary, search, sort):
    '''
    List all running processes.\n
    Usage: toolkit task [OPTIONS]
    '''
    tasks = Tasks()
    if summary:
        tasks.short_view(search, sort)
    else:
        tasks.full_view(search, sort)

@toolkit.command()
@click.option('--id', help="Specify ID of process to be killed", default=False, required=False)
@click.option('--name', help="Specify name of process to be killed", default=False, required=False)
@click.option('--force', help="Forcefully kill the process", is_flag=True)
def kill(id, name, force):
    '''
    Kill a running process.\n
    Usage: toolkit kill [OPTIONS]
    '''
    is_forced = ' /F' if force==True else ''
    if id:
        os.system('taskkill{} /PID {}'.format(is_forced, id))
    elif name:
        os.system('taskkill{} /IM {}'.format(is_forced, name))
    else:
        click.echo('Task can\'t be completed. Missing process identifier')

@toolkit.command()
@click.argument('url', required=True, type=str)
@click.argument('name', required=False, type=str, default=False)
@click.option('--retries', help="No. of retries if connection fails", default=3, required=False)
def wget(url, name, retries):
    '''
    Download file on server.\n
    Usage: toolkit wget URL [FILENAME]
    '''
    download = WGet()
    name = url.split("/")[-1].replace("&", "").replace("\\", "").replace("?", "").replace("=", "") if name==False else name
    download.wget(url, name, retries)

@toolkit.command()
@click.option("--port", help="Port to run the server", type=int, default=8000)
def serve(port):
    '''
    Create a static server.\n
    Usage: toolkit serve [OPTIONS]
    '''
    server = Server()
    server.run(port)

if __name__=='__main__':
    toolkit()