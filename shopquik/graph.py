import matplotlib.pyplot as plt
import networkx
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class MyNode:
#x,y should be in range 0-1
    def __init__(self, x, y, aisle_num, node_type):
        self.x = 1 - x
        self.y = 1 - y
        self.aisle_num = aisle_num
        self.node_type = node_type


def create_store_map():
#Get the hardcoded map
    G = networkx.Graph()

    aisle_nodes = []
    aisle_edges = []

#vertical aisles
    num_vert_aisles = 3
    for i in range(1, num_vert_aisles + 1):
#In x,y format
        aisle_nodes.append((i * 0.1, 0.5))
        aisle_nodes.append((i * 0.1, 0.1))

#Index of nodes followed by aisle_num. aisle_num = 0 if edge is not an aisle.
    for i in range(0, num_vert_aisles):
        aisle_edges.append((2 * i, 2 * i + 1, i + 1))

    for i in range(0, num_vert_aisles - 1):
        aisle_edges.append((2 * i + 1, 2 * i + 3, 0))

#Horizontal aisles
    num_hori_aisles = 7
    for i in range(1, num_hori_aisles + 1):
#In x,y format
        aisle_nodes.append(((num_vert_aisles + 1) * 0.1, i * 0.1))
        aisle_nodes.append(((num_vert_aisles + 1)* 0.1 + 0.3, i * 0.1))

#Index of nodes followed by aisle_num. aisle_num = 0 if edge is not an aisle.
    for i in range(0 , num_hori_aisles):
        aisle_edges.append((2 * (num_vert_aisles + i), 2 * (num_vert_aisles + i) + 1, num_vert_aisles + i + 1))

    for i in range(0, num_hori_aisles - 1):
        aisle_edges.append((2 * (num_vert_aisles + i) + 1, 2 * (num_vert_aisles + i) + 3, 0))

#Create aisle nodes with consective node ids
    node_id = 0
    for aisle_node in aisle_nodes:
        G.add_node(node_id, data = MyNode(aisle_node[0], aisle_node[1], None, None))
        node_id = node_id + 1

#Add edges
    for aisle_edge in aisle_edges:
        G.add_edge(aisle_edge[0], aisle_edge[1], aisle_num = aisle_edge[2])

    return G


def display_map(store_map, highlight_aisles, filename):
    img_dim = 800
    img_scale = img_dim/1;

    im = Image.new('RGB', (img_dim, img_dim), 'white')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('arial.ttf', int(12 * img_scale / img_dim ))

    highlight_aisle = {}
    for edge in store_map.edges(data = True):
        node0 = store_map.node[edge[0]]['data']
        node1 = store_map.node[edge[1]]['data']
        
        if edge[2]['aisle_num'] in highlight_aisles:
            draw.line((node0.x * img_scale, img_dim - node0.y * img_scale, node1.x * img_scale, img_dim - node1.y * img_scale), fill='red', width=2)
        else:
            draw.line((node0.x * img_scale, img_dim - node0.y * img_scale, node1.x * img_scale, img_dim - node1.y * img_scale), fill='black', width=3)

        if edge[2]['aisle_num'] != 0:
#Text co-ords
            text_x = (node0.x + node1.x + 0.02) * img_scale / 2
            text_y = img_dim - (node0.y + node1.y + 0.04) * img_scale / 2
            draw.text((text_x, text_y), 'Aisle ' + str(edge[2]['aisle_num']), 'black', font=font)

    im.save(filename + '.bmp')


def add_items(store_map):
    items = [
            MyNode(0.1, 0.15, 1, 1),
            MyNode(0.1, 0.2, 1, 1),
            MyNode(0.3, 0.2, 2, 1),
            ]

    for item in items:
        store_map.add_node(max(store_map.nodes()) + 1, data = item)


def main():
    filename = 'test1'
    if 1:
        store_map = create_store_map()
        add_items(store_map)
        networkx.write_gpickle(store_map, filename + '.gpickle')
    else:
        store_map = networkx.read_gpickle(filename + '.gpickle')
    
    highlight_aisles = [1, 2, 5]
    display_map(store_map, highlight_aisles, filename)

if __name__ == '__main__':
    main()