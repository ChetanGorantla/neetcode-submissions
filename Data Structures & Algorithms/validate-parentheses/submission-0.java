
class Solution {
    public boolean isValid(String s) {
        if (s.length() % 2 == 1) {
            return false;
        }

        Stack<Character> stack = new Stack<>();
        Map<Character, Character> opp = new HashMap<>() {{
            put(')', '(');
            put(']', '[');
            put('}', '{');
        }};

        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);

            if (opp.containsKey(currentChar)) { //if we are on a closing bracket
                
                if (!stack.isEmpty() && stack.peek() == opp.get(currentChar)) {//if the previous stack element is the opening for us
                    stack.pop(); //remove previous stack element and skip current addition
                } else {
                    return false; //we have a closing bracket that doesnt have an opening bracket matching same type right before it
                }
            } else {
                stack.push(currentChar);
            }
        }

        return stack.isEmpty();
    }
}
