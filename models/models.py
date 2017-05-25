# -*- coding: utf-8 -*-
from openerp import models, fields, api, exceptions


class Course(models.Model):
    _inherit = 'openacademy.course'

    # Add a new column to the openacademy.course model.
    level = fields.Integer(string="Level", required=True, default=0,
                           readonly=False)

    @api.constrains('level')
    def validate_level(self):
        for rec in self:
            if rec.level < 0 or rec.level > 10:
                raise exceptions.ValidationError(
                    "Field value must be between 1 and 10.")


class Partner(models.Model):
    _inherit = 'res.partner'

    level = fields.Integer(string="Level", required=True, default=0,
                           readonly=False)

    @api.constrains('level')
    def _validate_level(self):
        for rec in self:
            if rec.level < 0 or rec.level > 10:
                raise exceptions.ValidationError(
                    "Field value must be between 1 and 10.")


class Session(models.Model):
    _inherit = 'openacademy.session'

    session_level = fields.Integer(related='course_id.level', readonly=True)

    @api.constrains('instructor_id')
    def _check_level_instructor(self):
        for rec in self:
            if rec.instructor_id and rec.instructor_id.level < rec.course_id.level:
                raise exceptions.ValidationError(
                    "The instructor level should be superior")
