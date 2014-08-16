import markdown

from django.db      import models
from django.conf    import settings

def markdown_to_html(markdownText, imagelist):
    image_ref = ""

    for image in imagelist:
        image_ref += "\n[%s]: %s" % (image, image.phile.url)

    md = "%s\n%s" % (markdownText, image_ref)
    return markdown.markdown(md)


class Asset(models.Model):
    uploaded = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300)
    phile = models.FileField(upload_to="assets/")

    def __unicode__(self):
        return self.name


class Post(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    head = models.CharField(max_length=300)
    body = models.TextField()
    assets = models.ManyToManyField(Asset, blank=True)

    def __unicode__(self):
        return self.head

    def as_html(self):
        return markdown_to_html(self.body, self.assets.all())


class Event(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=300)
    info = models.TextField()
    assets = models.ManyToManyField(Asset, blank=True)
    
    def __unicode__(self):
        return self.name

    def as_html(self):
        return markdown_to_html(self.info, self.assets.all())


class AboutStatement(models.Model):
    updated = models.DateTimeField(auto_now=True)
    statement = models.TextField()
    assets = models.ManyToManyField(Asset, blank=True)

    def __unicode__(self):
        return unicode(self.updated)

    def as_html(self):
        return markdown_to_html(self.statement, self.assets.all())
