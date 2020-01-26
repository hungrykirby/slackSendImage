from data_packages import generateGraph
from api_packages import googleItem

# generateGraph.GraphGenerator("title", "test.png").create_pressure_graph([8, 15], [855, 1550])
googleItem.GoogleItem(True).fetch_pressure_time()