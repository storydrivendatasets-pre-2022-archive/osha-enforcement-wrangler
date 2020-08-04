from pathlib import Path
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
