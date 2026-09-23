from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200,verbose_name='标题')

    content = models.TextField(verbose_name='详细内容')

    tag = models.CharField(max_length=50, verbose_name='标签', default='未分类')

    is_mastered = models.BooleanField(default=False, verbose_name='已掌握')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = '错题/知识点'
        verbose_name_plural = '错题/知识点'
        
