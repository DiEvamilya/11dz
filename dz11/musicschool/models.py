from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify



class Student(models.Model):
    INSTRUMENT_CHOICES = [('piano', 'piano'), ('violin', 'violin'), ('flute', 'flute'),
                          ('accordion', 'accordion'), ('harp', 'harp')]

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    course = models.PositiveIntegerField()
    instrument = models.CharField(max_length=255, choices=INSTRUMENT_CHOICES, null=True)
    average_grade = models.DecimalField(max_digits=2, decimal_places=1,
                                        validators=[MinValueValidator(1), MaxValueValidator(12)])
    payment = models.BooleanField(default=False, null=True, blank=True)
    slug = models.SlugField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.age}- {self.course} - {self.instrument} " \
               f"- {self.average_grade} - {self.payment} "

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.surname}-{self.course}-{self.instrument}')
        return super().save()



