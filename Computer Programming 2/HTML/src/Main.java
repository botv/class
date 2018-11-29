import java.net.URL;

public class Main {

    public static void main(String[] args) throws Exception {
        String html = URLReader.read(new URL("https://benbotvinick.com"));
        System.out.println(html);
    }
}
