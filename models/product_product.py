# -*- coding: utf_8 -*-
from openerp import models, fields, _, api, exceptions
from openerp.tools.misc import DEFAULT_SERVER_DATE_FORMAT
import locale
import time
import logging
import ipdb as pdb
from openerp.exceptions import Warning

class product_product(models.Model):
    _inherit='product.product'

    stock_minimo = fields.Float(string='Stock Minimo')

product_product()
