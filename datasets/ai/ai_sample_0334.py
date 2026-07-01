import java.net.URL;
import java.util.Scanner;
 
public class QueryOverflow {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://api.stackexchange.com/2.2/search?order=desc&sort=activity&tags=python&site=stackoverflow");
        Scanner scan = new Scanner(url.openStream());
        String str = new String();
        while (scan.hasNext())
            str += scan.nextLine();
        scan.close();
 
        JSONObject obj = new JSONObject(str);
        JSONArray items = obj.getJSONArray("items");
        for (int i = 0; i < items.length(); i++)
        {
            // print title
            System.out.println(items.getJSONObject(i).getString("title"));
            // print answer
            System.out.println(items.getJSONObject(i).getJSONObject("accepted_answer").getString("body"));
        }
    }
}