from openerp import api, models
import ipdb as pdb

class ParticularReport(models.AbstractModel):
    _name = 'report.reporte.reporte'
    
    @api.multi
    def render_html(self, data=None):
        #pdb.set_trace()
        stock = []
        products = self.env['product.product'].search([]).sorted(key=lambda r: r.name)
        for product in products:
            if product.stock_minimo and product.qty_available != 0:
                print "No se ha establecido stock minimo"
                if product.stock_minimo >= product.qty_available:
                    stock.append(product.id)
        #pdb.set_trace() 
        stock_minimo = self.env['product.product'].browse(stock)


        report_obj = self.env['report']
        report = report_obj._get_report_from_name('reporte.reporte')
        docargs = {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'docs': self,
            'stock': stock_minimo,
        }
        return report_obj.render('reporte.reporte', docargs)