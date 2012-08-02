# coding:utf-8

"""
    search forum entries
    ~~~~~~~~~~~~~~~~~~~
    
    :copyleft: 2012 by the PyLucid team, see AUTHORS for more details.
    :license: GNU GPL v3 or above, see LICENSE for more details
"""


from django.db.models import Q

from djangobb_forum.models import Post

from pylucid_project.apps.pylucid.models.pluginpage import PluginPage


def get_search_results(request, search_languages, search_strings, search_results):
    groups = request.user.groups.all() or []

    queryset = Post.objects.all()
    queryset = queryset.filter(
        Q(topic__forum__category__groups__in=groups) | Q(topic__forum__category__groups__isnull=True)
    )

    for term in search_strings:
        queryset = queryset.filter(
            Q(body__icontains=term) | Q(topic__name__icontains=term)
        )

    # TODO: How can we resolve the url better?
    plugin_page = PluginPage.objects.get_by_plugin_name("djangobb_plugin")
    base_url = plugin_page.get_absolute_url()

    # FIXME: This doesn't work:
#    plugin_url_resolver = PluginPage.objects.get_url_resolver("djangobb_plugin")

    for item in queryset:

        # FIXME: This doesn't work:
#        url = plugin_url_resolver.reverse("djangobb:post", kwargs={"post_id":item.id})

        search_results.add(
            model_instance=item,

            # displayed headline of the result hit
            headline=item.topic.name,

            # displayed in the result list
            language=request.PYLUCID.current_language,

            # Link to the hit
            url="%spost/%s/" % (base_url, item.id),

            content=item.body_html,

            # hits in meta content has a higher score, but the content would not displayed 
            meta_content="",
        )
