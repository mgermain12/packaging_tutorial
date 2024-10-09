from biketrauma.io import Load_db

df = biketrauma.Load_db().save_as_df()
biketrauma.plot_location(biketrauma.get_accident(df))
