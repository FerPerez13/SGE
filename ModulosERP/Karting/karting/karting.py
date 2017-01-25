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

class karting_circuit(osv.osv):
    """(NULL)"""
    _name = 'karting.circuit'
    _columns = {
        'name': fields.char('Nombre',size=64),
        'type': fields.selection([('adult','Adult'),('childish','Childish')], 'Tipo de circuito'),
    }
karting_circuit()

class karting_diary(osv.osv):
    """(NULL)"""
    _name = 'karting.diary'
    _columns = {
        'date': fields.date('Día', size=64),
        'round_id': fields.one2many('karting.round','round_id',required=True),
        'circuit_id': fields.many2one('karting_circuit','Circuit','required=True),
    }
karting_diary()

class karting_racer(osv.osv):
    """(NULL)"""
    _name = 'karting.racer'
    _columns = {
        'name': fields.char('Nombre',size=64,required=True),
        'surname': fields.char('Apellidos',size=64,required=True),
        'date': fields.date('Fecha nacimiento', required=True),
        'country': fields.many2one('res.country','País',required=True),
        'country_state_id': fields.many2one('res.country_state','Población',required=True),
        'email': fields.char('E-Mail', size=64,required=True),
        'diary_racer_id': fields.one2many('karting.diary.racer',required=True),
    }
karting_racer()

class karting_racer_group(osv.osv):
    """(NULL)"""
    _name = 'karting.racer.group'
    _columns = {
        'name': fields.char('Nombre', size=64, required=True),
        'racer_group_id': fields.one2many('karting.diary.racer','racer_id',required=True),
    }
karting_racer_group()

class karting_diary_racer(osv.osv):
    """(NULL)"""
    _name = 'karting.diary.racer'
    _columns = {
        'name': fields.char('Nombre carrera', size=64, required=True),
        'date': fields.date('Dia',required=True),
        'circuit_id': fields.many2one('karting.diary', 'Circuito', required=True),
        'round_id': fields.many2one('karting.round',required=True),
        'racers_id': fields.many2one('karting.racer','Corredores',required=True),
        'kart_id': fields.many2one('karting.kart_type','Kart', required=True),
    }
karting_diary_racer()

class karting_kart_type(osv.osv):
    """(NULL)"""
    _name = 'karting.kart_type'
    _columns = {
        'name': fields.char('Nombre', size=64),
        'cc': fields.int('Cilindrada', size=4),
        'kart': fields.many2one('product.product','Kart'),
    }
karting_kart_type()

class karting_round(osv.osv):
    """(NULL)"""
    _name = 'karting.round'
    _columns = {
        'round': fields.int('Tanda',size=4,required=True),
        'time': fields.float('Tiempo', size=32, required=True),
    }
karting_round()

