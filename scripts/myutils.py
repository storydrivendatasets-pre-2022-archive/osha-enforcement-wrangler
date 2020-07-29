from pathlib import Path
import requests
from rich.console import Console
from tqdm import tqdm

MYLOG_CONSOLE = Console()

def mylog(*args, label=None, color='cyan'):
    labtxt = f"[bold {color} on black]{label}:[/bold {color} on black] " if label else ""
    txt = "\n» ".join([str(a) for a in args])
    if len(args) > 1:
        txt += '\n///'
    MYLOG_CONSOLE.log(f'{labtxt}{txt}')

def myinfo(*args, label=None):
    xlab = f'INFO; {label}' if label else 'INFO'
    mylog(*args, label=xlab, color='yellow')


def mywarn(txt, label=None):
    xlab = f'WARNING; {label}' if label else 'WARNING'
    mylog(*args, label=xlab, color='red')



def existed_size(path):
    e = Path(path)
    if e.is_file():
        return e.stat().st_size
    else:
        return False


def fetch(url):
    """
    easy downloading function: provides progress bar
    https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests
    """
    resp = requests.get(url, stream=True)
    content_length = int(resp.headers.get('content-length', 0))
    blocksize = 1024
    progress_bar = tqdm(total=content_length, unit='iB', unit_scale=True)

    for datablock in resp.iter_content(blocksize):
        progress_bar.update(len(datablock))
        yield datablock
    progress_bar.close()


def fetch_and_save(url, destpath):
    xb = existed_size(destpath)
    purl = Path(url)
    if xb:
        mylog(f"{destpath}", f"{xb} bytes", label="Exists")
        mylog(purl.name, purl.parent, label="Skipping")
    else:
        mylog(purl.name, purl.parent, label="Downloading")
        resp = fetch(url)
        destpath.parent.mkdir(exist_ok=True, parents=True)
        with open(destpath, 'wb') as dest:
            for data in resp:
                dest.write(data)

        mylog(destpath, f"{existed_size(destpath)} bytes", label="Saved")




