homoDom = 17
het = 21
homoRec = 19
popTotal = homoDom + het + homoRec

probHomoDom = homoDom/popTotal
probHet = het/popTotal
probHomoRec = homoRec/popTotal

pDD = probHomoDom * (homoDom - 1)/(popTotal - 1)
pDH = probHomoDom * het/(popTotal - 1)
pDR = probHomoDom * homoRec/(popTotal - 1)

pHD = probHet * homoDom/(popTotal - 1)
pHH = probHet * (het - 1)/(popTotal - 1)
pHR = probHet * homoRec/(popTotal - 1)

pRD = probHomoRec * homoDom/(popTotal - 1)
pRH = probHomoRec * het/(popTotal - 1)      
pRR = probHomoRec * (homoRec - 1)/(popTotal - 1)

DDfactor = 1
DHFactor = 1
DRFactor = 1
HHFactor = 0.75
HRFactor = 0.5
RRFactor = 0

probDominant = (pDD * DDfactor) + (pDH * DHFactor) + (pDR * DRFactor) + (pHD * DHFactor) + (pHH * HHFactor) + (pHR * HRFactor) + (pRD * DRFactor) + (pRH * HRFactor) + (pRR * RRFactor)

print(probDominant)