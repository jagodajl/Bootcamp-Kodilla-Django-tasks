from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0005_alter_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='posts.tag'),
        ),
    ]
