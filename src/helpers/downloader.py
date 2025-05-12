import requests
from pathlib import Path

def download_to_local(url:str, out_path:Path, parent_mkdir:bool=True):
    
    """
    Downloads a file from a given URL and saves it to the specified local path.
    
    Args:
        url (str): The URL of the file to download.
        out_path (Path): The local path where the file will be saved.
    """
    if not isinstance(out_path, Path):
        raise ValueError(f"{out_path} must be a valid pathlib.Path object")
    if parent_mkdir:
        out_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Write the file out in binary mode to prevent any newline conversions
        out_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f'Failed to download {url}: {e}')
        return False

