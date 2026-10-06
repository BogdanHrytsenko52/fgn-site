from django.db import models
from django.utils import timezone


class Department(models.Model):
    name = models.CharField("Назва", max_length=200)
    head = models.CharField("Завідувач кафедри", max_length=200)

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField("Назва", max_length=200)
    code = models.CharField("Код", max_length=50)
    description = models.TextField("Опис", blank=True)
    coordinator_name = models.CharField(
        "Імʼя координатора набору", max_length=200, blank=True
    )
    coordinator_contact = models.CharField(
        "Контакт координатора набору", max_length=200, blank=True
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="programs",
        verbose_name="Випускова кафедра",
    )
    subjects = models.TextField(
        "Список дисциплін", blank=True, help_text="По одній на рядок"
    )

    class Meta:
        verbose_name = "Спеціальність"
        verbose_name_plural = "Спеціальності"
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} {self.name}"

    def subjects_list(self):
        """Return subjects as a list, splitting by newlines."""
        return [s.strip() for s in self.subjects.splitlines() if s.strip()]


class Teacher(models.Model):
    name = models.CharField("Імʼя", max_length=200)
    position = models.CharField("Посада", max_length=200, blank=True)
    degree = models.CharField("Науковий ступінь", max_length=200, blank=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="teachers",
        verbose_name="Кафедра",
    )

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"
        ordering = ["name"]

    def __str__(self):
        return self.name


class HomePage(models.Model):
    title = models.CharField("Заголовок", max_length=200, default="Ласкаво просимо")
    description = models.TextField("Опис факультету")
    contacts = models.TextField("Контакти", blank=True)

    class Meta:
        verbose_name = "Головна сторінка"
        verbose_name_plural = "Головна сторінка"

    def __str__(self):
        return self.title


class Exchange(models.Model):
    university = models.CharField("Університет", max_length=300)
    country = models.CharField("Країна", max_length=150, blank=True)
    languages = models.CharField("Мови навчання", max_length=300)
    places = models.IntegerField("Кількість місць")
    deadline = models.DateField("Дедлайн подачі")
    description = models.TextField("Опис", blank=True)

    class Meta:
        verbose_name = "Програма обміну"
        verbose_name_plural = "Програми обміну"
        ordering = ["deadline"]

    def __str__(self):
        if self.country:
            return f"{self.university} ({self.country})"
        return self.university

    @property
    def is_open(self):
        return self.deadline >= timezone.localdate()

    @property
    def status(self):
        if self.is_open:
            return "Прийом триває"
        return "Прийом завершено"
