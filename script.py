import biketrauma
from .io.Load_db import Load._db
from .vis.plot_location import plot_location
from .preprocess.get_accident import get_accident

df = biketrauma.Load_db().save_as_df()
biketrauma.plot_location(biketrauma.get_accident(df))

