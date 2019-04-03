# pygal包已经更新为pygql_maps_world
import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'North,Central,and Sourth America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('america.svg')