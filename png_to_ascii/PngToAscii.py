import requests
from PIL import Image
from io import BytesIO

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

def fetch_image(source):
    if source.startswith('http://') or source.startswith('https://'):
        response = requests.get(source)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            return img
        else:
            print("Failed to retrieve image")
            return None
    else:
        return Image.open(source)

def image_to_ascii(source, out_width=100, character_set=None):
    if character_set is None:
        # 可自訂義
        character_set = "@%#WMN8B@WMmamwoc=;:-,. "
    
    char_len = len(character_set)
    img = fetch_image(source)
    if img is None:
        return
    
    img = img.convert("RGB")
    width, height = img.size
    ratio = height / width
    out_height = int(out_width * ratio * 0.55)
    img = img.resize((out_width, out_height), Image.LANCZOS)

    pixels = list(img.getdata())
    grayscale_characters = [character_set[(r + g + b) // 3 * (char_len - 1) // 255] for (r, g, b) in pixels]
    ascii_image = [grayscale_characters[index: index + out_width] for index in range(0, len(grayscale_characters), out_width)]
    
    for y, row in enumerate(ascii_image):
        for x, char in enumerate(row):
            r, g, b = img.getpixel((x, y))
            print(f"{rgb_to_ansi(r, g, b)}{char}", end="")
        print("\033[0m")
