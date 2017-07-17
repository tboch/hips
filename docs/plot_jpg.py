"""Basic example how to plot a sky image with the hips package"""
from astropy.coordinates import SkyCoord
from hips import HipsSurveyProperties
from hips import make_sky_image
from hips.utils import WCSGeometry

# Compute the sky image
url = 'http://alasky.u-strasbg.fr/Fermi/Color/properties'
hips_survey = HipsSurveyProperties.fetch(url)
geometry = WCSGeometry.create_simple(
    skydir=SkyCoord(0, 0, unit='deg', frame='galactic'),
    width=2000, height=1000, fov="3 deg",
    coordsys='galactic', projection='AIT',
)
image = make_sky_image(geometry=geometry, hips_survey=hips_survey, tile_format='jpg')

# Draw the sky image
import matplotlib.pyplot as plt
ax = plt.subplot(projection=geometry.wcs)
ax.imshow(image, origin='lower')