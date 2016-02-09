from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify as default_slugify

import datetime
import unidecode


class Question(models.Model):
    
    QUESTION_CHOICES = (
        (1, _('IDEA')),
        (2, _('CATALOGUE')),
        (3, _('PROJECT')),
    )
    
    question_text = models.CharField(_('question'),max_length=200)
    slug = models.SlugField(_('slug'), unique_for_date='pub_date', default='slug_text')
    #keywords = models.TextField(_('keywords'), null=True, blank=True)
    keywords = models.CharField(_('keywords'), null=True,max_length=100)
    pub_date = models.DateTimeField(_('date published'), auto_now_add=True)
    question_type = models.IntegerField(_('question Type'), choices=QUESTION_CHOICES, default=1)
    is_featured = models.BooleanField(_('is_featured'), default=False)
    likecount = models.PositiveIntegerField(default=0)
    
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = self.slugify(self.question_text)
        return super(Question, self).save(*args, **kwargs)
        
    def slugify(self, tag):
        tag = unidecode.unidecode(tag)
        slug = default_slugify(tag)
        return slug[:50]
        
        
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __unicode____(self):
        return self.choice_text