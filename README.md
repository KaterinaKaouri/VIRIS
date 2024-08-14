# VIRIS
Welcome to VIRIS - Viral Infection Risk Simulator! This repository includes all materials for VIRIS and the associated web app. VIRIS is a powerful simulator that can quickly assess and compare non-pharmaceutical interventions (NPIs) for airborne diseases, in diverse indoor spaces. The simulator combines people movement, viral transmission modelling, and detailed architectural design. The web app for VIRIS can be accessed at https://viris.app (available soon).

The jupyter notebooks for different case studies/scenarios are included in separate folders. For each case study, there are three main steps: step 1 - specifying the architectural design; step 2 - specifying people movement and step 3 - determining viral transmission (concentration of the virus and infection risk). The architectural design and people movement are powered by <a href="https://github.com/wassimj/topologicpy">topologicpy</a>. (The API documentation of topologypy can be found at https://topologicpy.readthedocs.io/.)

Prerequisites
-------------

The scripts require <a href="https://github.com/wassimj/topologicpy">topologicpy</a>, <a href="https://github.com/kinnala/scikit-fem">scikit-fem</a>, and <a href="https://gmsh.info">gmsh</a>, which can be installed via
`pip install topologicpy scikit-fem gmsh`

Related papers and other resources
----------------------------------

Xue, Y., Jabi, W., Woolley, T. E. and Kaouri, K. 2024. VIRIS: Simulating indoor viral transmission combining architectural design and people movement, submitted.  
Jabi, W., Xue, Y., Woolley, T. E. and Kaouri, K. 2024. 3D Topological modeling and multi-agent movement simulation for viral infection risk analysis, submitted.  
Lau, Z, Griffiths, I. M., English, A. and Kaouri, K. 2022. Predicting the spatio-temporal infection risk in indoor spaces using an efficient airborne transmission model, *Proceedings of the Royal Society A*, **478**, 20210383. https://doi.org/10.1098/rspa.2021.0383.  
Moore, J. W., Lau, Z., Kaouri, K., Dale, T. C. and Woolley, T. E. 2021. A General computational framework for COVID-19 modelling with applications to testing varied interventions in education environments, *COVID*, **1**(4), pp.674-703. https://doi.org/10.3390/covid1040055.  
<a href="https://www.siam.org/publications/siam-news/articles/epidemic-simulator-and-web-app-models-viral-transmission-in-indoor-spaces"> Epidemic Simulator and Web App Models Viral Transmission in Indoor Spaces  </a>, SIAM News, June 2024. 

About us
--------

<a href="https://profiles.cardiff.ac.uk/staff/kaourik">Katerina Kaouri</a>: Reader in Applied Mathematics, Cardiff University  
<a href="https://profiles.cardiff.ac.uk/staff/woolleyt1">Thomas Woolley</a>: Reader in Applied Mathematics, Cardiff University  
<a href="https://profiles.cardiff.ac.uk/staff/jabiw">Wassim Jabi</a>: Professor and Chair of Computational Methods in Architecture, Cardiff University  
<a href="https://yidanxue.github.io">Yidan Xue</a>: Postdoctoral fellow at the University of Manchester (previously postdoctoral fellow at Cardiff University)
