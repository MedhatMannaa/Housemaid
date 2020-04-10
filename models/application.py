from odoo import models, fields, api

app_state = [('new_application', 'New Application'),
             ('cancel_application', 'Cancel Application'),
             ('reservation', 'Reservation'),
             ('visa', 'Visa'),
             ('expecting_arrival', 'Expecting Arrival'),
             ('arrived', 'Arrived'),
             ('delivered', 'Delivered'),
             ]


class Application(models.Model):
    _name = 'housemaid.application'
    _description = 'Housemaid Application with Full Information of the Housemaid'

    create_date = fields.Date(string="Create Date", required=True, defualt=fields.Date.context_today, )
    ref_number = fields.Char(string="Ref No", required=True, size=20, )
    name = fields.Char(string="Housemaid Name", required=True, size=60, )
    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female'),
                                         ('other', 'Other'), ],
                              string="Gender",
                              default='female', required=True, )
    marital_status = fields.Selection(selection=[('single', 'Single'),
                                                 ('married', 'Married'),
                                                 ('divorced', 'Divorced'),
                                                 ('widow', 'Widow'), ],
                                      string="Marital Status",
                                      required=True, )
    salary = fields.Integer(string="Monthly Salary", required=True, copy=True)
    application_scan = fields.Image(string="Application Image", )
    passport_scan = fields.Image(string="Passport Image", )
    country = fields.Many2one(comodel_name='res.country', string='Nationality')
    external_offices = fields.Many2one(comodel_name='housemaid.externaloffices', string='External Office')
    religion = fields.Selection(selection=[('christian', 'Christian'),
                                           ('muslim', 'Muslim'),
                                           ('jewish', 'Jewish'),
                                           ('buddhist', 'Buddhist'),
                                           ('hindu', 'Hindu'),
                                           ('others', 'Others'), ],
                                string="Religion",
                                required=True, )
    education_level = fields.Selection(selection=[('non_educated', 'Non Educated'),
                                                  ('literacy', 'Literacy'),
                                                  ('primary_school', 'Primary School'),
                                                  ('prep_school', 'Prep School'),
                                                  ('high_school', 'High School'),
                                                  ('university_education', 'University Education'),
                                                  ('postgraduate_education', 'Postgraduate Education'), ],
                                       string="Education Level",
                                       required=True, )
    birth_date = fields.Date(string="Birth Date", required=False, )
    postapplied = fields.Selection(selection=[('housemaid', 'Housemaid'),
                                              ('baby_sitter', 'Baby Sitter'),
                                              ('cooker', 'Cooker'),
                                              ('gardener', 'Gardener'),
                                              ('guard', 'Guard'), ],
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
    state = fields.Selection(string="Application Status", required=True, selection=app_state, default='new_application')
