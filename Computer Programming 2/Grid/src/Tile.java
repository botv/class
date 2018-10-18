import java.awt.*;

class Tile {
    double resistance;
    Color color;

    Tile() {
        this.resistance = Math.random();
        int rgb = (int) (this.resistance * 100);
        this.color = new Color(rgb, rgb, rgb);
    }

}
