
class Map:

    def __init__(self):

        # variables de class
        self.nb_tiles_X = 12            # int : nb de tuiles sur X
        self.nb_tiles_Y = 12            # int : nb de tuiles sur Y
        self.file_map_content = ""      # string : contenu du fichier lvl.txt
        self.lvl = []
        
        # construction de l'obj
        self.load_map_from_file(1)
        self.load_lvl()

    #charge le contenu du fichier texte dans une str
    def load_map_from_file(self, lvl):

        file_map = open("./lvl/lvl1.txt", "r")
        self.file_map_content = file_map.read()
        file_map.close()

    # rempli self.lvl avec une liste de Tile
    def load_lvl(self):
        
        tmp = self.file_map_content.replace('\n', '')
        
        i = 0
        for y in range(0, self.nb_tiles_Y):
            for x in range(0, self.nb_tiles_X):
                self.lvl.append(Tile(x, y, tmp[i]))
                i += 1
                if x == self.nb_tiles_X - 1 :
                    x = 0

class Tile:

    def __init__(self, num_X, num_Y, m_type):

        self.num_tile_X = num_X
        self.num_tile_Y = num_Y
        self.type = m_type

test = Map()

print("test")