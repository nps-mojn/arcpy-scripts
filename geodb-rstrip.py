
import arcpy
import os

arcpy.env.workspace = "path/to/geodatabase.gdb"

datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

print datasets

tables = arcpy.ListTables()
for table in tables:
    path = os.path.join(arcpy.env.workspace, table)
    for field in arcpy.ListFields(path, "*", "String"):
        print field.type
        with arcpy.da.UpdateCursor(path, field.name) as cursor:
            for row in cursor:
                value = row[0]
                if value is None:
                    continue
                value = value.encode("utf-8")
                print path, field.name, value
                value = str(value).rstrip()
                row[0] = value
                cursor.updateRow(row)
        del cursor

for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        path = os.path.join(arcpy.env.workspace, ds, fc)
        for field in arcpy.ListFields(path, "*", "String"):
            print field.type
            with arcpy.da.UpdateCursor(path, field.name) as cursor:
                for row in cursor:
                    value = row[0]
                    if value is None:
                        continue
                    value = value.encode("utf-8")
                    print path, field.name, value
                    value = str(value).rstrip()
                    row[0] = value
                    cursor.updateRow(row)
            del cursor
