
__title__ = "CFDPorousZone"
__author__ = ""
__url__ = "http://www.freecadweb.org"

import FreeCAD, Part, math
from FreeCAD import Base
from pivy import coin
import FreeCADGui
class PartFeature:
	def __init__(self, obj):
		obj.Proxy = self

class _CfdPorousZone(PartFeature):
    "The CFD Physics Model"
    def __init__(self, obj):
        PartFeature.__init__(self, obj)
        
        #obj.addProperty("App::PropertyPythonObject","Properties")
        #obj.addProperty("Part::PropertyPartShape","Shape")
        
        #obj.addProperty("App::PropertyStringList","partNameList")
        obj.addProperty("App::PropertyPythonObject","partNameList").partNameList = []
        obj.addProperty("App::PropertyLinkList","shapeList")
        
        obj.Proxy = self
        self.Type = "PorousZone"
        

    def execute(self, fp):
	listOfShapes = []
	for i in range(len(fp.shapeList)):
            listOfShapes.append(fp.shapeList[i].Shape)
	if len(listOfShapes)>0:
	    fp.Shape = Part.makeCompound(listOfShapes)
	else:
	    fp.Shape = Part.Shape()
	    
        
        return
    def __getstate__(self):
        return None

    def __setstate__(self, state):
        return None