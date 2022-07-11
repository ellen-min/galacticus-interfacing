# -------------------------------------------- IMPORT FORTRAN DATA --------------------------------------------
#colossusResults = open("../../testSuite/data/haloBiasesColossus/sheth01_NA.txt")
# Data and parameters taken from above path.

colossusResults = {0.0: [0.734267, 0.753420, 0.789104, 0.850877, 0.954963, 1.130743, 1.433610, 1.975495, 3.004984, 5.112369],
                  0.5: [0.779165, 0.824471, 0.896504, 1.010418, 1.192284, 1.489924, 1.994336, 2.890808, 4.593047, 8.087258],
                  1.0: [0.864914, 0.945736, 1.067630, 1.253988, 1.545425, 2.017001, 2.812343, 4.225198, 6.913473, 12.449322]}

# -------------------------------------------- RUN PYTHON --------------------------------------------
import galacticus
import ctypes

# Set cosmological Parameters (Omega Matter, Omega Baryon, Omega Dark Energy, Temperature CMB, Hubble Constant)
cosmologyParameters = galacticus.cosmologyParametersSimple(0.3089, 0.0486, 0.691008829245, 2.7255, 67.74)

# Set power spectrum options
darkMatterParticle = galacticus.darkMatterParticleCDM()
cosmologyFunctions = galacticus.cosmologyFunctionsMatterLambda(cosmologyParameters)
transferFunction = galacticus.transferFunctionEisensteinHu1999(3.046, 0.000, darkMatterParticle, cosmologyParameters, cosmologyFunctions)
powerSpectrumPrimordial = galacticus.powerSpectrumPrimordialPowerLaw(0.9667, 0, 0, 1, False)
linearGrowth = galacticus.linearGrowthCollisionlessMatter(cosmologyParameters,cosmologyFunctions)
powerSpectrumPrimordialTransferredSimple = galacticus.powerSpectrumPrimordialTransferredSimple(powerSpectrumPrimordial, transferFunction, linearGrowth)
powerSpectrumWindowFunction = galacticus.powerSpectrumWindowFunctionTopHat(cosmologyParameters)
cosmologicalMassVariance = galacticus.cosmologicalMassVarianceFilteredPower(sigma8=0.8159,tolerance=1.0e-6,toleranceTopHat=4.0e-6,
                                                                            nonMonotonicIsFatal=True,monotonicInterpolation=False,truncateAtParticleHorizon=False,
                                                                            cosmologyParameters_=cosmologyParameters,cosmologyFunctions_=cosmologyFunctions,
                                                                            linearGrowth_=linearGrowth,powerSpectrumPrimordialTransferred_=powerSpectrumPrimordialTransferredSimple,
                                                                            powerSpectrumWindowFunction_=powerSpectrumWindowFunction)

# Structure formation options
linearGrowth = galacticus.linearGrowthCollisionlessMatter(cosmologyParameters,cosmologyFunctions)
criticalOverdensity = galacticus.criticalOverdensitySphericalCollapseClsnlssMttrCsmlgclCnstnt(linearGrowth,cosmologyFunctions,cosmologicalMassVariance,darkMatterParticle,True)
darkMatterHaloBias = galacticus.darkMatterHaloBiasSheth2001(criticalOverdensity, cosmologicalMassVariance)

# -------------------------------------------- Specify "parameters" --------------------------------------------
redshifts = [0.0, 0.5, 1.0]
haloMasses = [10000000000.0, 35938140000, 129155000000,
              464158900000, 1668101000000, 5994843000000,
              21544350000000, 77426370000000, 278255900000000,
              1000000000000000.0]

adjustedHubbleConstant = 0.6774

pythonResults = {}
for redshift in redshifts:
  expansionFactor = cosmologyFunctions.expansionFactorFromRedshift(redshift)
  time = cosmologyFunctions.cosmicTime(expansionFactor)
  outputs = []
  for mass in haloMasses:
    mass /= adjustedHubbleConstant #Adjust
    bias = darkMatterHaloBias.biasByMass(mass, time)
    outputs.append(bias)
  pythonResults[redshift] = outputs

# -------------------------------------------- COMPARISONS --------------------------------------------
EPS = 1e-2

def compareResults(l1, l2, eps, redshift):
  """
  Compare two lists.
  Print a success message if each value in one list is within EPS in the other list.
  Print fail message otherwise.
  """
  if (len(l1) != len(l2)):
    print("\n-------------------------------- FAILED FORTRAN-PYTHON COMPARISON: INVALID LENGTHS --------------------------------\n")
    return
  for i in range(len(l1)):
      if (abs(l1[i] - l2[i])) > EPS*0.5*(l1[i] + l2[i]):
        print("\n-------------------------------- FAILED FORTRAN-PYTHON COMPARISON FOR REDSHIFT= " + str(redshift) + "--------------------------------\n")
        return
  print("\n-------------------------------- PASSED FORTRAN-PYTHON COMPARISON FOR REDSHIFT= " + str(redshift) + "--------------------------------\n")

# Run comparisons.
for redshift in redshifts:
  pythonResult = pythonResults[redshift]
  fortranResult = colossusResults[redshift]
  print(pythonResult)
  compareResults(pythonResult, fortranResult, EPS, redshift)
