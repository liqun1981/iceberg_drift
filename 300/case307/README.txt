case307

***************************** 
Stable:
	- yes

Change(s) from previous case:
	- made floatingObject bigger and more dense

Result:
	- it ran nicely - less sloshing

Change for next case:
	- increase the spring stiffness to try and get more lateral motion

******************************

Domain
	vertices
	(
	    	(0 0 0)
	    	(1 0 0)
		(1 1 0)
		(0 1 0)
		(0 0 1)
		(1 0 1)
		(1 1 1)
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
	stiffness: 0.08
	damping: 0
	restLength: 3.2

Time
	deltaT:  1e-09
	endTime: 20
	crash time: n/a

Other:

