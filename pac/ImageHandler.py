from PIL import Image
from datetime import datetime

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
    #загрузка изображения
    def load_image(self):
        self.image = Image.open(self.image_path)
        print(f"Изображение успешно загружено: {self.image_path}")
    #сохранение изображения
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
    #масштабируем изображение до 50%
    def scale_image_50_percent(self):
        if self.image:
            original_size = self.image.size
            new_size = (original_size[0] // 2, original_size[1] // 2)
            self.image = self.image.resize(new_size)
            print(f"Изображение масштабировано до 50%: новый размер {new_size}")
        else:
            print("Сначала загрузите изображение")
    #изображение с текущей датой в имени файла
    def save_image_with_date(self, output_path_prefix, format=None):
        if self.image:
            date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_path = f"{output_path_prefix}_{date_str}.jpg"
            self.image.save(output_path, format=format)
            print(f"Изображение сохранено как: {output_path}")
        else:
            print("Сначала загрузите изображение")
    #получение копии изображения
    def get_image_for_processing(self):
        if self.image:
            return self.image.copy()
        else:
            print("Сначала загрузите изображение")
            return None