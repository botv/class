import java.net.*;
import java.io.*;

class URLReader {
	static String read(URL url) throws Exception {

		StringBuilder html = new StringBuilder();
		BufferedReader in = new BufferedReader(
				new InputStreamReader(url.openStream()));

		String inputLine;
		while ((inputLine = in.readLine()) != null)
			html.append(inputLine);
		in.close();

		return html.toString();
	}
}