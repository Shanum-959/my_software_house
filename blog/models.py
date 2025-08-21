from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='author_images/', blank=True, null=True)    
    author_bio = models.TextField(blank=True, null=True)

    category = models.CharField(max_length=100, default='Uncategorized') 
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # 'blog_detail' tumhare urls.py me blog detail ka URL name hona chahiye
        return reverse('blog:blog_detail', kwargs={'slug': self.slug})
    
class BlogSection(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='sections')
    heading_id = models.CharField(max_length=100, help_text="Used in <a href='#id'> and <h4 id='...'>")
    heading_title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.blog.title} - {self.heading_title}"

