from django.db import models

# Create your models here.

class Category(models.Model):
    """
    The Category model represents a blog post category (e.g. Science, Music, etc.).
    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    The Post model represents a blog post, which has a title, body, and creation date.
    """
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    The Comment model represents a comment on a blog post, which has an author, body, and creation date.
    """
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on {self.post}"