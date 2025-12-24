from django.db import models


class CategoryProject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(
        CategoryProject,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', null=True, blank=True, default=None)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class CategoryPost(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(
        CategoryPost,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts'
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts/')
    content = models.TextField()

    def __str__(self):
        return self.title


class CategoryTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostTag(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        CategoryTag,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.post} - {self.tag}"

