import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            if (words[i].indexOf(x) != -1) {
                result.add(i);
            }
        }
        return result;
    }
}

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] words = {"hello", "world", "java", "programming"};
        char x = 'o';
        List<Integer> indices = solution.findWordsContaining(words, x);
        System.out.println(indices); // Output: [0, 1]
    }
}
