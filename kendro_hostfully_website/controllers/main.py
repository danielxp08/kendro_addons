from odoo import http
from odoo.http import request


class KendroPropertyController(http.Controller):
    """Optional RPC controller for custom JSON access to properties."""

    @http.route('/kendro/properties', type='json', auth='public', website=True)
    def list_properties(self, domain=None, limit=None):
        """
        Return properties as JSON for custom integrations.
        Usage: /kendro/properties?limit=10
        """
        domain = domain or [('active', '=', True)]
        limit = limit or 10

        properties = request.env['kendro.property'].search_read(
            domain=domain,
            fields=['id', 'name', 'description', 'price', 'location',
                    'bedrooms', 'bathrooms', 'max_guests'],
            limit=limit
        )
        return properties