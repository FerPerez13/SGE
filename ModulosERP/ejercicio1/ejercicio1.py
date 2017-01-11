##############################################################################
#
# Copyright (c) 2004 TINY SPRL. (http://tiny.be) All Rights Reserved.
#                    Fabien Pinckaers <fp@tiny.Be>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from osv import osv, fields

class school_professor(osv.osv):
    """(NULL)"""
    _name = 'school.professor'
    _columns = {
        'name': fields.char('Professor Name', size=64, required=True),
        'contract': fields.selection([('trainee','Trainee'),('named','Named')],'Contract'),
        'partner_id': fields.many2one('res.partner','Associated Partner'),
        'address_id': fields.many2one('res.partner.address','Private Address'),
        'hours_available': fields.integer('Hours Per Week'),
        'course_ids': fields.one2many('school.course', 'prof_id', 'Courses'),
    }
school_professor()

class school_course(osv.osv):
    """(NULL)"""
    _name = 'school.course'
    _columns = {
        'name': fields.char('Course', size=32, required=True),
        'subject': fields.char('Subject', size=32, required=True),
        'prof_id': fields.many2one('res.partner', 'Professor', required=True),
        'hours_total': fields.integer('Total Hours'),
        'requirements': fields.char('Requirements', size=64),
        'website': fields.char('Website', size=64),
        'date': fields.date('First Date'),
        'note': fields.text('Note'),
    }
school_course()

class school_event(osv.osv):
    """(NULL)"""
    _name = 'school.event'
    _columns = {
        'course_id': fields.many2one('school.course', 'Course', required=True),
        'date': fields.datetime('Start Date'),
        'date_end': fields.datetime('End Date'),
        'name': fields.char('Title', size=32),
    }
school_event()

class school_student(osv.osv):
    """(NULL)"""
    _name = 'school.student'
    _columns = {
        'name': fields.char('Name', size=64),
        'surname': fields.char('Surname', size=32),
        'IDNum': fields.char('IDNum', size=32),
        'suscriptions_ids': fields.many2many('school.course', 'school_course_student_suscription_rel', 'course_id','student_id', 'Suscriptions'),
    }
school_student()

