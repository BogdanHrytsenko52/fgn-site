import re
from django.db import migrations, models

def split_university_country(apps, schema_editor):
    Exchange = apps.get_model('faculty', 'Exchange')
    for item in Exchange.objects.all():
        raw = item.university.strip()
        # Masaryk University, Чехія / Uniwersytet Warszawski, Польща / Vilnius University, Литва / Uniwersytet Jagielloński, Польща
        if ', ' in raw:
            parts = raw.split(', ', 1)
            item.university = parts[0].strip()
            item.country = parts[1].strip()
        # University of Tartu - Естонія
        elif ' - ' in raw:
            parts = raw.split(' - ', 1)
            item.university = parts[0].strip()
            item.country = parts[1].strip()
        # KU Leuven (Бельгія)
        elif '(' in raw and ')' in raw:
            m = re.match(r'^(.*?)\s*\((.*?)\)$', raw)
            if m:
                item.university = m.group(1).strip()
                item.country = m.group(2).strip()
            else:
                item.country = ''
        else:
            item.country = ''
        item.save()

def reverse_split_university_country(apps, schema_editor):
    Exchange = apps.get_model('faculty', 'Exchange')
    for item in Exchange.objects.all():
        if item.country:
            # Reconstruct original combined representation
            if item.university == 'KU Leuven':
                item.university = f"{item.university} ({item.country})"
            elif item.university == 'University of Tartu':
                item.university = f"{item.university} - {item.country}"
            else:
                item.university = f"{item.university}, {item.country}"
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_seed_exchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchange',
            name='country',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.RunPython(
            code=split_university_country,
            reverse_code=reverse_split_university_country,
        ),
    ]
