"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'newhome.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.ModelList(
            _('Настройка пользователей:'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=('django.contrib.*',),
        ))

        self.children.append(modules.ModelList(
            _('Настройка сайта'),
            collapsible=True,
            column=1,
            css_classes=('collapse closed',),
            models=('main.models.WorkingTime', 'main.models.Adress', 'main.models.Hmenu', 'main.models.HmenuItems',),
        ))

        self.children.append(modules.ModelList(
            _('Продукция'),
            collapsible=True,
            column=2,
            css_classes=('collapse closed',),
            models=('main.models.*',),
            exclude=('main.models.WorkingTime',),
        ))

        # append another link list module for "support".
        self.children.append(modules.LinkList(
            _('Media Management'),
            column=3,
            children=[
                {
                    'title': _('FileBrowser'),
                    'url': '/admin/filebrowser/browse/',
                    'external': False,
                },
            ]
        ))


        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Последние действия'),
            limit=5,
            collapsible=False,
            column=3,
        ))
