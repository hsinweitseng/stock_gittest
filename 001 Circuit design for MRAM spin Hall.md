Spin hall high density array design with circuit

Hsin-wei Tseng, Jongyeon Kim, Pei-feng, Jordan Katine

HGST, A Western Digital Company

###Working time: since 8/6/2016


### Disclosure and conferenc paeper writing 
- [ ] Concept forming
- [ ] Passing through the writing block
- [ ] Finishing the drafting
- [ ] Getting feedback from the related person. 
- [ ] Data and information searching

### Motivation
* Future direction of MRAM design for shrinking the Cache memory
* Non of the NVM memory could possibilily compete with MRAM structures
* MRAM show up in the embedded system in 2017, 2018 in low power high performance consumer product (Apple Watch).
* More demanding and investment for enhancing MRAM technology into maturity. 
* ReRAM would struggle for getting a space for embedded technology and also losing to 3D NAND technology. 
* Spin Hall material is coming to maturity.
* Using external transistor to reduce keeping the large V<sub>sense</sub>
* Embedded application. Will need to improve the cost, scalability, scale, ecosystem. 
* Height density cross point for storage controller, mcu,fpga, or asic application to accelerating SSD application. 
* Patent on the circuit space for the novel memeory is under investigated. 

### Issues to be resolve
* Old patent didn’t address the leakage current issue.
* Read disturbance issue for crosspoint array.
* V<sub>VCMA</sub> need asymmetric correction.

### Design concept and drawing (idea disclosure)
* Using spin Hall device to reduce device layout area for embedded memory cache application. 
* Due to external transistor size, additional area is needed. More  embedded high density NVM memory is needed. 
* Need OTS implementation for read improvement for large array. 
* future neuro-network-based. 
* Asymmetric line for improving size.
* Patent reference:
* Two Cornell’s patent
* two of my spin hall papers
* Large transistor design to provide enough power for fast read.
* Asymmetric bit line design for offsetting V<sub>VCMA</sub> for the last bit.
* V<sub>read</sub> problem for the last bit and matrix compensation.
* Double MgO free layer design with spin hall structure for sythentic  free Spin Hall MRAM design.	



### Table of key parameters for small Spin-Hall array implementation

#28nm node TSMC technology
|Physical Spin Hall system parameters |||||| 
|:--- |:---- |:----:| ----:|
|Array size| 1x1 |
|Line material|Pt|beta-W|Ta|CuBi,CuIr|
|SHE angle|0.07|0.33|0.12|
|Interface stack |Pt|W/Hf | |
|Thermal stability |60 | | |
|Material resistivity(uOhm-cm)||260|
|Jcwrite(A/cm<sup>2</sup>)|10<sup>8</sup>| | |
|MTJ device|20nm x 20nm
|Resistance area product (RA) (ohm*um<sup>2</sup>)|10||
|R<sub>HRS</sub>(kOhm)|
|R<sub>LRS</sub> (kOhm)|10
|Line width|28nm| | |
|Line thickness|6nm
|Line resistance|

#Write Operation
|Design parameters |||||| 
|:--- |:---- |:----:| ----:|
|Write operation|
|V<sub>write</sub> (mA)| left | nicely | right  |
|V<sub>VCMA</sub>|
|Iwrite | | | |

#Read Operation
|Design parameters |1x1| 2x2 | 3x3  | 
|:--- |:---- |:----:| ----:|
|Array size| is | is | is  |
|Line material|Pt|W|Ta|CuBi,CuIr|
|SHE angle|0.07|0.33|0.12|
|Interface stack |Pt|W/Hf | |


Key parameter form HGST spec for ReRAM/OTS design
|Key parameter|


###	To FIND: Information and Spec to look up on line
- [ ] Pt resistivity
- [ ] Transistor deisng power and current voltage strength
- [ ] Current exciting design
- [ ] 
- [ ] 

### To DO: Draw CAD draw for circuit design
- [ ]  MRAM embedded ASIC performance, and peformance chart for MRA
- [ ]  Magnetic-based logic operation

### To be DRAW: Illusion to be included in draft
- [X] standard L2-cache SRAM design with 6T transistor connection
- [ ] Layout design for 1T1MTJ transistor desig
- [ ] Internal illustration for MRAM design.

### Reference
* Luqiao’s crosspoint patent[1]
* Patrick crosspoint patent for structure
* Standford Philips Wang cross point estimation
* 1T1MTJ stats of art results
* Jongyeon Kim two patent disclosure
* Jongyeon Kim’s paper about spin torque logic.

[1]: Liu, L. et al. Spin-torque switching with the giant spin Hall effect of tantalum. Science 336, 555–8 (2012).