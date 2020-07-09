from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
        ('userprofilebrawler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilebrawler',
            name='equipments',
            field=models.ManyToManyField(to='equipment.Equipment'),
        ),
    ]
