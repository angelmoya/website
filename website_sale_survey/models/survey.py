# -*- coding: utf-8 -*-
#
#    Jamotion GmbH, Your Odoo implementation partner
#    Copyright (C) 2013-2015 Jamotion GmbH.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    Created by angel.moya on 01.09.2016.
#
from openerp import models, api, fields, _
from openerp.exceptions import ValidationError


class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    default_for_website_sales = fields.Boolean(
        string='Default for Website Sales',
        help='If checked this survey could be done by customer after payment, '
             'no more than one survey could be set as default.')

    @api.constrains('default_for_website_sales')
    def _check_field(self):
        defaults = self.search([('default_for_website_sales', '=', True)])
        if len(defaults) > 1:
            raise ValidationError(
                _("No more than one survey could be set as default."))


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    sale_order_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sale Order')
