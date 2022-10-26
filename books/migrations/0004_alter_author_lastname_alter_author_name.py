from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_desctiption_book_description_alter_book_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='lastname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]