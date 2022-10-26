from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]