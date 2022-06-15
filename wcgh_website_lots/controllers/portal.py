# -*- coding: utf-8 -*-

from collections import OrderedDict

from odoo import http, _
from odoo.http import request
from odoo.osv.expression import OR, AND

from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager


class ProductStatusCustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'product_status_count' in counters:
            Lots = request.env['stock.production.lot']
            domain = Lots._product_status_get_portal_domain()
            values['product_status_count'] = Lots.sudo().search_count(domain)
        return values

    def _get_searchbar_inputs(self):
        return {
            'all': {'input': 'all', 'label': _('Search in All')},
            'product': {'input': 'product', 'label': _('Search in Product')},
            'serial': {'input': 'serial', 'label': _('Search in Serial')},
            'owner': {'input': 'owner', 'label': _('Search in Owner')},
            'part': {'input': 'part', 'label': _('Search in Part Number')},
            'condition': {'input': 'condition', 'label': _('Search in Condition')},
            'box': {'input': 'box', 'label': _('Search in Box number')},
            'location': {'input': 'location', 'label': _('Search in Location')},
        }

    def _get_searchbar_groupby(self):
        return {
            'none': {'input': 'none', 'label': _('None')},
            'owner': {'input': 'owner', 'label': _('Owner')},
            'product': {'input': 'product', 'label': _('Product')},
            'condition': {'input': 'condition', 'label': _('Condition')},
        }

    def _get_search_domain(self, search_in, search):
        search_domain = []
        if search_in in ('product', 'all'):
            search_domain = OR([search_domain, [('product_id', 'ilike', search)]])
        if search_in in ('serial', 'all'):
            search_domain = OR([search_domain, [('name', 'ilike', search)]])
        if search_in in ('owner', 'all'):
            search_domain = OR([search_domain, [('partner_id', 'ilike', search)]])
        if search_in in ('part', 'all'):
            search_domain = OR([search_domain, [('customer_part_number', 'ilike', search)]])
        if search_in in ('condition', 'all'):
            search_domain = OR([search_domain, [('condition_id', 'ilike', search)]])
        if search_in in ('box', 'all'):
            search_domain = OR([search_domain, [('boxed_tracking_number', 'ilike', search)]])
        if search_in in ('location', 'all'):
            search_domain = OR([search_domain, [('current_location_id', 'ilike', search)]])
        return search_domain

    def _get_groupby_mapping(self):
        return {
            'owner': 'partner_id',
            'product': 'product_id',
            'condition': 'condition_id',
        }

    def _get_searchbar_filters(self):
        res = {
            'all': {'label': _('All'), 'domain': []},
        }
        for condition in request.env['stock.production.lot.condition'].sudo().search([]):
            res[str(condition.id)] = {'label': condition.name, 'domain': [("condition_id", "=", condition.id)]}
        return res

    @http.route(['/my/product_status', '/my/product_status/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_product_status(self, page=1, sortby=None, filterby=None, search=None, search_in='all', groupby='none', **kw):
        Lots = request.env['stock.production.lot']
        domain = Lots._product_status_get_portal_domain()
        Lots_sudo = Lots.sudo()

        values = self._prepare_portal_layout_values()
        _items_per_page = 100

        searchbar_inputs = self._get_searchbar_inputs()

        searchbar_groupby = self._get_searchbar_groupby()

        searchbar_filters = self._get_searchbar_filters()

        if search and search_in:
            domain += self._get_search_domain(search_in, search)

        if not filterby:
            filterby = 'all'
        domain = AND([domain, searchbar_filters[filterby]['domain']])

        product_status_count = Lots_sudo.search_count(domain)
        # pager
        pager = portal_pager(
            url="/my/product_status",
            url_args={'sortby': sortby, 'search_in': search_in, 'search': search, 'filterby': filterby, 'groupby': groupby},
            total=product_status_count,
            page=page,
            step=_items_per_page
        )

        def get_product_status():
            groupby_mapping = self._get_groupby_mapping()
            field = groupby_mapping.get(groupby, None)
            orderby = False
            product_status = Lots_sudo.search(domain, order=orderby, limit=_items_per_page, offset=pager['offset'])
            if field:
                raw_grouped_product_status =  Lots_sudo.read_group(domain, [field, "ids:array_agg(id)"], [field])
                # hope it is cached (product_qty is not stored, so can't be fetched from read_group)
                grouped_product_status = [(Lots_sudo.browse(group["ids"]), sum(Lots_sudo.browse(group["ids"]).mapped('product_qty'))) for group in raw_grouped_product_status]

                return product_status, grouped_product_status

            grouped_product_status = [(
                product_status,
                False
            )] if product_status else []
            return product_status, grouped_product_status

        product_status, grouped_product_status = get_product_status()

        values.update({
            'product_status': product_status,
            'grouped_product_status': grouped_product_status,
            'page_name': 'product_status',
            'default_url': '/my/product_status',
            'pager': pager,
            'search_in': search_in,
            'search': search,
            'groupby': groupby,
            'searchbar_inputs': searchbar_inputs,
            'searchbar_groupby': searchbar_groupby,
            'searchbar_filters': OrderedDict(sorted(searchbar_filters.items())),
            'filterby': filterby,
        })
        return request.render("wcgh_website_lots.portal_my_product_status", values)
