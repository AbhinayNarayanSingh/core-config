from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.text import slugify

from user.models import User




class Posts(models.Model):

    banner = models.URLField(_("Image"), max_length=2000)
    title = models.CharField(_("Title"), max_length=500)
    sub_title = models.CharField(_("Sub-title"), max_length=500)
    discription = models.TextField(_("Short discription"))
    content = models.TextField(_("Content"))

    createdAt = models.DateTimeField(_("Created at"), auto_now_add=True)
    updatedAt = models.DateTimeField(_("Updated at"), auto_now=True)

    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)

    slug = models.SlugField( max_length=500, blank=True, null=True)


    class Meta:
        verbose_name = _("posts")
        verbose_name_plural = _("posts")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        return super(Posts, self).save( *args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts", kwargs={"pk": self.pk})


class Tags(models.Model):

    name = models.CharField(_("Tag"), max_length=100)    
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("tags")
        verbose_name_plural = _("tags")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tags", kwargs={"pk": self.pk})



class Likes(models.Model):

    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("likes")
        verbose_name_plural = _("likes")

    def __str__(self):
        return f"{self.user} - {self.post}"

    def get_absolute_url(self):
        return reverse("likes", kwargs={"pk": self.pk})



class Comments(models.Model):

    name=models.CharField(_("Comment"), max_length=500)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("comments")
        verbose_name_plural = _("comments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("comments", kwargs={"pk": self.pk})
