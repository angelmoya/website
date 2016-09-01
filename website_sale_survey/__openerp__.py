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
{
    "name": "Website Sale Survey",
    "summary": "Survey for Online Sales",
    "version": "8.0.1.0.0",
    "category": "Website",
    "website": "https://odoo-community.org/",
    "author": "Jamotion GmbH, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    'depends': [
        'website_sale',
        'survey'
    ],
    'data': [
        'views/template.xml',
        'views/survey_view.xml',
    ]
}
