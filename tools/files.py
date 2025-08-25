def create_file(content: str | bytes, path: str, mode: str = 'wt') -> dict:
    """Creates a file at the given path with the specified content.

    Args:
        content (str or bytes): Content to write to the file.
        path (str): Destination file path.
        mode (str): File mode (e.g., 'wt' for text, 'wb' for binary). Defaults to 'wt'.

    Returns:
        dict: {
            'success': True if written successfully, else False,
            'error': Error message string if failed, else None
        }
    """
    try:
        with open(path, mode) as f:
            f.write(content)
        return {"success": True, "error": None}
    except (OSError, TypeError, ValueError) as e:
        return {"success": False, "error": str(e)}


def read_text_file(path: str, mode: str = 'rt', encoding: str = 'utf-8') -> dict:
    """Reads the content of a text file.

    Args:
        path (str): Path to the file.
        mode (str): File mode, usually 'rt' for reading text. Defaults to 'rt'.
        encoding (str): Text encoding. Defaults to 'utf-8'.

    Returns:
        dict: {
            'success': True if read successfully, else False,
            'content': The file content as a string if successful, else None,
            'error': Error message string if failed, else None
        }
    """
    try:
        with open(path, mode, encoding=encoding) as f:
            content = f.read()
        return {"success": True, "content": content, "error": None}
    except (OSError, UnicodeDecodeError, ValueError) as e:
        return {"success": False, "content": None, "error": str(e)}