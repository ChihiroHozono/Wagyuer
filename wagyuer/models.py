from django.db import models


class WagyuPackageImg(models.Model):
    """和牛パッケージ写真(実際にはパス）を保存するテーブル"""

    img = models.ImageField(verbose_name="アップロード画像", upload_to="uploads/%Y/%m/%d/")