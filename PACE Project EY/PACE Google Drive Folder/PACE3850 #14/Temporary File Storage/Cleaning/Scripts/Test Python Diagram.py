from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='EER Diagram for Adventure Planning System')

# Entities
dot.node('Location', 'Location\n(LocationID, Name, Description, Image)')
dot.node('Route', 'Route\n(RouteID, Name, StartTime, EstimatedTime, StartLocationID, EndLocationID)')
dot.node('Waypoint', 'Waypoint\n(WaypointID, ArrivalTime, DepartureTime)')
dot.node('PointOfInterest', 'PointOfInterest\n(POIID, Name, GoogleMapsRef, Photo, Description)')
dot.node('Person', 'Person\n(PersonID, Name, Password, Email)')
dot.node('Plan', 'Plan\n(PlanID, Name, DateCreated, LastUpdated)')

# Sub-Entities (Inheritance)
dot.node('Animal', 'Animal\n(POIID, Classification, Poisonous, Venomous, Aggressive, Endangered)')
dot.node('Plant', 'Plant\n(POIID, Poisonous, Edible, AllergyCausing)')
dot.node('Store', 'Store\n(POIID, Barcode)')
dot.node('HistoricalPlace', 'HistoricalPlace\n(POIID, YearsInExistence)')

# Relationships
dot.edge('Route', 'Waypoint', label='has', constraint='true')
dot.edge('Route', 'Location', label='starts at', constraint='true')
dot.edge('Route', 'Location', label='ends at', constraint='true')
dot.edge('Waypoint', 'Location', label='at', constraint='true')
dot.edge('Location', 'PointOfInterest', label='can view', constraint='true')
dot.edge('Person', 'Plan', label='creates', constraint='true')
dot.edge('Plan', 'Route', label='includes', constraint='true')
dot.edge('Plan', 'Location', label='includes', constraint='true')

# Inheritance Relationships (Use empty labels to denote generalization)
dot.edge('PointOfInterest', 'Animal', label='', arrowhead='none', style='dashed')
dot.edge('PointOfInterest', 'Plant', label='', arrowhead='none', style='dashed')
dot.edge('PointOfInterest', 'Store', label='', arrowhead='none', style='dashed')
dot.edge('PointOfInterest', 'HistoricalPlace', label='', arrowhead='none', style='dashed')

# Render the diagram
dot.render('adventure_planning_system', format='pdf', cleanup=True)

# Output the dot code as well, for manual editing if needed
with open('adventure_planning_system.dot', 'w') as f:
    f.write(dot.source)

print("EER Diagram created and saved as 'adventure_planning_system.pdf'")
