# VIRIS
Welcome to VIRIS (Viral Infection Risk Simulator)! This repository includes all materials for VIRIS and the associated app. VIRIS is a powerful simulator to quickly assess and compare non-pharmaceutical interventions (NPIs) for airborne disease. The simulator combines people movement schedule in an indoor space, viral transmission modelling, and detailed architectural design. The web app for VIRIS can be accessed at https://viris.app (available soon).

The jupyter notebook for different case study/scenario are included in different folders. For each case, there are usually two steps: step 1 - architectural design; step 2 - people movement and viral transmission simulations. The architectural design and people movement simulations are conducted using <a href="https://github.com/wassimj/topologicpy">topologicpy</a>, the API documentation of which can be found at https://topologicpy.readthedocs.io/.

Prerequisites
----------------------

The scripts require <a href="https://github.com/wassimj/topologicpy">topologicpy</a>, <a href="https://github.com/kinnala/scikit-fem">scikit-fem</a>, and <a href="https://gmsh.info">gmsh</a>, which can be installed via
`pip install topologicpy scikit-fem gmsh`

Related papers
----------------------

Xue, Y., Jabi, W., Woolley, T. E. and Kaouri, K. 2024. VIRIS: Simulating indoor viral transmission combining architectural design and people movement, submitted.  
Jabi, W., Xue, Y., Woolley, T. E. and Kaouri, K. 2024. 3D Topological Modeling and Multi-Agent Movement Simulation for Viral Infection Risk Analysis, submitted.  
Lau, Z, Griffiths, I. M., English, A. and Kaouri, K. 2022. Predicting the spatio-temporal infection risk in indoor spaces using an efficient airborne transmission model, *Proceedings of the Royal Society A*, **478**: 20210383. https://doi.org/10.1098/rspa.2021.0383.  
Moore, J. W., Lau, Z., Kaouri, K., Dale, T. C. and Woolley, T. E. 2021. A General Computational Framework for COVID-19 Modelling with Applications to Testing Varied Interventions in Education Environments, *COVID*, **1**(4), pp.674-703. https://doi.org/10.3390/covid1040055.  
Harper, P. R., Moore, J. W. and Woolley, T. E. 2021. Covid-19 transmission modelling of students returning home from university. *Health Systems*. **10**, pp.31-40, https://doi.org/10.1080/20476965.2020.1857214.


About us
----------------------

<a href="https://profiles.cardiff.ac.uk/staff/kaourik">Katerina Kaouri</a>: Reader in Applied Mathematics, Cardiff University
<a href="https://profiles.cardiff.ac.uk/staff/woolleyt1">Thomas Woolley</a>: Reader in Applied Mathematics, Cardiff University
<a href="https://profiles.cardiff.ac.uk/staff/jabiw">Wassim Jabi</a>: Professor and Chair of Computational Methods in Architecture, Cardiff University
<a href="https://yidanxue.github.io">Yidan Xue</a>: Postdoc at the University of Manchester, previously postdoc at Cardiff University