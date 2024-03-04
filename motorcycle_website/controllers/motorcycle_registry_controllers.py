# -*- coding: utf-8 -*-
from odoo import http


class motorcycle_registry(http.Controller):

    @http.route("/motorcycle_compare/", auth="public", website=True, sitemap=True)
    def motorcycle_compare(self, **kw):
        motorcycles = http.request.env["product.template"].search(
            [("detailed_type", "=", "motorcycle")]
        )
        return http.request.render(
            "motorcycle_website.motorcycle_compare",
            {"products": motorcycles},
        )

    # The purpose of using with_context(display_default_code=False)
    # in the provided code snippet could be to control the default behavior of
    # displaying product codes in a specific context,
    # such as a webpage where showing product codes may not be necessary or desirable.
    # {"products": motorcycles.with_context(display_default_code=False)},
