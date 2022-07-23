c_lib.treeNodeL.restype  = c_void_p
c_lib.treeNodeL.argtypes = [ c_long ]

class treeNodeL:
  # Constructor
  def __init__(self, objectTypeId):
    self._classId = -1 # intended to indicate this is a treeNode
    self._objectTypeId = objectTypeId # indicate the type of node contained in this treeNode
  
    self._glcObj = c_lib.treeNodeL(objectTypeId)
  
  # Get ID
  def treeNodeID(self):
    return c_lib.treeNodeIDL(self._glcObj)
  
  def treeNodeSetID(self, newID):
    self._objectTypeId = newID
    c_lib.treeNodeSetIDL(self._glcObj, newID)

c_lib.nodeComponentBasicL.restype  = c_void_p
c_lib.nodeComponentBasicL.argtypes = [ c_void_p ]

c_lib.nodeComponentBasicMassL.restype  = c_double
c_lib.nodeComponentBasicMassL.argtypes = [ c_void_p ]
c_lib.nodeComponentBasicSetMassL.restype  = c_void_p
c_lib.nodeComponentBasicSetMassL.argtypes = [ c_void_p, c_double ]

c_lib.nodeComponentBasicTimeL.restype  = c_double
c_lib.nodeComponentBasicTimeL.argtypes = [ c_void_p ]
c_lib.nodeComponentBasicSetTimeL.restype  = c_void_p
c_lib.nodeComponentBasicSetTimeL.argtypes = [ c_void_p, c_double ]

c_lib.nodeComponentBasicTimeLastIsolatedL.restype  = c_double
c_lib.nodeComponentBasicTimeLastIsolatedL.argtypes = [ c_void_p ]
c_lib.nodeComponentBasicSetTimeLastIsolatedL.restype  = c_void_p
c_lib.nodeComponentBasicSetTimeLastIsolatedL.argtypes = [ c_void_p, c_double ]

class nodeComponentBasicL:
  def __init__(self, treeNode):
    self._id = -1
    self._glcObj = c_lib.nodeComponentBasicL(treeNode._glcObj)

  def nodeComponentBasicMassL(self):
    return c_lib.nodeComponentBasicMassL(self._glcObj)

  def nodeComponentBasicTimeL(self):
    return c_lib.nodeComponentBasicTimeL(self._glcObj)

  def nodeComponentBasicTimeLastIsolatedL(self):
    return c_lib.nodeComponentBasicTimeLastIsolatedL(self._glcObj)
  
  def nodeComponentBasicSetMassL(self, mass):
    self._mass = mass
    c_lib.nodeComponentBasicSetMassL(self._glcObj, mass)

  def nodeComponentBasicSetTimeL(self, time):
    self._time = time
    c_lib.nodeComponentBasicSetTimeL(self._glcObj, time)
   
  def nodeComponentBasicSetTimeLastIsolatedL(self, timeLastIsolated):
    self._timeLastIsolated = timeLastIsolated
    c_lib.nodeComponentBasicSetTimeLastIsolatedL(self._glcObj, timeLastIsolated)
