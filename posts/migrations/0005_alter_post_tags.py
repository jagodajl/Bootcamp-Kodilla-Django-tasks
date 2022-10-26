from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0004_tag_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='posts.tag'),
        ),
    ]
