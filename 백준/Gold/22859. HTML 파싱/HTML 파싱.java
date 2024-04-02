import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split("");
        StringBuilder sb = new StringBuilder();

        int i = 0;
        while (i < input.length) {
            // tag appears
            if (input[i].equals("<")) {
                // tag
                String tag = input[++i];
                while (!input[++i].equals(">")) {
                    tag += input[i];
                }

                // opening tag
                if (tag.charAt(0) != '/') {
                    // div
                    if (tag.length() > 3 && tag.substring(0, 3).equals("div")) {
                        String title = tag.substring(11, tag.length()-1);
                        sb.append("title : ").append(title).append("\n");
                    // p
                    } else if (tag.equals("p")) {
                        i++;
                        String content = "";
                        while (i < input.length) {
                            // subTag appears
                            if (input[i].equals("<")) {
                                String subTag = input[++i];
                                while (!input[++i].equals(">")) {
                                    subTag += input[i];
                                }
                                // closing pTag
                                if (subTag.equals("/p")) {
                                    content = content.trim();
                                    // trim white space
                                    String tmp = "";
                                    int j = 0;
                                    while (j < content.length()) {
                                        if (content.charAt(j) == ' ') {
                                            while (content.charAt(j) == ' ') {
                                                j++;
                                            }
                                            tmp += " ";
                                            continue;
                                        }
                                        tmp += content.charAt(j++);
                                    }
                                    sb.append(tmp).append("\n");
                                    break;
                                }
                            // content
                            } else {
                                content += input[i];
                            }
                            i++;
                        }
                    }
                }
            }

            i++;
        }

        System.out.println(sb.toString());
    }
}