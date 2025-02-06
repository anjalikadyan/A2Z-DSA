# Strings in C++ and Python

## Strings in C++
### Definition
In C++, a string is a sequence of characters. It can be implemented using:
1. C-style character arrays
2. The `std::string` class from the Standard Library

### C-style Strings
A C-style string is an array of characters terminated by a null character `\0`.

#### Example:
```cpp
#include <iostream>
using namespace std;

int main() {
    char str[] = "Hello, World!";
    cout << str << endl;
    return 0;
}
```

### `std::string` Class
The `std::string` class provides more flexibility and ease of use compared to C-style strings.

#### Example:
```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string str = "Hello, World!";
    cout << str << endl;
    return 0;
}
```

### String Operations in C++
- Concatenation: `s1 + s2`
- Append: `s.append(s2)`
- Length: `s.length()`
- Substring: `s.substr(start, length)`
- Find: `s.find("text")`

#### Example:
```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s1 = "Hello";
    string s2 = " World";
    string s3 = s1 + s2;
    cout << "Concatenated String: " << s3 << endl;
    cout << "Length: " << s3.length() << endl;
    cout << "Substring: " << s3.substr(0, 5) << endl;
    return 0;
}
```

## Strings in Python
### Definition
In Python, a string is an immutable sequence of Unicode characters enclosed in single (`'`) or double (`"`) quotes.

### Example:
```python
str1 = "Hello, World!"
print(str1)
```

### String Operations in Python
- Concatenation: `s1 + s2`
- Length: `len(s)`
- Slicing: `s[start:end]`
- Finding substring: `s.find("text")`
- Upper/Lower case: `s.upper()`, `s.lower()`

#### Example:
```python
s1 = "Hello"
s2 = " World"
s3 = s1 + s2
print("Concatenated String:", s3)
print("Length:", len(s3))
print("Substring:", s3[:5])
```

Both C++ and Python provide powerful string manipulation capabilities, with C++ requiring more explicit memory management, while Python offers more flexibility with built-in methods.

