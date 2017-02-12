import matplotlib.pyplot as plt
import networkx
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class MyNode:
    def __init__(self, node_type, x, y):
#x,y should be in range 0-1
        self.x = x
        self.y = y
        self.node_type = node_type


def create_store_map():
#Get the hardcoded map
    G = networkx.Graph()
#In x,y format
    aisle_nodes = [(0.1, 0.1), (0.1, 0.2), (0.3, 0.1), (0.3, 0.3)]

#Index of nodes followed by aisle_num.aisle_num = 0 if not an aisle
    aisle_edges = [(0, 1, 1), (0, 2, 0), (2, 3, 2)]

#Create aisle nodes with consective node ids
    node_id = 0
    for aisle_node in aisle_nodes:
        G.add_node(node_id, data = MyNode(0, aisle_node[0], aisle_node[1]))
        node_id = node_id + 1

#Add edges
    for aisle_edge in aisle_edges:
        G.add_edge(aisle_edge[0], aisle_edge[1], aisle_num = aisle_edge[2])

    return G


def display_map(store_map):
    img_dim = 2000
    img_scale = 2000/1;

    im = Image.new('RGB', (img_dim, img_dim), 'white')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('arial.ttf', 32)

    for edge in store_map.edges(data=True):
        node0 = store_map.node[edge[0]]['data']
        node1 = store_map.node[edge[1]]['data']
        draw.line((node0.x * img_scale, img_dim - node0.y * img_scale, node1.x * img_scale, img_dim - node1.y * img_scale), fill='black')
        if edge[2]['aisle_num'] != 0:
            if node0.y < node1.y:
                text_x = (node0.x - 0.01) * img_scale
                text_y = img_dim - (node0.y - 0.01)* img_scale
                draw.text((text_x, text_y), 'Aisle ' + str(edge[2]['aisle_num']), 'black', font=font)

    im.save('test.bmp')


def main():
    store_map = create_store_map()
    display_map(store_map)


if __name__ == '__main__':
    main()