from allthepairs.all_pairs2 import all_pairs2 as all_pairs

"""
Demo of the basic functionality - just getting pairwise/n-wise combinations
"""


# sample parameters are is taken from
# http://www.stsc.hill.af.mil/consulting/sw_testing/improvement/cst.html

parameter_names = ["Brandname", "Version", "ConnectionType", "Wages", "Numbers"]

parameters = [ [ "Brand X", "Brand Y" ]
             , [ "98", "NT", "2000", "XP"]
             , [ "Internal", "Modem" ]
             , [ "Salaried", "Hourly", "Part-Time", "Contr." ]
             , [ 6, 10, 15, 30, 60 ]
             ]

pairwise = all_pairs( parameters )

print("PAIRWISE:")
for i, v in enumerate(pairwise):
    print("%i:\t%s" % (i, str(v)))

# import csv
#
# with open('test.csv', 'w') as csvfile:
#     w = csv.writer(csvfile)
#     w.writerow(parameter_names)
#     for i, v in enumerate(pairwise):
#         w.writerow(v)
