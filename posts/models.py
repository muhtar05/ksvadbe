from django.db import models
from django.template.defaultfilters import slugify

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # def save(self,*args,**kwargs):
    #     self.do_unique_slug()
    #     if not self.description:
    #         self.description = self.title
    #     super(Post,self).save(*args,**kwargs)
    #
    # def do_unique_slug(self):
    #     if not self.id:
    #         if not len(self.slug.strip()):
    #             self.slug = slugify(self.title)
    #
    #         self.slug = self.get_unique_slug(self.slug)
    #         return True
    #
    #     return False
    #
    # def get_unique_slug(self,slug):
    #     orig_slug = slug
    #     counter = 1
    #
    #     while True:
    #         posts = Post.objects.filter(slug=slug)
    #         if not posts.exists():
    #             return slug
    #
    #         slug = '%s-%s' % (orig_slug,counter)
    #         counter += 1


