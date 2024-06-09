import argparse
from PIL import Image

def rgb_to_ansi(r, g, b):
    """
    ansi ex: \033[48;2;0;0;255m
    - \033 告訴它你是在用ansi OCT
    - 38 前景色
    - 2 24位色彩
    - R (0~255) 紅色
    - G(0~255) 綠色
    - B(0~255) 藍色
    - m 結束轉義
    """
    return f"\033[38;2;{r};{g};{b}m"

def image_to_ascii(path, out_width=100, character_set=None):
    if character_set is None:
        # 可自訂義
        character_set = "@%#WMN8B@WMmamwoc=;:-,. "
    
    char_len = len(character_set)
    # 確保path安全
    image_path = path.replace("\\", "/")
    # RGB
    img = Image.open(image_path).convert("RGB")
    width, height = img.size
    ratio = height / width
    out_height = int(out_width * ratio * 0.55)
    img = img.resize((out_width, out_height), Image.LANCZOS)

    pixels = list(img.getdata())
    # 將灰度值轉換為字符
    grayscale_characters = [character_set[(r + g + b) // 3 * (char_len - 1) // 255] for (r, g, b) in pixels]
    ascii_image = [grayscale_characters[index: index + out_width] for index in range(0, len(grayscale_characters), out_width)]
    
    for y, row in enumerate(ascii_image):
        for x, char in enumerate(row):
            r, g, b = img.getpixel((x, y))
            print(f"{rgb_to_ansi(r, g, b)}{char}", end="")
        print("\033[0m")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an image to an ASCII art representation.")
    parser.add_argument("path", type=str, help="The path to the image file.")
    parser.add_argument("--width", type=int, default=100, help="The output width of the ASCII art (default: 100).")
    parser.add_argument("--characters", type=str, default="@%#WMN8B@WMmamwoc=;:-,. ", help="The set of characters to use for ASCII art (default: '@%#WMN8B@WMmamwoc=;:-,. ').")

    args = parser.parse_args()
    
    image_to_ascii(args.path, args.width, args.characters)
