import galacticus
import ctypes

treeNodeExample = galacticus.treeNodeL(1)
print("The tree node ID before changing is " + str(galacticus.treeNodeL.treeNodeID(treeNodeExample)) + ".")
galacticus.treeNodeL.treeNodeSetID(treeNodeExample, 10)
print("The tree node ID after changing is " + str(galacticus.treeNodeL.treeNodeID(treeNodeExample)) + ".\n")

nodeComponentBasicExample = galacticus.nodeComponentBasicL(treeNodeExample)

print("Mass before changing: " + str(galacticus.nodeComponentBasicL.nodeComponentBasicMassL(nodeComponentBasicExample)))
galacticus.nodeComponentBasicL.nodeComponentBasicSetMassL(nodeComponentBasicExample, 100000)
print("Mass after changing: " + str(galacticus.nodeComponentBasicL.nodeComponentBasicMassL(nodeComponentBasicExample)) + "\n")

print("Time before changing: " + str(galacticus.nodeComponentBasicL.nodeComponentBasicTimeL(nodeComponentBasicExample)))
galacticus.nodeComponentBasicL.nodeComponentBasicSetTimeL(nodeComponentBasicExample, 500)
print("Time after changing: " + str(galacticus.nodeComponentBasicL.nodeComponentBasicTimeL(nodeComponentBasicExample)) + "\n")

# Time last isolated does not work with a singular node.
# print("Time last isolated before changing: " + str(galacticus.nodeComponentBasicL.nodeComponentBasicTimeLastIsolatedL(nodeComponentBasicExample)))
# galacticus.nodeComponentBasicL.nodeComponentBasicSetTimeLastIsolatedL(nodeComponentBasicExample, 5)
# print("Time last isolated after changing: " + str(galacticus.nodeComponentBasicL.nodeComponentBasicTimeLastIsolatedL(nodeComponentBasicExample)) + "\n")
