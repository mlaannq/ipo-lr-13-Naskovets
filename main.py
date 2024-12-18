from PIL import Image
import datetime
import os

def menu():
    handler = None
    processor = None
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

        def show_image(self):
            if self.image:
                self.image.show()
            else:
                print("Нет изображения для отображения")

        def get_image(self):
            return self.image

    from PIL import Image
    from datetime import datetime

    class ImageHandler:
        def __init__(self, image_path):
            self.image_path = image_path
            self.image = None

        def load_image(self):
            self.image = Image.open(self.image_path)
            print(f"Изображение успешно загружено: {self.image_path}")

        def save_image(self, output_path, format=None):
            if self.image:
                self.image.save(output_path, format=format)
                print(f"Изображение сохранено как: {output_path}")
            else:
                print("Сначала загрузите изображение")

        def resize_image(self, new_size):
            if self.image:
                self.image = self.image.resize(new_size)
                print(f"Размер изображения изменен на: {new_size}")
            else:
                print("Сначала загрузите изображение")

        def scale_image_50_percent(self):
            if self.image:
                original_size = self.image.size
                new_size = (original_size[0] // 2, original_size[1] // 2)
                self.image = self.image.resize(new_size)
                print(f"Изображение масштабировано до 50%: новый размер {new_size}")
            else:
                print("Сначала загрузите изображение")

        def save_image_with_date(self, output_path_prefix, format=None):
            if self.image:
                date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                output_path = f"{output_path_prefix}_{date_str}.jpg"
                self.image.save(output_path, format=format)
                print(f"Изображение сохранено как: {output_path}")
            else:
                print("Сначала загрузите изображение")

        def get_image_for_processing(self):
            if self.image:
                return self.image.copy()
            else:
                print("Сначала загрузите изображение")
                return None
    #меню
    while True:
        decor = "=" * 22
        print(f"{decor} Выберите пункт из меню {decor}")
        print("1. Загрузить изображение")
        print("2. Масштабировать изображение до 50%")
        print("3. Сохранить изображение с текущей датой")
        print("4. Применить фильтр к изображению")
        print("5. Добавить водяной знак")
        print("6. Показать изображение")
        print("7. Сохранить обработанное изображение")
        print("8. Выйти из программы(")
        print(decor * 2)

        res = input("\nВыберите пункт из предложенного списка: ")

        if res == "1":
            image_path = input("Введите путь к изображению: ")
            handler = ImageHandler(image_path)
            handler.load_image()

        elif res == "2":
            if handler and handler.image:
                handler.scale_image_50_percent()
            else:
                print("Сначала загрузите изображение")

        elif res == "3":
            if handler and handler.image:
                output_prefix = input("Введите префикс для сохранения файла: ")
                handler.save_image_with_date(output_prefix)
            else:
                print("Сначала загрузите изображение")

        elif res == "4":
            if handler and handler.image:
                image_for_processing = handler.get_image_for_processing()
                if image_for_processing:
                    processor = ImageProcessor(image_for_processing)
                    processor.apply_filter()
            else:
                print("Сначала загрузите изображение")

        elif res == "5":
            if handler and handler.image:
                watermark_text = input(
                    "Введите текст водяного знака (по умолчанию текст: 'Вариант 5'): ").strip() or "Вариант 5"
                processor.add_watermark(watermark_text)
            else:
                print("Сначала загрузите изображение для обработки")

        elif res == "6":
            if processor and processor.image:
                processor.show_image()
            elif handler and handler.image:
                handler.image.show()
            else:
                print("Сначала загрузите изображение или обработайте его")

        elif res == "7":
            if handler and handler.image:
                save_path = input("Введите путь для сохранения обработанного изображения: ")
                processor.get_image().save(save_path)
                print(f"Изображение сохранено как: {save_path}")
            else:
                print("Сначала загрузите изображение для cохранения")


        elif res == "8":
            print("Выход из программы(")
            break

        else:
            print("Неправильный выбор, попробуйте снова")


if __name__ == "__main__":
    menu()