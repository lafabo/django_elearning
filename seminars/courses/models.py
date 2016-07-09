from django.db import models

# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    owner - models.ForeignKey(User, related_name='course_created')
    subject = models.ForeignKey(Subject, related_name='courses')
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(User, related_name="course_students")

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Module, related_name="contents")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    '''order = ....'''

    def __str__(self):
        return self.title   # self.order


class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='class_owner')
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    # def render
    # here will be something like return render_to_string(".... template ...")


# may be better to save all modules content to module_name directory?

class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()