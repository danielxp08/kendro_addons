from odoo import models, fields


class KendroProperty(models.Model):
    _name = 'kendro.property'
    _description = 'Property'
    _order = 'sequence ASC, name ASC'

    name = fields.Char(string='Property Name', required=True, translate=True)
    description = fields.Text(string='Description', translate=True)
    active = fields.Boolean(string='Active', default=True, index=True)
    sequence = fields.Integer(string='Sequence', default=0, index=True)

    # Pricing
    price = fields.Float(string='Price per Night', required=True)
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id.id if self.env.company else None
    )

    # Location
    location = fields.Char(string='Location', required=True, translate=True)

    # Property details
    bedrooms = fields.Integer(string='Bedrooms', default=1)
    bathrooms = fields.Integer(string='Bathrooms', default=1)
    max_guests = fields.Integer(string='Max Guests', default=2)

    # Images
    image_ids = fields.Many2many(
        'ir.attachment',
        'kendro_property_image_rel',
        'property_id',
        'attachment_id',
        string='Images'
    )

    def get_image_url(self):
        """Return the URL of the first image for carousel display."""
        self.ensure_one()
        if self.image_ids:
            return self.image_ids[0].external_url or '/web/image/%s' % self.image_ids[0].id
        return '/web/static/img/placeholder.png'