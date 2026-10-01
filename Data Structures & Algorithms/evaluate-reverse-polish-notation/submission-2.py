class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = '+-*/' 

        for t in tokens:
            if t not in operators:
                st.append(int(t))
            else:
                a = int(st.pop())
                b = int(st.pop())
                
                match t:
                    case '+':
                        st.append(a + b)
                    case '-':
                        st.append(b - a)
                    case '*':
                        st.append(a * b)
                    case '/':
                        st.append(int(b / a))
                        
        result = st.pop()
        return result
            
