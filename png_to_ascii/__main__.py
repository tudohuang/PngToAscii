import argparse
from .PngToAscii import image_to_ascii  

def main():
    parser = argparse.ArgumentParser(description="Convert an image to an ASCII art representation.")
    parser.add_argument("path", type=str, help="The path to the image file.")
    parser.add_argument("--width", type=int, default=100, help="The output width of the ASCII art (default: 100).")
    parser.add_argument("--characters", type=str, default="@%#WMN8B@WMmamwoc=;:-,. ", help="The set of characters to use for ASCII art (default: '@%#WMN8B@WMmamwoc=;:-,. ').")

    args = parser.parse_args()
    
    image_to_ascii(args.path, args.width, args.characters)

if __name__ == "__main__":
    main()
