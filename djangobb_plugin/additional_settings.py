# coding: utf-8

"""
    attitional settings for DjangoBB
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

def _search_position(l, s):
    for index, item in enumerate(l):
        if s in item:
            return index

def add_settings(local_dict):
    # move templates from 'djangobb_plugin' above the origin, so we
    # can "overwrite" the templates form 'djangobb_forum'
    template_dirs = list(local_dict["TEMPLATE_DIRS"])

    index = _search_position(template_dirs, "djangobb_plugin")
    assert index is not None, "djangobb_plugin not in TEMPLATE_DIRS!"
    djangobb_plugin_dir = template_dirs.pop(index)

    index = _search_position(template_dirs, "djangobb_forum")
    assert index is not None, "djangobb_forum not in TEMPLATE_DIRS!"
    template_dirs.insert(index, djangobb_plugin_dir)

    local_dict['TEMPLATE_DIRS'] = tuple(template_dirs)

    #--------------------------------------------------------------------------

    local_dict["TEMPLATE_CONTEXT_PROCESSORS"] += (
        'djangobb_forum.context_processors.forum_settings',
        'django_messages.context_processors.inbox',
        'django_authopenid.context_processors.authopenid',
    )

    #--------------------------------------------------------------------------

    middlewares = list(local_dict["MIDDLEWARE_CLASSES"])

    cache_pos = _search_position(middlewares, "PyLucidFetchFromCacheMiddleware")

    middlewares.insert(cache_pos, 'pagination.middleware.PaginationMiddleware')
    middlewares.insert(cache_pos, 'django_authopenid.middleware.OpenIDMiddleware')
    middlewares += [
        'djangobb_forum.middleware.LastLoginMiddleware',
        'djangobb_forum.middleware.UsersOnline',
    ]

    local_dict["MIDDLEWARE_CLASSES"] = tuple(middlewares)

    #--------------------------------------------------------------------------

    local_dict["INSTALLED_APPS"] += (
        'registration',
        'pagination',
        #'djangobb_forum', # is as plugin registred
        'haystack',
        'django_messages',
        'django_authopenid',
    )

    #--------------------------------------------------------------------------

    try:
        import mailer
        local_dict["INSTALLED_APPS"] += ('mailer',)
        local_dict["EMAIL_BACKEND"] = "mailer.backend.DbBackend"
    except ImportError:
        pass

    # Haystack settings
    local_dict["HAYSTACK_SITECONF"] = 'djangobb_plugin.search_sites'
    local_dict["HAYSTACK_SEARCH_ENGINE"] = 'whoosh'
    local_dict["HAYSTACK_WHOOSH_PATH"] = '/tmp/djangobb_index' # FIXME

    # Account settings
    local_dict["ACCOUNT_ACTIVATION_DAYS"] = 10
    local_dict["LOGIN_REDIRECT_URL"] = '/forum/'
    local_dict["LOGIN_URL"] = '/forum/account/signin/'



