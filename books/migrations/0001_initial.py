from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('lastname', models.CharField(max_length=20, unique=True)),
                ('nick', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('desctiption', models.TextField()),
                ('number_of_pages', models.IntegerField(max_length=5000)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateTimeField(auto_now=True)),
                ('is_returned', models.BooleanField()),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(related_name='books', to='books.tag'),
        ),
    ]