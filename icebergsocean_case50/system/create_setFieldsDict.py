# This program will create a new setFieldsDict file with the water layer
# transitioning from salty (alpha.other) to fresh (alpha.water) linearly 
# over a total depth H.

# to run this program, type
#     python create_setFieldsDict.py

# These parameters can be changed as needed.
N = 64 # number of vertical blocks
dy = 1./64 # size of vertical block
H = 56*dy # water depth

### SHOULDN'T NEED TO CHANGE BELOW:

template = r"""/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  3.0.x                                 |
|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       dictionary;
    location    "system";
    object      setFieldsDict;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

defaultFieldValues
(
    volScalarFieldValue alpha.air 1
    volScalarFieldValue alpha.other 0
    volScalarFieldValue alpha.water 0
);

%(regions)s

// ************************************************************************* //
"""

boxTemplate = r"""
    boxToCell
    {
        box (0 %(ymin)f 0) (1.0 %(ymax)f 0.1);
        fieldValues
        (
            volScalarFieldValue alpha.air 0
            volScalarFieldValue alpha.other %(alphaSalty)f
            volScalarFieldValue alpha.water %(alphaFresh)f
        );
    }
"""
p = {}

regions = "regions\n(\n"

y = 0
while y < H:
    p['ymin'] = y
    p['ymax'] = y+dy
    p['alphaFresh'] = (y+dy/2)/H
    p['alphaSalty'] = 1-(y+dy/2)/H

    regions += boxTemplate % p

    y += dy

regions += ");\n"

setFieldsDict = template % {'regions': regions}

# Save file
filename = 'setFieldsDict'
outfile = open(filename, 'w')
outfile.write(setFieldsDict)
outfile.close()

