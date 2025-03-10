#include <stdexcept>
#include <vector>
#include <algorithm>
#include <iostream>

// fuuuuusdasdklfasd;jfaskldfjalskdfja;sdlkfj;asdkfjaklsdjf how did i get this so wrong aguhghhghghghghgh

class MinStack {
  std::vector<std::pair<float, float> > stack;

public:
  void push(float x) {
    if (stack.size() == 0) {
      stack.push_back(std::pair<float, float>(x, x));
    } else {
      stack.push_back(std::pair<float, float>(x, std::min(x, stack[stack.size() - 1].second)));
    }
  }

  float pop() {
    if (stack.size() == 0) {
      throw std::underflow_error("empty stack");
    }
    float tmp = stack[stack.size() - 1].first;
    stack.pop_back();
    return tmp;
  }

  float min() {
    if (stack.size() == 0) {
      throw std::underflow_error("empty stack");
    }
    return stack[stack.size() - 1].second;
  }
};


int main() {
  MinStack s;

  s.push(1);
  s.push(5);
  s.push(-10);
  std::cout << s.min() << std::endl;
  s.pop();
  std::cout << s.min() << std::endl;
  s.push(5);
  s.push(2);
  s.push(-100);
  s.push(5);
  std::cout << s.min() << std::endl;
  std::cout << s.pop() << std::endl;
}