import biketrauma
from biketrauma.io.Load_db import Load_db
from biketrauma.vis.plot_location import plot_location
from biketrauma.preprocess.get_accident import get_accident

df = biketrauma.Load_db().save_as_df()
biketrauma.plot_location(biketrauma.get_accident(df))

