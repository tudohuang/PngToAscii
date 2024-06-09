from .PngToAscii import image_to_ascii

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m PngToAscii <path_to_image>")
    else:
        image_path = sys.argv[1]
        ascii_art = image_to_ascii(image_path)
        print(ascii_art)
