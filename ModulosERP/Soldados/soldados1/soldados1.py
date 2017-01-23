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

class guards_soldier(osv.osv):
    _name = 'guards.soldier'
    _columns = {
        'id_soldier': fields.char('ID', size=64, required=True),
        'name': fields.char('Name', size=64, required=True),
        'quarter': fields.many2one('guards.quarter', 'Quarter'),
        'rank': fields.selection([('soldier','Soldier'),('corporal','Corporal'),('sergeant','Sergeant')], 'Rank'),
        'soldier_ids': fields.many2many('guards.guard','guards_soldier_guard_rel','soldier_id','guards_id', readonly=True),
    }
guards_soldier()

class guards_quarter(osv.osv):
    _name = 'guards.quarter'
    _columns = {
        'name': fields.char('Name', size=64, required=True),
        'quarter_address': fields.many2one('res.partner.address', 'Ubication'),
    }
guards_quarter()

class guards_guard(osv.osv):
    _name = 'guards.guard'
    _columns = {
        'name': fields.char('Service code', size=64, required=True),
        'description': fields.char('Description', size=1000, required=True),
        'date': fields.date('Date', required=True),
        'hour': fields.integer('Hour', required=True),
        'guard': fields.many2many('guards.soldier','guards_soldier_guards_rel','guards_id','soldier_id','Guards'),
    }
guards_guard()

