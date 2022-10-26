from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('maths', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='math',
            options={'ordering': ['-id']},
        ),
    ]
