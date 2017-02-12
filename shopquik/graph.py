import matplotlib.pyplot as plt
import networkx
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class MyNode:
#x,y should be in range 0-1
    def __init__(self, x, y, aisle_num, node_type):
        self.x = x
        self.y = y
        self.aisle_num = aisle_num
        self.node_type = node_type


def create_store_map():
#Get the hardcoded map
    G = networkx.Graph()

    aisle_nodes = []
    aisle_edges = []

#vertical aisles
    num_vert_aisles = 4
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
    num_hori_aisles = 6
    for i in range(1, num_hori_aisles + 1):
#In x,y format
        aisle_nodes.append(((num_vert_aisles + 1) * 0.1, i * 0.1))
        aisle_nodes.append(((num_vert_aisles + 1)* 0.1 + 0.4, i * 0.1))

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


def display_map(store_map):
    img_dim = 800
    img_scale = img_dim/1;

    im = Image.new('RGB', (img_dim, img_dim), 'white')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('arial.ttf', int(10 * img_scale / img_dim ))

    aisle_items = {}
#Plot items
    dot_radius = 0.005
    dot_radius = dot_radius * img_scale
    for node in store_map.nodes(data = True):
        node = node[1]['data']
        if node.node_type is not None:
            x = node.x * img_scale
            y = img_dim - node.y * img_scale
            draw.ellipse([x-dot_radius, y-dot_radius, x+dot_radius, y+dot_radius], fill='red')
            if node.aisle_num in aisle_items:
                aisle_items[node.aisle_num].append(node.node_type)
            else:
                aisle_items[node.aisle_num]  = [node.node_type]

    aisle_text = ''
    for edge in store_map.edges(data = True):
        node0 = store_map.node[edge[0]]['data']
        node1 = store_map.node[edge[1]]['data']
        draw.line((node0.x * img_scale, img_dim - node0.y * img_scale, node1.x * img_scale, img_dim - node1.y * img_scale), fill='black')
        if edge[2]['aisle_num'] != 0:
#Per aisle item list
            if edge[2]['aisle_num'] in aisle_items:
                aisle_text += 'Aisle ' + str(edge[2]['aisle_num'])
                for aisle_item in aisle_items[edge[2]['aisle_num']]:
                    aisle_text += '\n' + str(aisle_item)
                aisle_text += '\n\n'

#Text co-ords
            text_x = (node0.x + node1.x + 0.02) * img_scale / 2
            text_y = img_dim - (node0.y + node1.y + 0.03) * img_scale / 2
            draw.text((text_x, text_y), 'Aisle ' + str(edge[2]['aisle_num']), 'black', font=font)

    im.save('test.bmp')
    print(aisle_text)


def add_items(store_map):
    items = [
            MyNode(0.1, 0.15, 1, 1),
            MyNode(0.1, 0.2, 1, 1),
            MyNode(0.3, 0.2, 2, 1),
            ]

    for item in items:
        store_map.add_node(max(store_map.nodes()) + 1, data = item)


def main():
    store_map = create_store_map()
    add_items(store_map)
    display_map(store_map)

if __name__ == '__main__':
    main()