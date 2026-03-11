def print_c(text: str) -> None:
    """
    зrints to the console.
    фrgs:
        text (str): text to print.
    """
    print(text)
def write_f(file_path: str, text: str) -> None:
    """
    writes text to a file
    args:
        file_path (str): file path.
        text (str): text to write.
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)