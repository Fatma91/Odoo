#! /usr/bin/env python
# encoding:UTF-8
from openerp.osv import orm, fields
        #...........................................hr...................................................

class myhr_employees(orm.Model):
    gender = [('m', 'Male'), ('f', 'Female')]
    career = [('n', 'normal employee'),
              ('m', 'manager for normal emoployee'),
              ('k', 'keeper for warehouse'),
              ('mk', 'manager for warehouse')
        , ('sm', 'supermanager for all warehouses')
        , ('mc', 'member  of  committee'), ]

    _name = 'myhr.employee'
    _columns = {
        'name': fields.char(string="الاسم", size=50, required=True),
        'tel': fields.char(string="رقم التليفون", size=30),
        'picture': fields.binary(string="الصوره الشخصيه "),
        'age': fields.integer(string="العمر", size=2),
        'salary': fields.float(string="المرتب", size=8),
        'gender': fields.selection(gender, string="النوع"),
        'career': fields.selection(career, string="المهنه"),
    }

        #...........................................warehouse...................................................

class odoowarehouse_warehouse(orm.Model):
    _name = 'odoowarehouse.warehouse'
    _columns = {

        'name': fields.char(string='الاسم', required=True, size=8),
        'address': fields.char(string='المكان', size=20),
        'keeper_ids': fields.many2one('myhr.employee', 'أمين المخزن', select=True),
        'manager_ids': fields.many2one('myhr.employee', 'مدير المخزن', select=True),
        'supermanager_ids': fields.many2one('myhr.employee', 'المدير العام', select=True),
    }

        #...........................................category...................................................

class odoowarehouse_category(orm.Model):
    _name = 'odoowarehouse.category'
    _columns = {
        'name': fields.char(string='الاسم ', size=50),
        'catcode': fields.integer(string='الكود', size=2),
        'subcategory_ids': fields.one2many('odoowarehouse.subcategory', 'cat_id', 'الفئه الفرعيه '),
    }

        #...........................................subcategory...................................................

class odoowarehouse_subcategory(orm.Model):
    _name = 'odoowarehouse.subcategory'
    _columns = {
        'name': fields.char(string='الاسم ', size=50),
        'subcatcode': fields.integer(string='الكود', size=2),
        'cat_id': fields.many2one('odoowarehouse.category', 'الفئه'),
    }

        #...........................................subsubcategory...................................................

class odoowarehouse_sub_subcategory(orm.Model):
    _name = 'odoowarehouse.sub.subcategory'
    _columns = {
        'name': fields.char(string='الاسم', size=50),
        'sub_subcatcode': fields.integer(string='الكود', size=2),
        'cat_id': fields.many2one('odoowarehouse.category', 'الفئه'),
        'subcat_id': fields.many2one('odoowarehouse.subcategory', 'الفئه الفرعيه ')
    }

        #...........................................product...................................................

class odoowarehouse_addproduct(orm.Model):
    case = [
        ('n', 'new'),
        ('d', 'depreciated'),
        ('u', 'used')
    ]
    _name = 'odoowarehouse.addproduct'
    _columns = {
        'Pname': fields.char(string='الاسم', size=50),
        'Photo': fields.binary(string='صوره المنتج'),
        'Price': fields.integer(string='السعر', size=50),
        'Pmax': fields.integer(string='اكبر كميه ', size=50),
        'Pmin': fields.integer(string='اقل كميه', size=50),
        'Proid': fields.integer(string='رقم المنج', size=2),
        'cat_id': fields.many2one('odoowarehouse.category', 'الفئه'),
        'subcat_id': fields.many2one('odoowarehouse.subcategory', 'الفئه الفرعيه'),
        'subsubcat_id': fields.many2one('odoowarehouse.sub.subcategory', 'القسم'),
        'Procode': fields.integer(string='productcode', size=8),
        # 'whouse_ids':fields.many2many('mywarehouse','Productwarehouse'),
        'case': fields.selection(case, string='الحاله'),
        'state': fields.selection([
                                      ('new', 'New'),
                                      ('entered', 'Entered')], 'المراحل', readonly=True),
    }

    def product_new(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'new'})
        return True

    def product_entered(self, cr, uid, ids):
        self.write(cr, uid, ids, {'state': 'entered'})
        return True
