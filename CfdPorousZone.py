
__title__ = "Classes to create a porous zone"
__author__ = ""
__url__ = "http://www.freecadweb.org"

import os.path

import FreeCAD
if FreeCAD.GuiUp:
    import FreeCADGui
    from PySide import QtCore, QtGui

import _CfdPorousZone
import Part



def makeCfdPorousZone(name="PorousZone"):
    #obj = FreeCAD.ActiveDocument.addObject("App::FeaturePython", name)
    obj = FreeCAD.ActiveDocument.addObject("Part::FeaturePython", name)
    #obj = FreeCAD.ActiveDocument.addObject("Part::Feature", name)
    _CfdPorousZone._CfdPorousZone(obj)
    #FreeCAD.ActiveDocument.recompute()

    if FreeCAD.GuiUp:
        from _ViewProviderCfdPorousZone import _ViewProviderCfdPorousZone
        _ViewProviderCfdPorousZone(obj.ViewObject)
    
    return obj

