from odoo import models, fields, api


class application(models.Model):
    _name = 'housemaid.application'
    _description = 'Housemaid Application with Full Information of the Housemaid'

    create_date = fields.Date(string="Create Date", required=True, defualt=fields.Date.context_today, )
    ref_number = fields.Char(string="Ref No", required=True, size=20, )
    name = fields.Char(string="Housemaid Name", required=True, size=60, )
    gender = fields.Selection(selection=[('0', 'Male'),
                                         ('1', 'Female'),
                                         ('2', 'Other'), ],
                              string="Gender",
                              default='1', required=True, )
    marital_status = fields.Selection(selection=[('0', 'Single'),
                                                 ('1', 'Married'),
                                                 ('2', 'Divorced'),
                                                 ('3', 'Widow'), ],
                                      string="Marital Status",
                                      default='0', required=True, )
    salary = fields.Integer(string="Monthly Salary", required=True, copy=True)
    image_1920 = fields.Image(string="Application Image", )
    image_1921 = fields.Image(string="Passport Image", )
    country_id = fields.Many2one('res.country', 'Nationality')
    externaloffices_id = fields.Many2one('housemaid.externaloffices', 'External Office')
    religion = fields.Selection(selection=[('1', 'Christian'),
                                           ('2', 'Muslim'),
                                           ('3', 'Jewish'),
                                           ('4', 'Buddhist'),
                                           ('5', 'Hindu'),
                                           ('6', 'Others'), ],
                                string="Religion",
                                required=True, )
    education_level = fields.Selection(selection=[('0', 'Non Educated'),
                                                  ('1', 'Literacy'),
                                                  ('2', 'Primary School'),
                                                  ('3', 'Prep School'),
                                                  ('4', 'High School'),
                                                  ('5', 'University Education'),
                                                  ('6', 'Postgraduate Education'), ],
                                       string="Education Level",
                                       required=True, )
    birth_date = fields.Date(string="Birth Date", required=False, )
    postapplied = fields.Selection(selection=[('0', 'Housemaid'),
                                              ('1', 'baby Sitter'),
                                              ('2', 'Cooker'),
                                              ('3', 'Gardener'),
                                              ('4', 'Guard'), ],
                                   string="Acceptable Job",
                                   required=True, )
    passport = fields.Char(string="Passport No", required=True, size=60, )
    passport_issue = fields.Date(string="Passport Issued", required=False, )
    passport_expiry = fields.Date(string="Passport Expiry", required=False, )
    eng_lang_skill = fields.Boolean(string="English Skill", default=False, )
    arb_lang_skill = fields.Boolean(string="Arabic Skill", default=False, )
    fr_lang_skill = fields.Boolean(string="French Skill", default=False, )
    experience_1 = fields.Char(string="First Experience", required=False, size=150, )
    experience_2 = fields.Char(string="Second Experience", required=False, size=150, )
    experience_3 = fields.Char(string="Third Experience", required=False, size=150, )
    contacts = fields.Char(string="Contact Numbers", required=False, size=80, )
    arrival_date = fields.Date(string="Arrival Date", required=False, )
