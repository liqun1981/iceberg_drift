case304

***************************** 
Change(s) from previous case:
	- increased endTime from 10-20 seconds

Stable:
	- no
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
		hex (0 1 2 3 4 5 6 7) (20 20 20) 
		simpleGrading (1 1 ((0.4 10 1)(0.2 20 1)(0.4 10 1)))
	);


floatingObject 
	size: 0.2x0.2x0.1
	density: 500
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
	deltaT: 0.0001
	endTime: 20
	crash time: 11.2

Other:

