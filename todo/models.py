from django.db import models

# Create your models here.


class Todolist(models.Model):
    content = models.CharField(blank=False, null=False, max_length=255)
    is_completed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)    # auto_now_add = add time
    update_at = models.DateTimeField(auto_now=True)    #

    def __unicode__(self):
        return 'Item: Content {}: IsCompleted {}'.format(
            self.content,
            self.is_completed,
        )
    class Meta:
        ordering = ('is_completed', '-update_at')    # class Meta会自动更改html中的meta样式，这里写的是ordering，是排序，根据is_completed排序，以及根据update_at逆序排序。


