from django.db import models


# Create your models here.
class Notice(models.Model):
    """
    Model representing the notice.

    Fields:
    - title: CharField for the title of the notice.
    - content: Textfield for the contents of the notice
    - created_at: DateTimeField for the date a notice is created and posted
    - author: ForeignKey to associate a notice with it's author.

    Methods: - __str__: Returns a string representation of the title of the
        notice.

    :param models.Model: Django's base model class.
    """
    title = models.CharField(max_length=225)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Define a foreignKey for the author's relationship
    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, null=True, blank=True
    )

    # indented. may need to remove indent
    def __str__(self):
        return self.title


class Author(models.Model):
    """
    Model representing the author of a notice in notice board.

    Fields:
    - name: CharField for the author's name.

    Methods: - __str__: Returns a string representation of the author, showing
    the name.

    :param models.Model: Django's base model class.
    """

    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name
