from django.db import migrations

INSERT_SQL = """
INSERT INTO faculty_exchange (university, languages, places, deadline, description)
VALUES
('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15', 'Провідний польський університет з високими академічними стандартами та широким вибором курсів.'),
('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01', 'Один із найстаріших і найавторитетніших університетів Європи, розташований у Бельгії.'),
('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20', 'Найдавніший та найбільший вищий навчальний заклад Литви з активною міжнародною спільнотою.'),
('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15', 'Один із найстаріших університетів Центральної Європи з багатою академічною спадщиною.'),
('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10', 'Національний університет Естонії, відомий інноваційними дослідженнями та якісною освітою.'),
('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30', 'Сучасний чеський університет у місті Брно з динамічним академічним середовищем.');
"""

REVERSE_SQL = """
DELETE FROM faculty_exchange WHERE university IN (
    'Uniwersytet Warszawski, Польща',
    'KU Leuven (Бельгія)',
    'Vilnius University, Литва',
    'Uniwersytet Jagielloński, Польща',
    'University of Tartu - Естонія',
    'Masaryk University, Чехія'
);
"""

class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0003_exchange'),
    ]

    operations = [
        migrations.RunSQL(
            sql=INSERT_SQL,
            reverse_sql=REVERSE_SQL,
        ),
    ]
