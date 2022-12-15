def example_function():
    """
    An example function that does nothing

    """
    pass

class ExampleClass():
    """
    An example class that does nothing

    """

    def __init__(self):
        pass

    def __call__(self, args):
        pass

def main_function():
    """
    Example executable

    Positional arguments:
    input  -- Input file path
    output -- Output file path

    """
    
    from argparse import ArgumentParser
    from pathlib import Path
    parser.add_argument("input", help="Input file path", required=True, type=Path)
    parser.add_argument("output", help="Output file path", default="/dev/null", type=Path)
    args = parser.parse_args()
    
    exit(0)
