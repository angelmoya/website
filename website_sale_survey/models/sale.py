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
from openerp import models, api, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    survey_id = fields.Many2one(
        comodel_name='survey.survey',
        string='Survey',
        compute='_compute_survey_id')

    @api.multi
    def _compute_survey_id(self):
        survey = self.env['survey.survey'].search(
            [('default_for_website_sales', '=', True)])
        survey = len(survey) > 0 and survey[0] or False
        for record in self:
            record.survey_id = survey
