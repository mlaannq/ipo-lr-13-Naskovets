from PIL import Image, ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_filter(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.EMBOSS)
            print(f"Фильтр эмбосс применен")

        else:
            print("Нет изображения для обработки")
    #водяной знак
    def add_watermark(self, text="Вариант 5"):
        if self.image:
            draw = ImageDraw.Draw(self.image)
            font_size = max(20, min(self.image.size) // 20)
            font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", font_size)

            text_width = draw.textlength(text, font=font)
            text_height = font_size
            position = (self.image.size[0] - text_width - 10, self.image.size[1] - text_height - 10)

            watermark = Image.new("RGBA", self.image.size, (0, 0, 0, 0))
            watermark_draw = ImageDraw.Draw(watermark)
            watermark_draw.text(position, text, font=font, fill=(255, 255, 255, 128))
            self.image = Image.alpha_composite(self.image.convert("RGBA"), watermark)
            print(f"Водяной знак '{text}' добавлен в правый нижний угол.")
        else:
            print("Нет изображения для обработки")
    #отображает изображение
    def show_image(self):
        if self.image:
            self.image.show()
        else:
            print("Нет изображения для отображения")

    def get_image(self):
        return self.image