import java.awt.*;

class Tile {
    double resistance;
    Color color;

    Tile() {
        this.resistance = Math.random();
        int rgb = (int) ((1 - this.resistance) * 255);
        this.color = new Color(rgb, rgb, rgb);
    }

}
