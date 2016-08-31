# This program will create a new setFieldsDict file with the water layer
# transitioning from salty (alpha.other) to fresh (alpha.water) linearly 
# over a total depth H.

# to run this program, type
#     python create_setFieldsDict.py

# These parameters can be changed as needed.
N = 120 # number of vertical blocks
dz = 0.6/120 # size of vertical block
H = 0.55 # water depth

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
    volScalarFieldValue alpha.fresh 1
    volScalarFieldValue alpha.salty 0
);

%(regions)s

// ************************************************************************* //
"""

boxTemplate = r"""
    boxToCell
    {
        box (-100 -100 %(zmin)f) (100 100 %(zmax)f);
        fieldValues
        (
            volScalarFieldValue alpha.salty %(alphaSalty)f
            volScalarFieldValue alpha.fresh %(alphaFresh)f
        );
    }
"""
p = {}

regions = "regions\n(\n"

z = 0
while z < H:
    p['zmin'] = z
    p['zmax'] = z+dz
    p['alphaFresh'] = (z+dz/2)/H
    p['alphaSalty'] = 1-(z+dz/2)/H

    regions += boxTemplate % p

    z += dz

regions += ");\n"

setFieldsDict = template % {'regions': regions}

# Save file
filename = 'setFieldsDict'
outfile = open(filename, 'w')
outfile.write(setFieldsDict)
outfile.close()
