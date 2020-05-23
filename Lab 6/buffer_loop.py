# basic buffer to run via the ArcMap python window

# import arcpy module
import arcpy

# will be used for filtering in technical variation option 1 
import fnmatch

# buffer input feature class
fc = "mc_major_roads"

# choosing technical variation option 1

# populating all feature classes present
feature_classes = arcpy.ListFeatureClasses()

# filtering to find the ones starting with our buffer input feature class
filtered = fnmatch.filter(feature_classes, fc+'*')

# looping through the filtered classes
for feature_class in filtered:
    # in the filtered list checking if the class exist
	if arcpy.Exists(feature_class):
		# if it does deleting it
		arcpy.Delete_management(feature_class)

# after all deletions clearing the cache
arcpy.ClearWorkspaceCache_management()
# technical variation option 1 Ends 

# distance to buffer the roads
distance_list = ["100 meters", "200 meters", "300 meters"]

#looping through each distance
for dist in distance_list:
    # for output name appending feature class name 
	# with first three characters of dist value 
	outname = fc + "_" + dist[0:3]
	
	# providing user feedback
	print ("Now Buffering " + outname)
	
	arcpy.Buffer_analysis(fc, outname, dist)

# program ends user feedback
print ("Finished Buffering")
