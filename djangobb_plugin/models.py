# coding:utf-8

"""
    'models'
    ~~~~~~~~
    
    No models here, only a signal receiver ;)
    
    :copyleft: 2012 by the PyLucid team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details
"""


from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from djangobb_forum.models import Post


@receiver(post_save, sender=Post)
def clear_cache(sender, **kwargs):
    """
    Clear the complete cache.
    This is needed, because we cache the complete pages for anonymous users.
    See:
    https://github.com/jedie/PyLucid/blob/master/pylucid_project/middlewares/cache.py
    """
#    print "Post save() -> clear cache"
    cache.clear() # FIXME: This cleaned the complete cache for every site!
