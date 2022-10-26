from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_number_of_pages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='desctiption',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]