#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

WorkDir = "."

def install():
    pisitools.dodir("/opt")
    pisitools.insinto("/opt/eclipse", "plugins")
    pisitools.insinto("/opt/eclipse", "features")
    
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.pde.junit.runtime_3.4.200.v20120530-1435.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.pde.api.tools_1.0.400.v20120523-2012.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.pde.runtime_3.4.300.v20120523-1453.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.pde.launching_3.6.100.v20120605-203027.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.pde.ui.templates_3.4.500.v20120523-2012.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.pde.ds.ui_1.0.200.v20120530-1435.jar")
    pisitools.remove("/opt/eclipse/plugins/org.objectweb.asm_3.3.1.v201105211655.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.pde.ua.ui_1.0.200.v20120523-1453.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.pde.ua.core_1.0.200.v20120530-1435.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.pde.ds.core_1.0.200.v20120530-1435.jar")
    pisitools.remove("/opt/eclipse/plugins/org.eclipse.ui.views.log_1.0.300.v20120530-1435.jar")