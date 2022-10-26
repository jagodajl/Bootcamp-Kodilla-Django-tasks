from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Math',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(choices=[('add', 'add'), ('sub', 'sub'), ('mul', 'mul'), ('div', 'div')],
                                               max_length=5)),
                ('a', models.IntegerField()),
                ('b', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(blank=True, null=True, unique=True)),
                ('error', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='result',
            constraint=models.CheckConstraint(
                check=models.Q(models.Q(('error__isnull', True), ('value__isnull', False)),
                               models.Q(('error__isnull', False), ('value__isnull', True)), _connector='OR'),
                name='maths_result_value_error_together'),
        ),
        migrations.AddField(
            model_name='math',
            name='result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='maths.result'),
        ),
    ]
