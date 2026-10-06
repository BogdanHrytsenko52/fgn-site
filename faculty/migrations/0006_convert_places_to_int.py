import re
from django.db import migrations, models

def convert_places_to_int(apps, schema_editor):
    Exchange = apps.get_model('faculty', 'Exchange')
    for item in Exchange.objects.all():
        numbers = re.findall(r'\d+', str(item.places))
        item.places = numbers[0] if numbers else '0'
        item.save()

def reverse_places_to_int(apps, schema_editor):
    Exchange = apps.get_model('faculty', 'Exchange')
    for item in Exchange.objects.all():
        item.places = str(item.places)
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0005_split_university_country'),
    ]

    operations = [
        migrations.RunPython(
            code=convert_places_to_int,
            reverse_code=reverse_places_to_int,
        ),
        migrations.AlterField(
            model_name='exchange',
            name='places',
            field=models.IntegerField(),
        ),
    ]
