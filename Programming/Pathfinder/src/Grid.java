import java.util.ArrayList;

class Grid {
    Tile[][] tiles;

    Grid(int width, int height) {
        this.tiles = new Tile[width][height];

        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                tiles[x][y] = new Tile();
            }
        }
    }
}
