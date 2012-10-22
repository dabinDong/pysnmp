# 
# Copyright (C) 2012 Credo Semiconductor Inc.
# Author: Xiongfei GUO, <xfguo@credosemi.com>
#
# This work is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License Version 2 as published by the 
# Free Software Foundation.
#
# This work is distributed in the hope that it will be useful, but without
# any warranty; without even the implied warranty of merchantability or
# fitness for a particular purpose. See the GNU General Public License for 
# more details. You should have received a copy of the GNU General Public 
# License along with this program; if not, write to: Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

try:
    from gevent.socket import AF_INET6
except:
    AF_INET6 = None
from pysnmp.carrier.gevent.dgram.base import DgramGeventTransport

domainName = snmpUDP6Domain = (1, 3, 6, 1, 2, 1, 100, 1, 2)

class Udp6GeventTransport(DgramGeventTransport):
    sockFamily = AF_INET6

Udp6Transport = Udp6GeventTransport
