
from rhombus.lib.utils import cerr, set_dbhandler_class, get_dbhandler_class
from rhombus.routes import add_route_view, add_route_view_class

from messy_panelseq.models.handler import generate_handler_class

set_dbhandler_class(generate_handler_class(get_dbhandler_class()))


def includeme(config):

    add_route_view_class(
        config, 'messy_panelseq.views.panel.PanelViewer', 'messy-panelseq.panel',
        '/panel',
        '/panel/@@action',
        '/panel/@@add',
        ('/panel/@@lookup', 'lookup', 'json'),
        '/panel/{id}@@edit',
        '/panel/{id}@@save',
        ('/panel/{id}@@attachment/{fieldname}', 'attachment'),
        ('/panel/{id}', 'view')
    )

# EOF
