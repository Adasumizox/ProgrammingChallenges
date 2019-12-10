int basicOp(char op, int val1, int val2) {
  switch (op) {
    case '+': return val1 + val2;
              break;
    case '-': return val1 - val2;
              break;
    case '*': return val1 * val2;
              break;
    case '/': return val1 / val2;
              break;
    default: return -99999;
  }
}