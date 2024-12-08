from django.db import models


class status_choices(models.TextChoices):
    PUBLISHED = 'pub', 'Published'
    DRAFT = 'draft', 'Draft'
    COMING_SOON = 'coming_soon', 'Coming Soon'


class AccessChoices(models.TextChoices):
    ANY = 'any', 'Anyone'
    EMAIL_REQUIRED = 'email_required', 'Email Required'


def handleUpload(instance, fileName):
    return f'{fileName}'


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, upload_to=handleUpload)
    access = models.CharField(choices=AccessChoices,
                              default=AccessChoices.ANY, max_length=20)
    status = models.CharField(choices=status_choices, max_length=20,
                              default=status_choices.DRAFT)

    @property
    def is_published(self):
        return self.status == status_choices.PUBLISHED
