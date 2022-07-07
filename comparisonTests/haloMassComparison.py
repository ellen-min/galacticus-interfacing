import os 

# -------------------------------------------- RUN FORTRAN --------------------------------------------
runHaloMassXML = "./Galacticus.exe comparisonTests/haloMassFunction.xml"
exportHaloMasses = "h5ls -d haloMassFunction.hdf5/Outputs/Output1/haloMass > comparisonTests/haloMasses.txt"
exportHaloMassLnM = "h5ls -d haloMassFunction.hdf5/Outputs/Output1/haloMassFunctionLnM > comparisonTests/haloMassOutput.txt"

os.system(runHaloMassXML)
os.system(exportHaloMasses)
os.system(exportHaloMassLnM)

# -------------------------------------------- RUN PYTHON --------------------------------------------
import galacticus
import ctypes


# Set cosmological Parameters (Omega Matter, Omega Baryon, Omega Dark Energy, Temperature CMB, Hubble Constant)
cosmologyParameters = galacticus.cosmologyParametersSimple(0.27250, 0.04550, 0.72750, 2.72548, 70.20000)

# Set power spectrum options
darkMatterParticle = galacticus.darkMatterParticleCDM()
cosmologyFunctions = galacticus.cosmologyFunctionsMatterLambda(cosmologyParameters)
transferFunction = galacticus.transferFunctionEisensteinHu1999(3.046, 0.000, darkMatterParticle, cosmologyParameters, cosmologyFunctions)
powerSpectrumPrimordial = galacticus.powerSpectrumPrimordialPowerLaw(0.961, 0, 0, 1, False)
linearGrowth = galacticus.linearGrowthCollisionlessMatter(cosmologyParameters,cosmologyFunctions)
powerSpectrumPrimordialTransferredSimple = galacticus.powerSpectrumPrimordialTransferredSimple(powerSpectrumPrimordial, transferFunction, linearGrowth)
powerSpectrumWindowFunction = galacticus.powerSpectrumWindowFunctionTopHat(cosmologyParameters)
cosmologicalMassVariance = galacticus.cosmologicalMassVarianceFilteredPower(sigma8=0.807,tolerance=1.0e-6,toleranceTopHat=1.0e-6,
                                                                            nonMonotonicIsFatal=True,monotonicInterpolation=False,truncateAtParticleHorizon=False,
                                                                            cosmologyParameters_=cosmologyParameters,cosmologyFunctions_=cosmologyFunctions,
                                                                            linearGrowth_=linearGrowth,powerSpectrumPrimordialTransferred_=powerSpectrumPrimordialTransferredSimple,
                                                                            powerSpectrumWindowFunction_=powerSpectrumWindowFunction)

# Structure formation options
virialDensityContrast = galacticus.virialDensityContrastSphericalCollapseClsnlssMttrCsmlgclCnstnt(True, cosmologyFunctions)
criticalOverdensity = galacticus.criticalOverdensitySphericalCollapseClsnlssMttrCsmlgclCnstnt(linearGrowth,cosmologyFunctions,cosmologicalMassVariance,darkMatterParticle,True)
haloMassFunction = galacticus.haloMassFunctionTinker2008(cosmologyParameters, cosmologicalMassVariance, linearGrowth, cosmologyFunctions, virialDensityContrast)

# -------------------------------------------- Specify "parameters" --------------------------------------------
redshifts = [1.0]
haloMasses = [100000, 107977.516232771, 116591.440117983, 125892.541179417, 135935.639087852, 146779.926762207, 158489.319246111, 171132.830416178, 184784.979742229, 199526.231496888,
              215443.469003188, 232630.506715363, 251188.643150958, 271227.257933203, 292864.456462524, 316227.766016838, 341454.88738336, 368694.506451957, 398107.170553497,
              429866.234708228, 464158.883361278, 501187.233627273, 541169.526546464, 584341.413373517, 630957.344480193, 681292.069057961, 735642.254459642, 794328.234724282,
              857695.898590893, 926118.728128794, 1000000, 1079775.16232771, 1165914.40117983, 1258925.41179417, 1359356.39087853, 1467799.26762207, 1584893.19246111, 1711328.30416178,
              1847849.79742229, 1995262.31496888, 2154434.69003188, 2326305.06715362, 2511886.43150958, 2712272.57933203, 2928644.56462524, 3162277.66016838, 3414548.8738336,
              3686945.06451957, 3981071.70553498, 4298662.34708227, 4641588.83361278, 5011872.33627272, 5411695.26546464, 5843414.13373518, 6309573.44480193, 6812920.69057961,
              7356422.54459641, 7943282.34724281, 8576958.98590894, 9261187.28128792, 9999999.99999997, 10797751.6232771, 11659144.0117983, 12589254.1179417, 13593563.9087852,
              14677992.6762207, 15848931.9246111, 17113283.0416178, 18478497.9742229, 19952623.1496888, 21544346.9003188, 23263050.6715362, 25118864.3150958, 27122725.7933202,
              29286445.6462523, 31622776.6016838, 34145488.7383361, 36869450.6451958, 39810717.0553497, 42986623.4708228, 46415888.3361277, 50118723.3627271, 54116952.6546463,
              58434141.3373519, 63095734.4480193, 68129206.905796, 73564225.4459642, 79432823.4724281, 85769589.8590892, 92611872.8128793, 99999999.9999998, 107977516.232771,
              116591440.117983, 125892541.179417, 135935639.087852, 146779926.762207, 158489319.246111, 171132830.416178, 184784979.742229, 199526231.496888, 215443469.003188,
              232630506.715362, 251188643.150957, 271227257.933203, 292864456.462523, 316227766.016837, 341454887.38336, 368694506.451958, 398107170.553497, 429866234.708227,
              464158883.361278, 501187233.627272, 541169526.546462, 584341413.373517, 630957344.480194, 681292069.057961, 735642254.45964, 794328234.724282, 857695898.590893,
              926118728.128791, 999999999.999999, 1079775162.32771, 1165914401.17983, 1258925411.79417, 1359356390.87853, 1467799267.62207, 1584893192.46111, 1711328304.16178,
              1847849797.42229, 1995262314.96888, 2154434690.03188, 2326305067.15363, 2511886431.50958, 2712272579.33202, 2928644564.62524, 3162277660.16837, 3414548873.8336,
              3686945064.51957, 3981071705.53498, 4298662347.08227, 4641588833.61277, 5011872336.27272, 5411695265.46463, 5843414133.73518, 6309573444.80192, 6812920690.57962,
              7356422544.59641, 7943282347.2428, 8576958985.90894, 9261187281.28792, 9999999999.99997, 10797751623.2771, 11659144011.7983, 12589254117.9417, 13593563908.7852,
              14677992676.2207, 15848931924.6111, 17113283041.6178, 18478497974.2229, 19952623149.6888, 21544346900.3188, 23263050671.5362, 25118864315.0958, 27122725793.3202,
              29286445646.2523, 31622776601.6838, 34145488738.3361, 36869450645.1956, 39810717055.3497, 42986623470.8228, 46415888336.1277, 50118723362.7271, 54116952654.6463,
              58434141337.3518, 63095734448.0191, 68129206905.796, 73564225445.9642, 79432823472.4278, 85769589859.0892, 92611872812.8793, 99999999999.9998, 107977516232.771,
              116591440117.983, 125892541179.416, 135935639087.852, 146779926762.207, 158489319246.111, 171132830416.178, 184784979742.228, 199526231496.888, 215443469003.189,
              232630506715.362, 251188643150.957, 271227257933.203, 292864456462.523, 316227766016.838, 341454887383.36, 368694506451.957, 398107170553.497, 429866234708.227,
              464158883361.276, 501187233627.271, 541169526546.462, 584341413373.517, 630957344480.194, 681292069057.958, 735642254459.64, 794328234724.281, 857695898590.893,
              926118728128.791, 999999999999.999, 1079775162327.7, 1165914401179.83, 1258925411794.16, 1359356390878.53, 1467799267622.07, 1584893192461.11, 1711328304161.78,
              1847849797422.29, 1995262314968.87, 2154434690031.88, 2326305067153.63, 2511886431509.57, 2712272579332.02, 2928644564625.23, 3162277660168.36, 3414548873833.59,
              3686945064519.57, 3981071705534.97, 4298662347082.29, 4641588833612.77, 5011872336272.72, 5411695265464.64, 5843414133735.16, 6309573444801.92, 6812920690579.62,
              7356422544596.38, 7943282347242.8, 8576958985908.94, 9261187281287.88, 9999999999999.97, 10797751623277.1, 11659144011798.3, 12589254117941.6, 13593563908785.2,
              14677992676220.7, 15848931924611.1, 17113283041617.8, 18478497974222.9, 19952623149688.8, 21544346900318.7, 23263050671536.2, 25118864315095.8, 27122725793320.1,
              29286445646252.3, 31622776601683.8, 34145488738336.1, 36869450645195.6, 39810717055349.6, 42986623470822.8, 46415888336127.6, 50118723362727.1, 54116952654646.3,
              58434141337351.4, 63095734448019.1, 68129206905796, 73564225445964.1, 79432823472427.8, 85769589859089.2, 92611872812879.3, 99999999999999.4, 107977516232771,
              116591440117983, 125892541179417, 135935639087852, 146779926762207, 158489319246111, 171132830416177, 184784979742228, 199526231496888, 215443469003187, 232630506715362,
              251188643150957, 271227257933201, 292864456462522, 316227766016837, 341454887383360, 368694506451958, 398107170553496, 429866234708227, 464158883361278, 501187233627270,
              541169526546462, 584341413373517, 630957344480189, 681292069057958, 735642254459640, 794328234724276, 857695898590890, 926118728128790, 999999999999999]

pythonResults = {}
for redshift in redshifts:
  expansionFactor = cosmologyFunctions.expansionFactorFromRedshift(redshift)
  time = cosmologyFunctions.cosmicTime(expansionFactor)
  outputs = []
  for mass in haloMasses:
    hmf = haloMassFunction.differential(time,mass) * mass
    outputs.append(hmf)
  pythonResults[redshift] = outputs

# -------------------------------------------- COMPARISONS --------------------------------------------
EPS = 1.0e-1

def compareResults(l1, l2, eps):
  """
  Compare two lists.
  Print a success message if each value in one list is within EPS in the other list.
  Print fail message otherwise.
  """
  if (len(l1) != len(l2)):
    print("\n-------------------------------- FAILED FORTRAN-PYTHON COMPARISON: INVALID LENGTHS --------------------------------\n")
    return
  for i in range(len(l1)):
    if (abs(l1[i] - l2[i]) > EPS):
      print("\n-------------------------------- FAILED FORTRAN-PYTHON COMPARISON --------------------------------\n")
      return
  print("\n-------------------------------- PASSED FORTRAN-PYTHON COMPARISON --------------------------------\n")

# Read in and format Fortran output.
# TODO: Use h5py in Jupyter notebooks.
import re 
f = open("comparisonTests/haloMassOutput.txt")
fortranResults = []
for line in f:
  splitSpaces = line.split(")")
  if (len(splitSpaces) > 1):
    nums = re.findall(r"-?[\d.]+(?:e-?\d+)?", splitSpaces[1]) # find all numbers
    for num in nums:
      fortranResults.append(float(num))

# Run comparisons.
python_0 = pythonResults[1.0]
fortran_0 = fortranResults
compareResults(python_0, fortran_0, EPS)
