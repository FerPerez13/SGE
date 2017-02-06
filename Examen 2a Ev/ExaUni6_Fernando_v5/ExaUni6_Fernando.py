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

class tfcs_tfc(osv.osv):
    _name = 'tfcs.tfc'
    _columns = {
        'number': fields.char('TFC Number', size=64, required=True),
        'name': fields.char('TFC Title', size=64, required=True),
        'date': fields.datetime('Day to defense the TFC', required=True),
        'mark': fields.integer('Mark', required=True, help='Don t put decimal numbers'),
        'notes': fields.text('Coments'),
        'students_ids': fields.one2many('tfcs.student', 'tfc_id', 'Students'),
    }
tfcs_tfc()

class tfcs_professor(osv.osv):
    _name = 'tfcs.professor'
    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'surname': fields.char('Surname', size=64, required=True),
        'employee': fields.many2one('hr.employee', 'Employee', required=True),
        'tribunal_ids': fields.many2many('tfcs.tribunal', 'tfcs_professor_tribunal_rel', 'tribunal_ids','professor_ids','Tribunals'),
    }
tfcs_professor()

class tfcs_student(osv.osv):
    _name = 'tfcs.student'
    _columns = {
        'dni': fields.char('DNI', size=9, required=True),
        'name': fields.char('Name', size=64, required=True ),
        'tfc_id': fields.many2one('tfcs.tfc', 'TFC', required=True),
        'tribunal_id': fields.many2one('tfcs.tribunal', 'Tribunal', required=True),
        'professor': fields.many2one('tfcs.professor', 'Professor', required=True),
        'contact': fields.many2one('res.partner', 'Contact', required=True),
    }
tfcs_student()

class tfcs_tribunal(osv.osv):
    _name = 'tfcs.tribunal'
    _columns = {
        'name': fields.char('Tribunal ID', size=64, required=True),
        'meeting': fields.selection([('s2-12','Class S2-12'),('s2-08','Class S2-08')], 'Meeting'),
        'professor_ids': fields.many2many('tfcs.professor', 'tfcs_tribunal_professor_rel', 'professor_ids', 'tribunal_ids', 'Professors'),
        'student_ids': fields.one2many('tfcs.student','tribunal_id','Students'),
    }
tfcs_tribunal()

