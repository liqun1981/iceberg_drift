case311

***************************** 
Stable:
	- no

Change(s) from previous case:
	- increased domain in x-dir from 1 to 2

Result:
	- the objects leading edge immediately got dragged underwater

Change for next case:
	- reduce the density of the object to 500 so that it will be at its waterline initially

******************************

Domain
	vertices
	(
	    	(0 0 0)
	    	(2 0 0)
		(2 1 0)
		(0 1 0)
		(0 0 1)
		(2 0 1)
		(2 1 1)
		(0 1 1)
	);	
	blocks
	(
	    hex (0 1 2 3 4 5 6 7) (30 30 30) 
	    simpleGrading (
	    (1)
	    (1)
	    ((0.4 10 1)(0.2 40 1)(0.4 10 1)))
	);


floatingObject 
	size: 0.4x0.4x0.3
	density: 900
	CentreOfMass: (0.5 0.5 0.5)
	innerDist: 0.05
	outerDist: 0.35

Spring 
	anchor:  (4.0 0.50 0.50)
	refAttachmentPt: (0.5 0.50 0.50)
	stiffness: 1
	damping: 0
	restLength: 3.2

Time
	deltaT:  1e-09
	endTime: 40
	crash time: 1.2

Other:

